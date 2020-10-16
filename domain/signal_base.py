import numpy as np

class SignalBase(object):
    def __init__(self, x, y, name="Signal"):
        self.x = x
        self.y = y
        self.name = name

    def mean(self):
        return [np.average(self.x), np.average(self.y)]

    def offset(self, scalar):
        self.y = self.y + scalar
        return self

    def scale(self, scalar):
        self.y = self.y * scalar
        return self

    def length(self):
        return len(self.x)
