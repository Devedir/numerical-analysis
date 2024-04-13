#include <stdio.h>
#include <math.h>

// pointer to function of one variable
typedef double (* FuncFp)(double);

double fun(double x) {
    return 1. / (x + 1.);
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

// trapezoidal rule
double quad_trap(FuncFp f, double a, double b, int n) {
    double h = (b - a) / n;
    double sum = 0;
    double prev = f(a);
    for (double x = a + h; x < b + h; x += h) {
        double new = f(x);
        sum += prev + new;
        prev = new;
    }
    return sum * h / 2;
}

// Simpson's rule
double quad_simpson(FuncFp f, double a, double b, int n) {
    double h = (b - a) / n;
    double sum = f(a) + 4 * f((a + a + h) / 2);
    for (double x = a + h; x < b; x += h)
        sum += 2 * f(x) + 4 * f((x + x + h) / 2);
    sum += f(b);
    return sum * h / 6;
}

int main() {
    const int N_array[] = {1, 3, 5};
    const QuadratureFp quad_array[] = {quad_rect_mid, quad_trap, quad_simpson};
    const char* names[] = {"Rectangle", "Trapezoidal", "Simpson's"};

    const double correct = log(2);

    for (int i = 0; i < 3; i++) {
        printf("%s rule:\n", names[i]);
        for (int n = 0; n < 3; n++) {
            double S = quad_array[i](fun, 0, 1, N_array[n]);
            printf("n = %d: S = %.10f, Error = %.10f\n", N_array[n], S, fabs(correct - S));
        }
        printf("\n");
    }

    return 0;
}
