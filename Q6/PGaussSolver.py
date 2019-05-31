import math

class PGaussSolver:
    # Constructor1
    def __init__(self, a, b, n, function):
        self._a = a
        self._b = b
        self._n = n
        self._func = function
        self.results = 0

    # Legendre Equation
    def legendre(self, n , x):
        if (n == 0):
            return 1
        elif (n == 1):
            return x
        else:
            return ((2.0 * n - 1) * x * self.legendre(n - 1, x) - (1.0 * n - 1) * self.legendre(n - 2, x)) / (n)

    # Legendre polynomial derivatives
    def dlegendre(self, n, x):
        return (1.0 * n/(x**2-1))*(x*self.legendre(n, x) - self.legendre(n-1, x))

    # Weight
    def weight(self, n, x):
        return 2 / ((1 - x ** 2) * (self.dlegendre(n, x) ** 2))

    # Legendre polynomial zeros
    def legendreZeroes(self, n, i):
        pi = 3.141592655
        xold1 = math.cos(pi * (i - 1/4) / (n + 1/2))
        iteration = 1
        xnew1 = xold1 - self.legendre(n, xold1) / self.dlegendre(n, xold1)
        while (1 + math.fabs(xnew1 - xold1) > 1.0):
            xold1 = xnew1
            xnew1 = xold1 - self.legendre(n, xold1) / self.dlegendre(n, xold1)
        return xnew1

    # The final equation
    def exec(self):
        integral = 0
        for i in range(1, self._n + 1):
            integral = integral + ( self._func(self.legendreZeroes(self._n, i)) * self.weight(self._n, self.legendreZeroes(self._n, i)) )
        self.results = ((self._b - self._a) / 2.0) * integral;

    def result(self):
        return self.results