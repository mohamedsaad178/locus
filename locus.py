import cmath

import matplotlib.pyplot as plt
import sympy


def convert_roots(poles):
    roots = []
    for i in range(len(poles)):
        roots.append(poles[i][0] + cmath.sqrt(-1)*poles[i][1])
    return roots

def find_equation(my_roots):
    roots = convert_roots(my_roots)
    from sympy import Symbol
    x = Symbol('x')
    whole = 1
    if len(roots) == 0:
        return 0
    for root in roots:
        whole *= (x-root)
    return whole.expand()

my_roots=[[-50,10],[-50,-10],[-25,0],[0,0]]
x1=[-50,-50,-25,0]
y1=[10,-10,0,0]
plt.plot(x1,y1,'x')
equation=find_equation(my_roots)
arr = []
x = []
y = []
for i in range(1000):
    arr.append(sympy.solve(equation, simplify=False, rational=False))
    equation+= 2500

for i in range(1000):
    for j in range(4):
        z = complex(arr[i][j])
        real_part = z.real
        imag_part = z.imag
        x.append(real_part)
        y.append(imag_part)
plt.plot(x, y, 'o')
plt.show()