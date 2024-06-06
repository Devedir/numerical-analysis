from random import uniform  # liczby quasi-losowe (rozkład jednostajny)
from math import sqrt, pi, fabs
from time import perf_counter
import matplotlib.pyplot as plt


def estimate_maximum(f, a, b):
    if a == 0:
        a = .0001
    cur = f(a)
    d = min((b - a) / 100, .5)
    x = a
    while x < b:
        cur = max(cur, f(x))
        x += d
    return cur * 1.1


def monte_carlo(f, a, b, n):
    counter = 0
    h = estimate_maximum(f, a, b)
    for _ in range(n):
        x = uniform(a, b)
        y = uniform(0, h)
        if y <= f(x):
            counter += 1
    return (b - a) * h * counter / n


def rect_integrate(f, a, b, h):
    if a == 0:
        a = .0001
    sum = 0
    x = a
    while x < b:
        sum += f(x)
        x += h
    return sum * h


x_0, x_n = 0, 1
funs = [
    (lambda x: x * x + x + 1, 11/6, 'x^2 + x + 1'),
    (lambda x: sqrt(1 - x * x), pi/4, 'sqrt(1 - x^2)'),
    (lambda x: 1 / sqrt(x), 2, '1 / sqrt(x)')
]


def ex2():
    for i, (fun, exact, rep) in enumerate(funs):
        print(f'f(x) = {rep}')
        for k in range(1, 7):
            N = 10 ** k
            result = monte_carlo(fun, x_0, x_n, N)
            print(f'for N = 10^{k}: {result:.4f}', end='\t')
            print(f'error = {fabs(exact - result):.4f}')
        print()


def ex3():
    for i, (fun, _, rep) in enumerate(funs):
        print(f'f(x) = {rep}')
        mc_times, rect_times = [], []
        for k in range(3, 7):
            N = 10**k
            time = perf_counter()
            mc_result = monte_carlo(fun, x_0, x_n, N)
            time = perf_counter() - time
            print(f'for N = 10^{k}:  {mc_result:.4f}', end='\t')
            print(f'time = {time:.5f} s')
            mc_times.append(time)
            time = perf_counter()
            rect_result = rect_integrate(fun, x_0, x_n, 1/N)
            time = perf_counter() - time
            print(f'for h = 10^-{k}: {rect_result:.4f}', end='\t')
            print(f'time = {time:.5f} s')
            rect_times.append(time)
        print()
        plt.plot(range(3, 7), mc_times, label='monte carlo')
        plt.plot(range(3, 7), rect_times, label='rectangle rule')
        plt.legend(loc='upper left')
        plt.title('Comparison of method times')
        plt.xlabel('precision [10^k]')
        plt.ylabel('time [s]')
        plt.show()


if __name__ == '__main__':
    # ex2()
    ex3()
