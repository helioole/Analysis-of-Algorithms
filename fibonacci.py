import matplotlib.pyplot as plt
from prettytable import PrettyTable
import numpy as np
import timeit
import decimal as d

# Recursive Method
def fib_rec(n):
    if n==0 or n==1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)

# DP Method
def fib_dyn(n):
    fib = [0, 1]
    if n==0 or n==1:
        return fib[n]
    else:
        for i in range(2, n + 1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]

# Iterative Method
def fib_iter(n):
    count = 0
    n1 = 0
    n2 = 1
    while count < n - 1:
        sum = n1 + n2
        n1 = n2
        n2 = sum
        count += 1
    return n2

# Matrix Power Method
def fib_mat(n):
    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)

    return F[0][0]

def multiply(F, M):
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(F, n):
    M = [[1, 1],
         [1, 0]]

    for i in range(2, n + 1):
        multiply(F, M)

# Binet's Formula Method
def binet(n):
    rnd = d.Context(prec=50, rounding="ROUND_HALF_EVEN")
    phi = d.Decimal((1 + d.Decimal(5 ** (1 / 2))))
    phi1 = d.Decimal((1 - d.Decimal(5 ** (1 / 2))))

    return int((rnd.power(phi, d.Decimal(n)) - rnd.power(phi1, d.Decimal(n))) / (2 ** n * d.Decimal(5 ** (1 / 2))))

# Fast Doubling Method
def fib_fast_doubling(n):
    if n == 0:
        return 0, 1
    else:
        a, b = fib_fast_doubling(n // 2)
        c = a * ((2 * b) - a)
        d = a * a + b * b
        if n % 2 == 0:
            return c, d
        else:
            return d, c + d

def fib(n):
    return fib_fast_doubling(n)[0]

# x and y axises of the plot
ns = [501, 631, 794, 1000,
1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
ts = [timeit.timeit('fib_dyn({})'.format(n),
                    globals=globals(),
                    number=1)
      for n in ns]
ts1 = [timeit.timeit('fib_iter({})'.format(n),
                    globals=globals(),
                    number=1)
      for n in ns]
ts2 = [timeit.timeit('fib_mat({})'.format(n),
                    globals=globals(),
                    number=1)
      for n in ns]
ts3 = [timeit.timeit('binet({})'.format(n),
                    globals=globals(),
                    number=1)
      for n in ns]
ts4 = [timeit.timeit('fib({})'.format(n),
                    globals=globals(),
                    number=1)
      for n in ns]

# Graph of 5 Methods
plt.plot(ns, ts, '-b', marker='o', label = 'Dynamic Programming Method')
plt.plot(ns, ts1, '-r', marker='o', label = 'Iterative Method')
plt.plot(ns, ts2, '-g', marker='o', label = 'Matrix Power Method')
plt.plot(ns, ts3, '-m', marker='o', label = 'Binet Formula Method')
plt.plot(ns, ts4, '-k', marker='o', label = 'Fast Doubling Method')
plt.title('Implementation of Algorithms')
plt.xlabel('n-th Fibonacci Term')
plt.ylabel('Execution Time(s)')
plt.legend()

plt.show()

# Results table
rts= np.round_(ts, decimals = 5)
x = PrettyTable()
x.title = "Implementation of Algorithms"
x.field_names = ["", 501, 631, 794, 1000,
1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
number = np.insert(rts, 0, 0)
rts1= np.round_(ts1, decimals = 5)
number1 = np.insert(rts1, 0, 1)
rts2= np.round_(ts2, decimals = 5)
number2 = np.insert(rts2, 0, 2)
rts3= np.round_(ts3, decimals = 5)
number3 = np.insert(rts3, 0, 3)
rts4= np.round_(ts4, decimals = 5)
number4 = np.insert(rts4, 0, 4)
x.add_row(number)
x.add_row(number1)
x.add_row(number2)
x.add_row(number3)
x.add_row(number4)
print(x)
