class Adder:
    iterations = 10_000_000

    def __init__(self):
        self.counter = 0

    def increment(self):
        for _ in range(self.iterations):
            self.counter += 1
