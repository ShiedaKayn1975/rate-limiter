from collections import deque
from datetime import datetime
from time import time
from connections.redis_connection import redis_connection

class SlidingWindowLog:
    # Assume that window size is the number of requests allowed in a time_unit
    # Assume that time_unit is a period of time in hour, example: 0.4 hour, 1 hour, 2 hours...

    def __init__(self, window_size, time_unit):
        self.window_size = window_size
        self.time_unit = time_unit*60*60 # convert hour into second
        self.redis = redis_connection()

    def request(self, key, timestamp = time()):
        try:
            self.log = self.__find_or_create_log(key)
            self.key = key
        except Exception as ex:
            # Return True if the connection to the redis server had an error!
            # If the redis server goes down, the developer can choose whether to use the rate limiter or not
            
            return True

        # Remove outdated logs from the window
        self.__clean_log(timestamp)

        # Check if request is allowed based on window size
        if len(self.log) < self.window_size:
            # Add the new request timestamp
            self.log.append(timestamp)
            
            # Save new log to Redis
            self.__save_log()
            print(f'Time {datetime.fromtimestamp(timestamp)}, accepted = True')
            return True
        else:
            print(f'Time {datetime.fromtimestamp(timestamp)}, accepted = False')
            return False

    def __clean_log(self, timestamp):
        # Calculate minimum timestamp allowed in the current window
        min_timestamp = timestamp - self.time_unit
        while self.log and self.log[0] < min_timestamp:
            self.log.pop(0)
    
    def __find_or_create_log(self, key):
        # Find existed log, if it isn't available, create a new one.
        if self.redis.exists(key):
            log = self.redis.get(key)
            log_decoded = log.decode()
            return [float(i) for i in log_decoded.split(",")]
        else:
            self.redis.set(key, "")
            return []
            
    
    def __save_log(self):
        self.redis.set(self.key, str.encode(",".join([str(i) for i in self.log])))        
