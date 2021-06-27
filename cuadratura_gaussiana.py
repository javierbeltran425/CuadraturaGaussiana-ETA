import numpy as np
import matplotlib.pyplot as plt
from sympy import *


def gaussian_quadrature(fx, a, b, n):
    [roots, weights] = np.polynomial.legendre.leggauss(n)

    values = [
        wi * fx.subs({"x": ((b - a) / 2) * xi + ((a + b) / 2)}).evalf()
        for (xi, wi) in zip(roots, weights)
    ]

    return ((b - a) / 2) * sum(values)


print("Cuadratura Gaussiana: ")
s = input("Ingrese f(x) a integrar: ")
f = sympify(s)

a = int(input("Ingrese limite inferior (a): "))
b = int(input("Ingrese limite superior (b): "))
n = int(input("Ingrese el numero de nodos: "))

# Approximated area
res = gaussian_quadrature(f, a, b, n)
print('Resultado: {}'.format(res))

print('Renderizando grafica...')

# Gaussian Quadrature plot
[roots, _] = np.polynomial.legendre.leggauss(n)
gauss_xs = [((b - a) / 2) * xi + ((a + b) / 2) for xi in roots]
gauss_ys = [f.subs({'x': xi}).evalf() for xi in gauss_xs]

plt.plot(gauss_xs, gauss_ys, 'ro', label="Nodos de interpolación")
plt.plot(gauss_xs, gauss_ys, 'r--', label="Solución Númerica")

# Analytical plot
xs = np.arange(a, b, 0.2)
ys = [f.subs({'x': x}).evalf() for x in xs]

plt.plot(xs, ys, label="Solución analítica")
plt.title('f(x) = {}'.format(s))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()