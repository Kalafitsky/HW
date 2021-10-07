import time

def timeChecker(func):
    def main(*args, **kwargs):
        start_time = time.perf_counter_ns()
        func(*args, **kwargs)
        print(time.perf_counter_ns() - start_time)
    return main

@timeChecker
def investigated():
    print("sum is", 1323124+4234234)

investigated()