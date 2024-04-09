import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def findnormdensity (avg, stdev, x):
  return (1/(stdev*np.sqrt(2*np.pi)))*np.exp(-((x-avg)**2)/(2*stdev**2))

def plotnormdensity (avgs, diff, x_range):
  x_values=np.linspace(x_range[0], x_range[1], 1000)
  for avg, diff in zip(avgs, diff):
    y_values = [findnormdensity(avg, diff, x) for x in x_values]
    plt.plot(x_values, y_values, label = f'Mean: {avg}, Variance: {diff}')
  plt.legend()
  plt.show()

def integratenormdensity (avg, diff, a,b):
  integral = quad(findnormdensity, a, b, args=(avg, diff))
  return integral

plotnormdensity([0,5,12,14],[1,2,100,0.5],[-10,15,0.01,30])

avgheight = 171
diffheight = 7.12
stdevheight = np.sqrt(diffheight)

probability = integratenormdensity(avgheight, stdevheight, 162, 190)
print(f"Probability that a randomly selected man is between 162cm and 190cm in height: {probability:.4f}")

