import numpy as np
from scipy.stats import skew, kurtosis, hmean, mode, uniform
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


seed = int(time.time())
a1 = list(np.random.randint(low = 1, high = 1000, size = 20))
a2 = list(np.random.randint(low = 1, high = 1000, size = 100))
a = generator(seed, a1, 3, 999, 21)
b = generator(seed, a2, 6, 999, 101)
c = np.linspace(uniform.ppf(0.01), uniform.ppf(0.99), 100)
print(type(a))
'''
print('Rozklad rownomierny:')
print(f'Dla rozkladu rownomiernego:\nsrednia - {np.average(c)}\nmediana - {np.median(c)}\nmoda - {mode(c)}\nodchylenie standardowe - {np.std(c)}')
print(f'wariancja - {np.var(c)}\nskosnosc - {skew(c)}\nkurtoza - {kurtosis(c)}\nsrednia harmoniczna - {hmean(c)}\n')
print(f'Lista a:\n{a}')
print(f'Dla listy a:\nsrednia - {np.average(a)}\nmediana - {np.median(a)}\nmoda - {mode(a)}\nodchylenie standardowe - {np.std(a)}')
print(f'wariancja - {np.var(a)}\nskosnosc - {skew(a)}\nkurtoza - {kurtosis(a)}\nsrednia harmoniczna - {hmean(a)}\n')
print(f'Lista b:\n{b}')
print(f'Dla listy b:\nsrednia - {np.average(b)}\nmediana - {np.median(b)}\nmoda - {mode(b)}\nodchylenie standardowe - {np.std(b)}')
print(f'wariancja - {np.var(b)}\nskosnosc - {skew(b)}\nkurtoza - {kurtosis(b)}\nsrednia harmoniczna - {hmean(b)}')

fig1, ax1 = plt.subplots(1, 1)
ax1.plot(c, uniform.pdf(c),
       'r-', lw=5, alpha=1.0, label='uniform pdf')
ax1.hist(a, density=True, histtype='stepfilled', alpha=0.7, color = 'green')
plt.show()

fig2, ax2 = plt.subplots(1, 1)
ax2.plot(c, uniform.pdf(c),
       'r-', lw=5, alpha=1.0, label='uniform pdf')
ax2.hist(b, density=True, histtype='stepfilled', alpha=0.7, color = 'green')
plt.show()
'''