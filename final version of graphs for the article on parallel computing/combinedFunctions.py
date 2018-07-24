
from numpy import *
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.add_subplot(111)
xax = ax.xaxis
v = 16
t = arange(2,17,1)
q = arange(1 / 16, 1, 1 / 16)


def plotFirstGraph():
    q = arange(1 / 16, 1, 1 / 16)
    k = 0
    for c in q:
        ax.axvline(x=c, linestyle="dashed", dashes=(20, 8), linewidth=0.5, color='black')  # ассимптота
        x = arange(1/16, c, 0.001)
        ax.plot(x, 1 + ((1 - 2 * c) / (c - x)), color='black', linewidth=1)  # сам график
        k += 1

        if k == 4:
            ax.axvline(x=c, linestyle="dashed", dashes=(20, 8), linewidth=0.5, color='black')
            ax.plot(x, 1 + ((1 - 2 * c) / (c - x)), color='black', linewidth=1.7)  # сам график


def plotSecondGraph():
    j = 0
    for c in t:
        ax.axvline(x=c, linestyle="dashed", dashes=(20, 8), linewidth=0.5, color='black')  # ассимптота
        x = arange(0.00001, 1/16, 0.001)
        ax.plot(x, calculateFunc(x,j), color='black', linewidth=1)  # сам график
        j += 1
        if j == 2:
            ax.axvline(x=c, linestyle="dashed", dashes=(20, 8), linewidth=0.5, color='black')
            ax.plot(x, calculateFunc(x,j), color='black', linewidth=1.7)  # сам график


def calculateFunc(x, j):
    return ((1-t[j]/v)-x)/(x*(t[j]-1))



def fill_area(plot):
    q = arange(0, 1, 1 / 16)
    for i in range(1, 8, 1):
        x1 = arange(1/16, 1, 0.001)
        ax.fill_between(x1, 1 + ((1 - 2 * q[i]) / (q[i] - x1)), 0, facecolors=cm.Greens(40 + i * 30))
        ax.fill_between(x1, 1 + ((1 - 2 * q[i]) / (q[i] - x1)), 0, facecolors=cm.Greens(40 + i * 30))

def fill_square_areas():
    pass




plotFirstGraph()
plotSecondGraph()
fill_area(ax)






plt.ylim(0, 25)
plt.xlim(0, 0.5)
plt.show()