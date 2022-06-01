# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from scipy.stats import skew, kurtosis, hmean, uniform, mode
import matplotlib.pyplot as plt
import math


a = uniform.rvs(size=20)
b = uniform.rvs(size=100)
c = np.linspace(uniform.ppf(0.01), uniform.ppf(0.99), 100)



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
       'r-', lw=5, alpha=0.6, label='uniform pdf')
ax1.hist(a, density=True, histtype='stepfilled', alpha=0.2)
plt.show()

fig2, ax2 = plt.subplots(1, 1)
ax2.plot(c, uniform.pdf(c),
       'r-', lw=5, alpha=0.6, label='uniform pdf')
ax2.hist(b, density=True, histtype='stepfilled', alpha=0.2)
plt.show()
