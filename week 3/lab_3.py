# Nurtay Maksat
# MKM - 203M
# Golden section method

import math

a = 0.5
b = 3.5
E = 0.5
steps = 0


def calc_c(_a, _b):
    return ((3-math.sqrt(5))/2) * (_b - _a) + _a


def calc_d(_a, _b):
    return ((math.sqrt(5)-1)/2) * (_b - _a) + _a


def calc_Ei():
    return (1/2) * (b-a) * ((math.sqrt(5)-1)/2)**(steps-1)


def f(x):
    return x + 2/x


def find(_a, _b, _c=None, _d=None):
    global steps
    steps += 1
    _E = (_b - _a) / 2
    if (_E <= E):
        print('E\t=\t', _E)
        print('Ei\t=\t', calc_Ei())
        return (_a + _b) / 2
    if (_c == None or _d == None):
        _c = calc_c(_a, _b)
        _d = calc_d(_a, _b)
    if (f(_c) <= f(_d)):
        return find(_a, _d, calc_c(_a, _d), _c)
    else:
        return find(_c, _b, _d, calc_d(_c, _b))


Xm = find(a, b)
print('Xm\t=\t', Xm)
print('f(Xm)\t=\t', f(Xm))
