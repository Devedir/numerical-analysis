from math import exp, sin, cos, fabs


def exact(x: float) -> float:
    return exp(-sin(x)) + sin(x) - 1.


def fun(x: float, y: float) -> float:
    return sin(x) * cos(x) - y * cos(x)


def runge_kutta(x_0, y_0, n, h, f):
    x = x_0
    y = y_0
    for _ in range(n):
        k1 = f(x, y)
        k2 = f(x + h/2, y + k1 * h/2)
        k3 = f(x + h/2, y + k2 * h/2)
        k4 = f(x + h,   y + k3 * h)
        y += (k1 + 2*k2 + 2*k3 + k4) * h/6
        x += h
    return y


def euler(x_0, y_0, n, h, f):
    x = x_0
    y = y_0
    for _ in range(n):
        y += h * f(x, y)
        x += h
    return y


if __name__ == '__main__':
    for k in range(1, 6):
        n = 10**k
        print(f'For {n = }:')
        rk_method = runge_kutta(0., 0., n, 1./ n, fun)
        e_method = euler(0., 0., n, 1./ n, fun)
        expect = exact(1.)
        print(f'    Expected value: {expect}')
        print(f'Runge-Kutta method: {rk_method}', end='\t\t')
        print(f'Difference: {fabs(rk_method - expect):.5e}')
        print(f"    Euler's method: {e_method}", end='\t\t')
        print(f'Difference: {fabs(e_method - expect):.5e}')
        print()
