import numpy as np
from timeit import default_timer as timer
from numpy.fft import rfft, irfft
from timeit import default_timer as timer
from matplotlib import pyplot as plt


def fft(x):
    if len(x) == 2:
        return np.array([x[0] + x[1], x[0] - x[1]], dtype=np.complex128)
    even = fft(x[::2])
    odd = fft(x[1::2])
    w = np.exp(-2 * np.pi * 1j * np.arange(len(x) // 2) / len(x))
    X = np.hstack((even + w * odd, even - w * odd))
    return X


def naive_multiply(A, B):
    start = timer()
    m = len(A)
    n = len(B)
    prod = [0] * (m + n - 1)
    for i in range(m):
        for j in range(n):
            prod[i + j] += A[i] * B[j]
            end = timer()
    return prod, end-start


def fft_multiply(arr_a, arr_b):
    start = timer()
    L = len(arr_a) + len(arr_b)
    a_f = rfft(arr_a, L)
    b_f = rfft(arr_b, L)
    end = timer()
    return irfft(a_f * b_f)[:-1], end-start


A = []
B = []
T1 = []
T2 = []
for i in range(100):
    A.append(np.random.randint(1, 10))
    B.append(np.random.randint(1, 10))
    res1, time1 = naive_multiply(A, B)
    res2, time2 = fft_multiply(A, B)
    T1.append(time1)
    T2.append(time2)
    #print(res1, res2)
    #print(time1, time2)

plt.plot(T1, color='r', label='naive multiplication')
plt.plot(T2, color='g', label='ifft multiplication')
plt.legend()
plt.show()

