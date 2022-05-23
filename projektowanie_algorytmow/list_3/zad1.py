from math import sqrt
res1 = 0
res2 = 0


def x1(i):
    global res1
    if i == 0:
        return 0
    res1 = 3**i + x1(i - 1)
    print(res1)
    return res1


def x2(i):
    global res1
    if i == -1 or i == 0:
        return 0
    else:
        res1 = i + x2(i - 2)
        print(res1)
        return res1


def x3(i):
    global res1
    if i == 1:
        return 1
    elif i == 0:
        return 0
    else:
        res1 = x3(i - 1) + x3(i - 2)
        print(res1)
        return res1 


def x1_1(n):
    global res2
    res2 = 3/2 * (pow(3, n) - 1)
    print(res2)
    return res2


def x2_1(n):
    global res2
    res2 = 1/8 * ((2*(n+1)*(n+2)) + pow(-1, n+1) + pow(-1, (2*n) + 1) * (2*n + 3))
    print(res2)
    return res2


def x3_1(n):
    global res2
    res2 = (pow((1 + sqrt(5)) / 2, n) - pow((1 - sqrt(5)) / 2, n)) / sqrt(5)
    print(res2)
    return res2


def verify(f1, f2, x):
    f1(x)
    f2(x)
    if f1(x) == f2(x):
        return True
    else:
        return (False, abs(f1(x) - f2(x)))


print(verify(x1, x1_1, 5))