import math

def f (x):
    return x**2

def f_deriv(x):
  return (f(x+(10**-8))-f((10**-8)-x))/(2*(10**-8))

def L(x):
  return f(c) + f_deriv(c)*(x-c)

start = 0
lrate = 2
c = 1
h = -1*lrate*f_deriv(c)
i = 0

for i in range (c, lrate*h):
  i+=1
  start += L(c+h)

