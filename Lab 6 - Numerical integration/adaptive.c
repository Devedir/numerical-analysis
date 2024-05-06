#include <stdio.h>
#include <math.h>

#define RECURS_LEVEL_MAX  10000

// pointer to function of one variable
typedef double (* FuncFp)(double);

double fun(double x) {
    return exp(-x*x) * cos(x);
}

// pointer to quadrature function
typedef double (* QuadratureFp)(FuncFp, double, double, int);

// rectangle rule, midpoint
double quad_rect_mid(FuncFp f, double a, double b, int n) {
    double h = (b - a) / n;
    double sum = 0;
    for (double x = a + (h / 2); x < b; x += h)
        sum += f(x);
    return h * sum;
}

// adaptive algorithm
double adaptive(FuncFp f, double a, double b, double S, double tolerance, QuadratureFp quad, int level) {
    double S1 = quad(f, a, (a + b) / 2, 1);
    double S2 = quad(f, (a + b) / 2, b, 1);
    if (fabs(S1 + S2 - S) <= tolerance)
        return S1 + S2;
    if (level == RECURS_LEVEL_MAX) // for safety
        return NAN;
    double result1 = adaptive(f, a, (a + b) / 2, S1, tolerance / 2, quad, level + 1);
    double result2 = adaptive(f, (a + b) / 2, b, S2, tolerance / 2, quad, level + 1);
    return result1 + result2;
}

// initialization for adaptive algorithm
double init_adaptive(FuncFp f, double a, double b, double tolerance, QuadratureFp quad) {
    double S = quad(f, a, b, 1);
    return adaptive(f, a, b, S, tolerance, quad, 1);
}

int main() {
    const double correct = sqrt(M_PI) / sqrt(sqrt(M_E));

    double S = 2 * init_adaptive(fun, 0, 10, 0.0001, quad_rect_mid);
    printf("Adaptive algorithm (tolerance = 0.0001):\n");
    printf("S = %.10f, Error = %.10f\n\n", S, fabs(correct - S));

    return 0;
}