import numpy as np
from matplotlib import pyplot
from scipy import interpolate


def runge(t) -> float:
    return 1 / (1 + 25 * t * t)


x = np.linspace(-1, 1, 1000)


def plot_for_n_knots(n: int):
    x_knots = np.linspace(-1, 1, n)
    y_knots = runge(x_knots)
    y = interpolate.krogh_interpolate(x_knots, y_knots, x)

    pyplot.title(f'Wykres dla {n} węzłów')
    pyplot.plot(x_knots, y_knots, 'o', label='węzły')
    pyplot.plot(x, y, label='interpolująca')
    pyplot.plot(x, runge(x), label='interpolowana')
    pyplot.legend()
    pyplot.show()


if __name__ == '__main__':
    for n in range(4, 13):
        plot_for_n_knots(n)
