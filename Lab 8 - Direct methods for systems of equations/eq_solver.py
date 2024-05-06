import numpy as np
import time


def main(n: int) -> (int, int, int):
    A = np.random.uniform(-10., 10., (n, n))
    A[A == 0] = 0.0001  # for Doolittle's method to work
    B = np.random.uniform(-10, 10, n)

    expected = np.linalg.solve(A, B)

    # for each method:
    #     calculate result
    #     check for correctness
    #     measure time

    # LU decomposition
    lu_time = time.time()

    L = np.eye(n, dtype=np.float64)
    U = np.zeros((n, n), dtype=np.float64)

    U[0, 0] = A[0, 0]
    for i in range(n):
        for j in range(i, n):
            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])
        for j in range(i+1, n):
            L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]

    z = np.linalg.solve(L, B)
    x = np.linalg.solve(U, z)

    lu_time = time.time() - lu_time

    if not np.allclose(x, expected):
        raise AssertionError("LU decomposition got it wrong!")

    # inversion
    inv_time = time.time()

    A_inv = np.linalg.inv(A)

    if not np.allclose(A.dot(A_inv), np.eye(n)) or not np.allclose(A_inv.dot(A), np.eye(n)):
        raise AssertionError("Matrix not invertible")

    x = np.dot(A_inv, B)

    inv_time = time.time() - inv_time

    if not np.allclose(x, expected):
        raise AssertionError("Inversion got it wrong!")

    # QR decomposition
    qr_time = time.time()

    qr_time = time.time() - qr_time

    if not np.allclose(x, expected):
        raise AssertionError("QR decomposition got it wrong!")

    return lu_time, inv_time, qr_time


if __name__ == '__main__':
    # TODO: argument user input
    LU_time, inversion_time, QR_time = main(4)
    print('For equation size = 5:')
    print(f'{LU_time = }')
    print(f'{inversion_time = }')
    print(f'{QR_time = }')
