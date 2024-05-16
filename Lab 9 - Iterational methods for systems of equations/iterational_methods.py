import numpy as np


def generate_data(n: int):
    diag0 = np.full(n, 2.)
    diag0[0] = 1.
    diag0[n - 1] = 1.
    diag1 = np.fromfunction(lambda i: 1./(i + 2.), (n - 1,))
    D = np.diag(diag0)
    LU = np.diag(diag1, 1) + np.diag(diag1, -1)
    A = D + LU
    x = np.random.choice([-1., 0.], n)
    # avoiding all zeroes for the sake of safe division
    while not np.any(x):
        x = np.random.choice([-1., 0.], n)
    return A, x


def jakobi(A, b, precision: float, n: int):
    x_prev = np.zeros(n, float)
    D = np.diag(np.diag(A))
    D_inv = np.linalg.inv(D)
    LU = A - D
    b_norm = np.linalg.norm(b)
    iterations = 0
    while True:
        iterations += 1
        x = D_inv @ (b - LU @ x_prev)
        test1 = np.linalg.norm(x - x_prev)
        test2 = np.linalg.norm(A @ x - b) / b_norm
        x_prev = x
        if test1 < precision or test2 < precision:
            return x, iterations


def run(n: int):
    A, x_expected = generate_data(n)
    print(f'True generated x:\n{x_expected}')
    b = A @ x_expected
    print(f'{b = }')

    print('\nJacobi method:')
    precision = 0.01
    for i in range(2, 8, 2):
        x, iterations = jakobi(A, b, precision, n)
        print(f'Approximated x with precision = 10^(-{i}):\n{x}')
        print(f'in {iterations} iterations')
        precision /= 100.


def run2():
    A = np.array([
        [10, -1,  2, -3],
        [ 1, 10, -1,  2],
        [ 2,  3, 20, -1],
        [ 3,  2,  1, 20]
    ])
    b = np.array([0, 5, -10, 15])
    precision = 0.001
    for i in range(3, 6):
        x, iterations = jakobi(A, b, precision, len(b))
        print(f'Approximated x with precision = 10^(-{i}):\n{x}')
        print(f'in {iterations} iterations')
        precision /= 10.


if __name__ == '__main__':
    np.set_printoptions(suppress=True)
    run(5)
    #run2()
