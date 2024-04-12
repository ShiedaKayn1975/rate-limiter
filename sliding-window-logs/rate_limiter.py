from collections import deque
from datetime import datetime
from time import time

class SlidingWindowLog:
    # Assume that window size is the number of requests allowed in a time_unit
    # Assume that time_unit is a period of time in hour, example: 0.4 hour, 1 hour, 2 hours...

    def __init__(self, window_size, time_unit):
        self.window_size = window_size
        self.time_unit = time_unit*60*60 # convert hour into second
        self.log = deque()

    def request(self, timestamp = time()):
        # Remove outdated logs from the window
        self.clean_log(timestamp)

        # Check if request is allowed based on window size
        if len(self.log) < self.window_size:
            # Add the new request timestamp
            self.log.append(timestamp)
            print(f'Time {datetime.fromtimestamp(timestamp)}, accepted = True')
            return True
        else:
            print(f'Time {datetime.fromtimestamp(timestamp)}, accepted = False')
            return False

    def clean_log(self, timestamp):
        # Calculate minimum timestamp allowed in the current window
        min_timestamp = timestamp - self.time_unit
        while self.log and self.log[0] < min_timestamp:
            self.log.popleft()

# # Example usage
window_size = 3  # Allow 3 requests in a window
time_unit = 1  # Window size is in seconds

rate_limiter = SlidingWindowLog(window_size, time_unit)
times = [
    1642612385.0,
    1642613251.0,
    1642614327.0,
    1642615249.0,
    1642616145.0,
    1642616401.0,
    1642618209.0,
    1642618335.0,
    1642618440.0,
    1642618800.0
]

for i in times:
    rate_limiter.request(i)