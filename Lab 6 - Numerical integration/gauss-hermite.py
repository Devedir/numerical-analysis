from math import sqrt, pi, cos, e


nodes = [
    -0.381186990207322, 0.381186990207322,
    -1.15719371244678, 1.15719371244678,
    -1.98165675669584, 1.98165675669584,
    1.98165675669584, 2.93063742025724
]


def hermite7(x):
    return 128 * (x**7) - 1344 * (x**5) + 3360 * (x**3) - 1680 * x


def w(i):
    return (80640 * sqrt(pi)) / (hermite7(nodes[i])**2)


S = 0
for k in range(8):
    S += w(k) * cos(nodes[k])

correct = sqrt(pi) / pow(e, 0.25)

print(f'{S = }, Error = {abs(correct - S)}')
