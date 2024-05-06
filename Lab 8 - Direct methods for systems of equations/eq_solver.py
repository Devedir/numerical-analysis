def main(n: int) -> (int, int, int):
    # generate A(n x n) matrix
    # generate b(n) vector
    # for each method:
    #     calculate result
    #     check for correctness
    #     measure time
    return 1, 2, 3  # measured times


if __name__ == '__main__':
    LU_time, inversion_time, QR_time = main(5)
    print('For equation size = 5:')
    print(f'{LU_time = }')
    print(f'{inversion_time = }')
    print(f'{QR_time = }')
