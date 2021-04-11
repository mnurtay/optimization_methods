# Lab 5 - Week 6
# @Author: Nurtay Maksat
# Method Parabola

import random
import math

E = 0.25
a = 1.2
b = 6.3
x1, x2, x3 = 0, 0, 0
Y = None
Y_PREV = None


def f(x):
    return 5 * math.sin(2*x) + x**2


def q(x):
    global x1, x2, x3
    a0 = f(x1)
    a1 = (f(x2)-a0) / (x2-x1)
    a2 = (f(x3)-a0-a1*(x3-x1)) / ((x3-x1)*(x3-x2))
    return a0 + a1*(x-x1) + a2*(x-x1)*(x-x2)


def q_derivative():
    global x1, x2, x3
    a0 = f(x1)
    a1 = (f(x2)-a0) / (x2-x1)
    a2 = (f(x3)-a0-a1*(x3-x1)) / ((x3-x1)*(x3-x2))
    return 1/2 * (x1 + x2 - a1/a2)


def calculate():
    global a, b, Y, Y_PREV
    global x1, x2, x3
    while True:
        # --- Step 1
        while True:
            x1 = random.uniform(a, b)
            x2 = random.uniform(x1, b)
            x3 = random.uniform(x2, b)
            f1 = f(x1)
            f2 = f(x2)
            f3 = f(x3)
            if (f1 >= f2 and f2 <= f3):
                break

        # --- Step 2
        Y_PREV = Y
        Y = q_derivative()

        # --- Step 3
        if Y_PREV != None:
            delta = abs(Y - Y_PREV)
            if delta <= E:
                return

        # --- Step 4
        print('f(x*): ', f(Y))

        # --- Step 5
        a = x1
        b = x3


print('-'*50)
calculate()
print('-'*50)
print('Xmin:   ', Y)
print('f(min): ', f(Y))
