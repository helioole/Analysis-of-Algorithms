import math
import timeit
import matplotlib.pyplot as plt


def alg1(n):
    c = [True] * (n + 1)
    c[1] = False
    i = 2

    while i <= n:
        if c[i]:
            j = 2 * i
            while j <= n:
                c[j] = False
                j += i
        i += 1

    primes = []
    for k in range(2, n + 1):
        if c[k]:
            primes.append(k)

    return primes


def alg2(n):
    c = [True] * (n + 1)
    c[1] = False
    i = 2

    while i <= n:
        j = 2 * i
        while j <= n:
            c[j] = False
            j += i
        i += 1

    primes = []
    for k in range(2, n + 1):
        if c[k]:
            primes.append(k)

    return primes


def alg3(n):
    c = [True] * (n + 1)
    c[1] = False
    i = 2

    while i <= n:
        if c[i]:
            j = i + 1
            while j <= n:
                if j % i == 0:
                    c[j] = False
                j += 1
        i += 1

    primes = []
    for k in range(2, n + 1):
        if c[k]:
            primes.append(k)

    return primes


def alg4(n):
    c = [True] * (n + 1)
    c[1] = False
    i = 2

    while i <= n:
        j = 1
        while j < i:
            if i % j == 0 and j != 1:
                c[i] = False
            j += 1
        i += 1

    primes = []
    for k in range(2, n + 1):
        if c[k]:
            primes.append(k)

    return primes


def alg5(n):
    c = [True] * (n + 1)
    c[1] = False
    i = 2

    while i <= n:
        j = 2
        while j <= math.sqrt(i):
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1

    primes = []
    for k in range(2, n + 1):
        if c[k]:
            primes.append(k)

    return primes


sieves = [
    {
        "name": "Algorithm 1",
        "algo": lambda arr: alg1(arr),
        "color": "b"
    },
    {
        "name": "Algorithm 2",
        "algo": lambda arr: alg2(arr),
        "color": "r"
    },
    {
        "name": "Algorithm 3",
        "algo": lambda arr: alg3(arr),
        "color": "g"
    },
    {
        "name": "Algorithm 4",
        "algo": lambda arr: alg4(arr),
        "color": "y"
    },
    {
        "name": "Algorithm 5",
        "algo": lambda arr: alg5(arr),
        "color": "k"
    }
]
plt.title('Implementation of algorithms')
plt.xlabel('Prime numbers up to')
plt.ylabel('Execution Time(s)')

for algo in sieves:
    elements = list()
    elements1 = list()
    start_all = timeit.default_timer()
    for i in range(1, 100):
        start = timeit.default_timer()
        a = i*100
        algo["algo"](a)
        end = timeit.default_timer()
        elements.append(a)
        elements1.append(end - start)

    plt.plot(elements, elements1, label=algo["name"], color=algo["color"])

plt.legend()
plt.show()


