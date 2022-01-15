import random

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
        x = 0
        for _ in range(yy):
            count = 0
            part = 0
            while count < 1:
                count += random.random()
                part += 1
            x += part

        self.y = yy
        self.x = x

    def euler_number_result(self):
        return self.x / self.y
