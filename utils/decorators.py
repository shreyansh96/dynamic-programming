from functools import wraps
import time


def slow_it_down(_func=None, rate=1):
    """
    :param _func: can be used both as a decorator and function
    :param rate:  rate is the seconds to sleep after the function call
    """

    def decorator_slow_down(func):
        @wraps(func)
        def wrapper_slow_down(*args, **kwargs):
            resp = func(*args, **kwargs)
            time.sleep(rate)
            return resp

        return wrapper_slow_down

    if _func is None:
        return decorator_slow_down
    else:
        return decorator_slow_down(_func)


def time_this(logger=None):
    """
    decorator to time any method
    :param logger:
    :return:
    """

    def decorator(function):
        @wraps(function)
        def wrapper_timer(*args, **kwargs):
            start_time = time.time()
            resp = function(*args, **kwargs)
            end_time = time.time()
            if logger:
                logger.info("Time taken to execute: " + str(end_time - start_time))
            else:
                print("Time taken to execute: " + str(end_time - start_time))
            return resp

        return wrapper_timer

    return decorator
