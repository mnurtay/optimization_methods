# Lab 6
# @Author: Nurtay Maksat
# Method Secand (секущих)

import math

E = 0.2
x0 = 1.2
x1 = 4.3
N = 0


def f(x):
    return math.cos(x) - x + 1


def calculate():
    global x0, x1, N
    while True:
        if (abs(x1 - x0) < E):
            return
        tempX = x1
        x1 = x1 - (x1-x0) * f(x1) / (f(x1)-f(x0))
        x0 = tempX
        N += 1


calculate()
print('x =', x1)
