from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import sys


class Adder:
    iterations = 10_000_000

    def __init__(self):
        self.counter = 0

    def increment(self, *args):
        for _ in range(self.iterations):
            self.counter += 1


def run_threaded_add(num_threads):
    adder = Adder()

    threads = []
    for _ in range(num_threads):
        thread = Thread(target=adder.increment)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return adder.counter


def run_concurrent_thread_add(num_threads):
    adder = Adder()

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = []
        for _ in range(num_threads):
            results.append(executor.submit(adder.increment))

    return adder.counter


def check_threaded_adder(runs, num_threads):
    for _ in range(runs):
        result = run_threaded_add(num_threads)
        expected = num_threads * Adder.iterations
        if result != expected:
            print(f"Issue found: {result} but expected {expected}")


def check_concurrent_thread_adder(runs, num_threads):
    for _ in range(runs):
        result = run_concurrent_thread_add(num_threads)
        expected = num_threads * Adder.iterations
        if result != expected:
            print(f"Concurrent issue found: {result} but expected {expected}")


def main():
    # Display interpreter switch interval and Python version
    print(f"Interpreter switch interval: {sys.getswitchinterval()}")
    print(f"Python Version: {sys.version.split(' ')[0]}")

    # Run test multiple times and verify function end result
    runs = 3
    num_threads = 10
    check_threaded_adder(runs, num_threads)

    # Run test multiple times and verify function end result
    check_concurrent_thread_adder(runs, num_threads)


if __name__ == "__main__":
    main()
