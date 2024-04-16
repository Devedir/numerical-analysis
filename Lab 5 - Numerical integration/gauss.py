from math import pi


def f(x: float) -> float:
    return 1 / (1 + x*x)


weights = [
    (-0.96029, 0.101229),
    (-0.796667, 0.222381),
    (-0.525532, 0.313707),
    (-0.183435, 0.362684),
    (0.183435, 0.362684),
    (0.525532, 0.313707),
    (0.796667, 0.222381),
    (0.96029, 0.101229)
]

sum = 0.0
for x, w in weights:
    sum += w * f(x)

print(f'Quadrature result: {sum}\tError: {abs(pi/2 - sum)}')
