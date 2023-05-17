import timeit
from decimal import Decimal, getcontext
import decimal

import numpy as np
from matplotlib import pyplot as plt
from prettytable import PrettyTable


def bbp_algorithm(n):
    getcontext().prec = n + 10
    pi = Decimal(0)
    k = 0
    while k <= n:
        a = Decimal(1) / (16 ** k)
        b = Decimal(4) / (8 * k + 1)
        c = Decimal(2) / (8 * k + 4)
        d = Decimal(1) / (8 * k + 5)
        e = Decimal(1) / (8 * k + 6)
        pi += a * (b - c - d - e)
        k += 1
    pi = str(pi)
    return pi[n + 1]

def gauss_legendre_algorithm(n):
    getcontext().prec = n + 10

    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(1) / Decimal(4)
    p = Decimal(1)

    for _ in range(n):
        a_next = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2

    pi = (a + b) ** 2 / (4 * t)
    pi = str(pi)
    return pi[n + 1]

def chudnovsky(n):
    decimal.getcontext().prec = n + 10
    decimal.getcontext().Emax = 999999999

    C = 426880 * decimal.Decimal(10005).sqrt()
    M = decimal.Decimal(1)
    X = decimal.Decimal(1)
    L = decimal.Decimal(13591409)
    S = L

    for i in range(1, n + 10):
        M = decimal.Decimal(M * ((1728 * i * i * i) - (2592 * i * i) + (1104 * i) - 120) / (i * i * i))
        L = decimal.Decimal(545140134 + L)
        X = decimal.Decimal(-262537412640768000 * X)
        S += decimal.Decimal((M * L) / X)

    pi = C / S
    pi_str = str(pi)[n+1]

    return pi_str

inputs = [
    {
        "name": "Bailey–Borwein–Plouffe (BBP) Algorithm",
        "algo": lambda arr: bbp_algorithm(arr),
        "color": "b"
    },
    {
        "name": "Gauss-Legendre Algorithm",
        "algo": lambda arr: gauss_legendre_algorithm(arr),
        "color": "r"
    },
    {
        "name": "Chudnovsky Algorithm",
        "algo": lambda arr: chudnovsky(arr),
        "color": "y"
    }
]
plt.title('Algorithms that determine the Nth decimal digit of PI')
plt.xlabel('The Nth digit')
plt.ylabel('Execution Time(s)')

for algo in inputs:
    elements = list()
    elements1 = list()
    start_all = timeit.default_timer()
    for i in range(1, 11):
        start = timeit.default_timer()
        a = i*100
        algo["algo"](a)
        end = timeit.default_timer()
        elements.append(a)
        elements1.append(end - start)

    plt.plot(elements, elements1, label=algo["name"], color=algo["color"])

plt.legend()
plt.show()

ns = [i*100 for i in range(1, 11)]
ts = [timeit.timeit('bbp_algorithm({})'.format(n),
                    globals=globals(),
                    number=1)
      for n in ns]

ts1 = [timeit.timeit('gauss_legendre_algorithm({})'.format(n),
                    globals=globals(),
                    number=1)
      for n in ns]

ts2 = [timeit.timeit('chudnovsky({})'.format(n),
                    globals=globals(),
                    number=1)
      for n in ns]

x = PrettyTable()
x.title = "Execution Time Result Table"
x.field_names = [i*100 for i in range(1, 11)]
elements1_r = np.round(ts, 5)
x.add_row(elements1_r)
elements2_r = np.round(ts1, 5)
x.add_row(elements2_r)
elements3_r = np.round(ts2, 5)
x.add_row(elements3_r)
print(x)
