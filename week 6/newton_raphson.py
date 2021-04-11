# Lab 6
# @Author: Nurtay Maksat
# Method Newton-Raphson

import math

E = 0.2
x = 0.5


def f(x):
    return x + 2/x


def f_derivative(x):
    return 1 - 2/x**2


def f_2derivative(x):
    return 4 / x**3


def calculate():
    global x
    while True:
        f_x = f_derivative(x)
        if (abs(f_x) > E):
            f2_x = f_2derivative(x)
            x = x - f_x / f2_x
            continue
        return


calculate()
print('Xmin =', x)
