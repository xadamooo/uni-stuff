# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from scipy.stats import skew, kurtosis, median_abs_deviation, mode, norm, shapiro
import matplotlib.pyplot as plt



a = np.random.normal(loc=0, scale=1, size=20)
b = np.random.normal(loc=0, scale=1, size=100)
c = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 1000)



print('Rozklad normalny:\n')
print(f'Dla rozkladu normalnego:\nsrednia - {np.mean(c)}\nmediana - {np.median(c)}\nmoda - {mode(c)}\nodchylenie standardowe - {np.std(c)}')
print(f'wariancja - {np.var(c)}\nskosnosc - {skew(c)}\nkurtoza - {kurtosis(c)}\nsrednie odchylenie bezwzgledne - {median_abs_deviation(c, scale="normal")}\n')
print(f'Lista a:\n{a}')
print(f'Dla listy a:\nsrednia - {np.mean(a)}\nmediana - {np.median(a)}\nmoda - {mode(a)}\nodchylenie standardowe - {np.std(a)}')
print(f'wariancja - {np.var(a)}\nskosnosc - {skew(a)}\nkurtoza - {kurtosis(a)}\nsrednie odchylenie bezwzgledne - {median_abs_deviation(a, scale="normal")}\n')
print(f'Lista b:\n{b}')
print(f'Dla listy b:\nsrednia - {np.mean(b)}\nmediana - {np.median(b)}\nmoda - {mode(b)}\nodchylenie standardowe - {np.std(b)}')
print(f'wariancja - {np.var(b)}\nskosnosc - {skew(b)}\nkurtoza - {kurtosis(b)}\nsrednie odchylenie bezwzgledne - {median_abs_deviation(b, scale="normal")}')

fig1, ax1 = plt.subplots(1, 1)
ax1.plot(c, norm.pdf(c),
       'r-', lw=5, alpha=0.6, label='normal pdf')
ax1.hist(a, density=True, histtype='stepfilled', alpha=0.2)
plt.show()

fig2, ax2 = plt.subplots(1, 1)
ax2.plot(c, norm.pdf(c),
       'r-', lw=5, alpha=0.6, label='normal pdf')
ax2.hist(b, density=True, histtype='stepfilled', alpha=0.2)
plt.show()