class List:
    def __init__(self, size):
        if size <= 0:
            raise TypeError("size should be positive")
        self.size = size

    def add(self, value):
        raise NotImplementedError("method is not implemented")

    def remove(self):
        raise NotImplementedError("method is not implemented")

    def removeLeft(self):
        raise NotImplementedError("method is not implemented")

def test():
    print("TEST")