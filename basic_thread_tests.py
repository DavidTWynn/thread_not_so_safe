from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import sys

from functions_to_verify import Adder


class ThreadSafeCheck:
    def __init__(self, runs, num_threads):
        self.runs = runs
        self.num_threads = num_threads

    def check_threaded_adder(self):
        for _ in range(self.runs):
            result = self._run_threaded_add()
            expected = self.num_threads * Adder.iterations
            if result != expected:
                print(f"Issue found: {result} but expected {expected}")

    def check_concurrent_thread_adder(self):
        for _ in range(self.runs):
            result = self._run_concurrent_thread_add()
            expected = self.num_threads * Adder.iterations
            if result != expected:
                print(
                    f"Concurrent issue found: {result} but expected {expected}"
                )

    def _run_threaded_add(self):
        adder = Adder()

        threads = []
        for _ in range(self.num_threads):
            thread = Thread(target=adder.increment)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        return adder.counter

    def _run_concurrent_thread_add(self):
        adder = Adder()

        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            results = []
            for _ in range(self.num_threads):
                results.append(executor.submit(adder.increment))

        return adder.counter


def main():
    # Display interpreter switch interval and Python version
    print(f"Interpreter switch interval: {sys.getswitchinterval()}")
    print(f"Python Version: {sys.version.split(' ')[0]}")

    # Run test multiple times and verify function end result
    runs = 3
    num_threads = 10

    executor = ThreadSafeCheck(runs, num_threads)
    # Uses threading module
    executor.check_threaded_adder()

    # Uses concurrent.futures.module
    executor.check_concurrent_thread_adder()


if __name__ == "__main__":
    main()
