from services.rate_limiter import SlidingWindowLog
from functools import wraps
from flask import request

DEFAULT_WINDOW_SIZE = 3
DEFAULT_TIME_UNIT = 1

def limiter(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        window_size = DEFAULT_WINDOW_SIZE
        time_unit = DEFAULT_TIME_UNIT
        # Each customer was represented by the public ip.
        key = request.remote_addr
        
        rate_limiter = SlidingWindowLog(window_size, time_unit)
        result = rate_limiter.request(key)
        
        if result:
            return f(*args, **kwargs)
        else:
            raise Exception("Too much requests!")

    return decorated  
        
        