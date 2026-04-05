import threading
import multiprocessing
import time
import math


# A CPU-bound task: calculating factorials
def cpu_bound_task(n=500000):
    _ = [math.factorial(i) for i in range(100)]


# An I/O-bound task: simulating a network request or sleep
def io_bound_task(seconds=1):
    time.sleep(seconds)


def run_test(func, mode, iterations=4):
    start = time.time()
    threads_or_procs = []

    for _ in range(iterations):
        if mode == "threading":
            t = threading.Thread(target=func)
        else:
            t = multiprocessing.Process(target=func)
        threads_or_procs.append(t)
        t.start()

    for t in threads_or_procs:
        t.join()

    return time.time() - start


# Benchmarking
cpu_thread_time = run_test(cpu_bound_task, "threading")
cpu_multiprocess_time = run_test(cpu_bound_task, "multiprocessing")

io_thread_time = run_test(io_bound_task, "threading")
io_multiprocess_time = run_test(io_bound_task, "multiprocessing")

print(f"{cpu_thread_time=}")
print(f"{cpu_multiprocess_time=}")
print(f"{io_thread_time=}")
print(f"{io_multiprocess_time=}")