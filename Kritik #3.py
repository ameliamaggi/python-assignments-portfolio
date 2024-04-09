from sympy import symbols, solve
import math

def f(x):
  return math.sin(x)

E = 0.05
c = math.pi/4

def f_deriv(x):
  return (f(x+(10**-8))-f((10**-8)-x))/(2*(10**-8))

def L(x):
  return f(c) + f_deriv(c)*(x-c)

x=symbols('x')
Eq1 = f(x) - L(x) - E

sol = solve(Eq1)
print(sol)


