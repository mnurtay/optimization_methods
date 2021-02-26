# Nurtay Maksat
# MKM - 203M

a = 0.5
b = 3.5
E = 0.5
delta = 0.1
steps = 0


def f(x):
    return x + (2/x)


def check():
    return ((b-a-delta)/2**steps) + (delta/2)


def find(_a, _b):
    global steps
    steps += 1
    if (((_b - _a) / 2) < E):
        print('ERROR:', (_b - _a) / 2)
        print('Ei:', check())
        return (_b + _a) / 2

    _c = ((_a + _b) / 2) - (delta / 2)
    _d = ((_a + _b) / 2) + (delta / 2)

    if (f(_c) <= f(_d)):
        return find(_a, _d)
    else:
        return find(_c, _b)


xm = find(a, b)
print(xm)
