import matplotlib as matplotlib
import numpy

from numpy import *
import matplotlib.pyplot as plt
import matplotlib.cm as sm

q = arange(1 / 16, 1, 1 / 16)
x = arange(0, 1.5, 0.1)
y = 1 + ((1 - 2 * q) / (q - x))
colors = ['r', 'g', 'b', 'y', 'o', 'p', 'pink']


def plotAFunction(q, y):
    for c in q:
        plt.axvline(x=c, linestyle="dashed", linewidth=0.8)
        x = arange(0, c, 0.001)
        plt.plot(x, 1 + ((1 - 2 * c) / (c - x)))
        plt.ylim(0, 100)
        plt.xlim(0, 0.5)


plt.grid(True)
plotAFunction(q, y)
plt.show()
