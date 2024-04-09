import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

# Gradient Descent
def grad_des (xi, yi, f, grad_f, a, repetitions):
  x, y = xi, yi
  for i in range (repetitions):
    dx, dy = grad_f(x, y)
    x -= a * dx
    y -= a * dy
  return x, y

# Function f1 and its Gradient
def f1(x, y) :
  return x**2 + y**2

def grad_f1(x, y) :
  return (2*x, 2ж)
  
# Function f2 and its Gradient
def f2(x, y) :
  return 1 - np.exp(-x**2 - (y - 2)**2) - 2 * np.exp(-x**2 - (y + 2) **2)

def grad_f2(x, y) :
  df_dx = 2*x*p.exp(-×**2 - (y - 2) **2) + 4*x*р.exp(-×**2 - (y + 2)**2)
  df_dy = 2* (y-2) *пр.exp(-×**2 - (y - 2) **2) + 4* (y+2)жр.exp(-x**2 - (y + 2) **2) 
  return df_dx, df_dy
  
# Plotting Function
def plot_function(f, x_range, y_range):
  X, Y = np.meshgrid(×_range, y_range)
  Z = f(X, Y)
  fig = plt. figure (figsize= (10, 7))
  ax = fig.add_subplot (111, projection='3d')
  ax.plot_surface(X, Y, Z, cmap='viridis')
  plt.show()
  
# define test Cases
test_cases = [
  {'func': f1, 'grad': grad_f1, 'x0': 0.1, 'y': 0.1, 'alpha': 0.1, 'iterations': 10}, 
  {'func': f1, 'grad': grad_f1, 'x0': -1, 'yO': 1, 'alpha': 0.01, 'iterations': 100},
  {'func': f2, 'grad': grad_f2, 'x0': 0, 'yo': 1, 'alpha': 0.01, 'iterations': 10000}, 
  {'func': f2, 'grad': grad_f2, 'x0': 0, 'yo': -1, 'alpha': 0.01, 'iterations': 10000}
]

# Applying Gradient Descent and Plotting
for test in test cases:
  final_x, final_y = gradient_descent (test ['×0'], test['y'], test ['func'], test ['grad'], test ['alpha'], test['iterations ']) 
  print ("Final point for function {test ['func'].__name, _} starting at ({test['×0']}, {test['y0'1}): ({final_x), {final_y})")

#Call ploting function
plot_function(f2, np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))