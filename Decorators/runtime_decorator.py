import time
import functools

def void_runtime_decorator(func):
    @functools.wraps(func)
    def inner_wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        run_time = end - start
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
    return inner_wrapper

def run_time_decorator(func):
    @functools.wraps(func)
    def inner_wrapper(*args, **kwargs):
        start = time.time()
        val = func(*args, **kwargs)
        end = time.time()
        run_time = end - start
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return val
    return inner_wrapper