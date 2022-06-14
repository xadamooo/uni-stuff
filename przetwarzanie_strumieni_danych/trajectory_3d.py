import numpy as np


class Trajectory3D:
    def __init__(self, v, a, x=0):
        self.v = v
        self.a = a
        self.t = 0
        self.x0 = x
        self.N = 0
        self.x = 0
        self.dane = []

    def start_values(self, x, v, a, l):
        self.x0 = np.array(x).T
        self.v = np.array(v).T
        self.a = np.array(a).T
        self.dane = np.zeros(shape=(l, 3))
        while self.N < l:
            self.dane[self.N] = (self.x0 + self.v * self.t + (self.a * self.t**2)/2 + np.random.random() - 0.5)
            self.t += 1
            self.N += 1
        return self.dane, self.N

    def new_value(self):
        self.N += 1
        self.x = self.x0 + self.v * self.t + (self.a * self.t**2)/2 + np.random.random() - 0.5
        self.t += 1
        return self.x, self.N


