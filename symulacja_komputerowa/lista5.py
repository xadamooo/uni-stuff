import numpy as np
import time
import math


def generator(x0, a, b, m, n):
    x = np.zeros(n)
    y = np.zeros(n)
    x[0] = int(x0 % m)
    y[0] = int((x0 % m)/m)
    suma = 0
    for i in range(n-1):
        x[i + 1] = (suma + (a[i % 20] * x[i] + b)) % m
        y[i + 1] = x[i + 1] / m
        suma += x[i]
    y = np.delete(y, 0)
    return y


def f1(x):
    return math.exp(-1*(x**2)/2)


def company(price, cost, const_cost, quant):
    s = 0
    price = generator(seed1, a1, 3, 7000, 1) * 3
    for i in range(12):
        s = s + (price - cost) * quant[i]
        s = s - const_cost
    return s


def integral_monte_carlo(xp, xk, n, s, x):
    for i in range(len(x)):
        s = s + f1(x[i])
        dx = abs(xk-xp)
    s = (dx * s) / n
    return s


a1 = list(np.random.randint(low = 1, high = 100, size = 100))
seed1 = int(time.time() - np.random.rand())
x1 = generator(seed1, a1, 3, 7000, 100)

print(f'Calka oznaczona na przedziale [0,1] z funkcji e^-x^2/2 wynosi w przyblizeniu {integral_monte_carlo(0, 1, 1000, 0, x1)}')
print