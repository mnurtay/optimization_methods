# Lab 4 - Week 4
# @Author: Nurtay Maksat
# Method Fibonacci

fibonacci = []
a = 0.5
b = 3.5
E = 0.5
N = 0


def find_n():
    global N
    checkValue = (b - a) / E
    while True:
        if (len(fibonacci) < 2):
            fibonacci.append(1)
            continue
        index = len(fibonacci)-1
        nextItem = fibonacci[index] + fibonacci[index-1]
        fibonacci.append(nextItem)
        if (nextItem >= checkValue):
            break
    N = (len(fibonacci) - 2) - 1


def f(x):
    return x + 2/x


def find_min(_n, _a, _b, _c, _d):
    if (_n == 0):
        return (_b + _a) / 2
    _fc = f(_c)
    _fd = f(_d)
    if _fc <= _fd:
        _c_next = _a + (_d - _a) * (fibonacci[_n-1] / fibonacci[_n+1])
        return find_min(_n-1, _a, _d, _c_next, _c)
    else:
        _d_next = _c + (_b - _c) * (fibonacci[_n-1] / fibonacci[_n+1])
        return find_min(_n-1, _c, _b, _d, _d_next)


find_n()
c = a + (b - a) * (fibonacci[N] / fibonacci[N+2])
d = a + (b - a) * (fibonacci[N+1] / fibonacci[N+2])
Xm = find_min(N, a, b, c, d)
print('Xm:\t', Xm)