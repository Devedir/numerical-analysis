from random import uniform
from math import sqrt, pi, fabs


def estimate_maximum(f, a, b):
    if a == 0:
        a = .0001
    cur = f(a)
    d = min((b - a) / 100, .5)
    x = a
    while x <= b:
        cur = max(cur, f(x))
        x += d
    return cur


def monte_carlo(f, a, b, n):
    counter = 0
    h = estimate_maximum(f, a, b)
    for _ in range(n):
        x = uniform(a, b)
        y = uniform(0, h)
        if y <= f(x):
            counter += 1
    return (b - a) * h * counter / n


if __name__ == '__main__':
    x_0, x_n = 0, 1
    funs = [
        (lambda x: x * x + x + 1, 11/6, 'x^2 + x + 1'),
        (lambda x: sqrt(1 - x * x), pi/4, 'sqrt(1 - x^2)'),
        (lambda x: 1 / sqrt(x), 2, '1 / sqrt(x)')
    ]
    for i, (fun, exact, rep) in enumerate(funs):
        print(f'f(x) = {rep}')
        for k in range(1, 7):
            N = 10**k
            result = monte_carlo(fun, x_0, x_n, N)
            print(f'for N = 10^{k}: {result:.4f}', end='\t')
            print(f'error = {fabs(exact - result):.4f}')
        print()
