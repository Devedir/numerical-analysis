#include <stdio.h>
#include <math.h>

// pointer to function of one variable
typedef double (* FuncFp)(double);

double fun(double x) {
    return exp(-x*x) * cos(x);
}

// pointer to quadrature function
typedef double (* QuadratureFp)(FuncFp, double, double);

// rectangle rule, midpoint
double quad_rect_mid(FuncFp f, double h, double precision) {
    double sum = 0;
    double x = h / 2;
    double val = f(x);
    while (val >= precision) {
        sum += val;
        x += h;
        val = f(x);
    }
    return h * sum;
}

// trapezoidal rule
double quad_trap(FuncFp f, double h, double precision) {
    double sum = 0;
    double prev = f(0);
    for (double x = h; prev >= precision; x += h) {
        double new = f(x);
        sum += prev + new;
        prev = new;
    }
    return sum * h / 2;
}

// Simpson's rule
double quad_simpson(FuncFp f, double h, double precision) {
    double sum = f(0) + 4 * f(h / 2);
    double x = h;
    double val = 2 * f(x) + 4 * f((x + x + h) / 2);
    while (val >= precision) {
        sum += val;
        x += h;
        val = 2 * f(x) + 4 * f((x + x + h) / 2);
    }
    sum += f(x);
    return sum * h / 6;
}

int main() {
    const QuadratureFp quad_array[] = {quad_rect_mid, quad_trap, quad_simpson};
    const char* names[] = {"Rectangle", "Trapezoidal", "Simpson's"};

    const double correct = sqrt(M_PI) / sqrt(sqrt(M_E));

    const double H = 0.0001;
    const double precision = 0.0001;

    for (int i = 0; i < 3; i++) {
        printf("%s rule:\n", names[i]);
        double S = 2 * quad_array[i](fun, H, precision);
        printf("S = %.10f, Error = %.10f\n", S, fabs(correct - S));
    }

    return 0;
}
