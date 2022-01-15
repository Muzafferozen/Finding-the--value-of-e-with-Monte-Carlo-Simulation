import random
from numba import jit
import time


class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2 - self.t1


class FindEulerNumber:
    def __init__(self):
        self.x = 0
        self.y = 0

    def number_more_than_one(self, yy):
        (self.x, self.y) = self.number_more_than_one_static(yy)

    @staticmethod
    @jit(nopython=True, nogil=True)
    def number_more_than_one_static(yy):
        x = 0
        for i in range(yy):
            count = 0
            part = 0
            while count < 1:
                count += random.random()
                part += 1
            x += part

        return x, yy

    def euler_number_result(self):
        return self.x / self.y
