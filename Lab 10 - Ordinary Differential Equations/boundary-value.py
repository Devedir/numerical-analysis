from math import sin, cos, pi


def exact(x: float) -> float:
    return cos(x) - sin(x) + x


def fun(x: float, y: float) -> float:
    return x - y


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


if __name__ == '__main__':
    print(exact(pi/2))
