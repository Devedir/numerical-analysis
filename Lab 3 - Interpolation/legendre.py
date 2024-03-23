from numpy.polynomial.polynomial import Polynomial


p = [Polynomial([1]), Polynomial([0, 1])]
x = Polynomial([0, 1])  # x jako wielomian 0 + 1*x

for n in range(1, 6):
    p.append((2*n + 1)/(n+1) * x * p[n] - n/(n+1) * p[n-1])
    print(p[n+1])
