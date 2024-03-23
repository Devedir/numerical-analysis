import math


def my_exp(x: int or float) -> float:
    if x < 0:
        return 1.0 / my_exp(-x)
    sum1 = 1.0
    sum2 = 1.0 + x
    denominator = 1
    while sum1 != sum2:
        sum1 = sum2
        denominator += 1
        sum2 += x ** denominator / math.factorial(denominator)
    return sum2


def test_exp(x: int or float):
    print(f'  my_exp({x}) = {my_exp(x)}')
    print(f'math.exp({x}) = {math.exp(x)}')
    print(f'absolute error = {abs(my_exp(x) - math.exp(x))}')
    print(f'relative error = {abs(my_exp(x) - math.exp(x)) / math.exp(x)}\n')


if __name__ == '__main__':
    test_exp(-10)
    test_exp(-5)
    test_exp(-1)
    test_exp(1)
    test_exp(5)
    test_exp(10)
