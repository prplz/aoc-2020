import time
from contextlib import contextmanager


@contextmanager
def timer(name):
    start = time.perf_counter_ns()
    try:
        yield
    finally:
        elapsed_ms = (time.perf_counter_ns() - start) / 1_000_000
        print(f'{name} took {elapsed_ms:.6g}ms')
