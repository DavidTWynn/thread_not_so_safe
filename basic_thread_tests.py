from threading import Thread
import sys


class Adder:
    iterations = 10_000_000

    def __init__(self):
        self.counter = 0

    def increment(self):
        for _ in range(self.iterations):
            self.counter += 1


def run_threaded_add(num_threads):
    adder = Adder()

    threads = []
    for _ in range(num_threads):
        threads.append(Thread(target=adder.increment))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return adder.counter


def main():
    # Display interpreter switch interval and Python version
    print(f"Interpreter switch interval: {sys.getswitchinterval()}")
    print(f"Python Version: {sys.version.split(' ')[0]}")

    # Run test multiple times and verify function end result
    runs = 3
    num_threads = 10
    for _ in range(runs):
        result = run_threaded_add(num_threads)
        expected = num_threads * Adder.iterations
        if result != expected:
            print(f"Issue found: {result} but expected {expected}")


if __name__ == "__main__":
    main()
