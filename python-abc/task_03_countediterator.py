class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        value = next(self.iterator)
        self.counter += 1
        return value

    def get_count(self):
        return self.counter

    def __iter__(self):
        return self
