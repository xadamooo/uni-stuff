import numpy as np
from scipy.stats import skew, kurtosis, median_abs_deviation, mode, norm
import matplotlib.pyplot as plt
import time


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


def box_muller(x1, x2):
    r = np.sqrt(-2 * np.log(x1))
    theta = 2 * np.pi * x2
    X = r * np.cos(theta)
    return X


def norm_generator(x1, x2):
    return box_muller(x1, x2)

'''parametry a:'''
a1 = list(np.random.randint(low = 1, high = 1000, size = 20))
a2 = list(np.random.randint(low = 1, high = 1000, size = 100))
a3 = list(np.random.randint(low = 1, high = 1000, size = 20))
a4 = list(np.random.randint(low = 1, high = 1000, size = 100))


seed1 = int(time.time() - np.random.rand())
seed2 = int(time.time() - np.random.rand())
seed3 = int(time.time() - np.random.rand())
seed4 = int(time.time() - np.random.rand())

x1 = generator(seed1, a1, 3, 7000, 21)
x2 = generator(seed2, a3, 4, 7000, 21)
x3 = generator(seed3, a2, 3, 7000, 101)
x4 = generator(seed4, a4, 4, 7000, 101)
a = norm_generator(x1, x2)
b = norm_generator(x3, x4)
c = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 1000)

print(f'Dla rozkladu normalnego:\nsrednia - {np.average(c)}\nmediana - {np.median(c)}\nmoda - {mode(c)}\nodchylenie standardowe - {np.std(c)}')
print(f'wariancja - {np.var(c)}\nskosnosc - {skew(c)}\nkurtoza - {kurtosis(c)}\nsrednie odchylenie bezwzgledne - {median_abs_deviation(c, scale="normal")}\n')
print(f'Lista a:\n{a}')
print(f'Dla listy a:\nsrednia - {np.average(a)}\nmediana - {np.median(a)}\nmoda - {mode(a)}\nodchylenie standardowe - {np.std(a)}')
print(f'wariancja - {np.var(a)}\nskosnosc - {skew(a)}\nkurtoza - {kurtosis(a)}\nsrednie odchylenie bezwzgledne - {median_abs_deviation(a, scale="normal")}\n')
print(f'Lista b:\n{b}')
print(f'Dla listy b:\nsrednia - {np.average(b)}\nmediana - {np.median(b)}\nmoda - {mode(b)}\nodchylenie standardowe - {np.std(b)}')
print(f'wariancja - {np.var(b)}\nskosnosc - {skew(b)}\nkurtoza - {kurtosis(b)}\nsrednie odchylenie bezwzgledne - {median_abs_deviation(b, scale="normal")}')

fig1, ax1 = plt.subplots(1, 1)
ax1.plot(c, norm.pdf(c),
       'r-', lw=5, alpha=1.0, label='normal pdf')
ax1.hist(a, density=True, histtype='stepfilled', alpha=0.7, color = 'green')
plt.show()

fig2, ax2 = plt.subplots(1, 1)
ax2.plot(c, norm.pdf(c),
       'r-', lw=5, alpha=1.0, label='normal pdf')
ax2.hist(b, density=True, histtype='stepfilled', alpha=0.7, color = 'green')
plt.show()
