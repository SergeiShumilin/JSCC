import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import *


def calculate_func(x, j):
    """Calculate the value of function

    Calculates the value of the function defined in return expression

    :param x: the function's argument
    :param j: the number of an element in array k

    """
    return ((1 - k[j] / v) - x) / (x * (k[j] - 1))


def plot_a_function(i, color):
    """Plot the number of asymptotes and functions according to the q array.

        Plots the k-th function thicker then others.

        :param i: the exact number of function which need
            to be plotted thicker then others
        :param color: desired color of functions

    """
    for j in range(0, len(k)):
        x = arange(0.00001, 0.5, 0.001)
        ax.plot(x, calculate_func(x, j), color=color, linewidth=1)
        if j == i:
            ax.plot(x, calculate_func(x, j), color=color, linewidth=1.7)


def fill_areas():
    """Fill areas between graphs with different colors.

        Colors are selected by defining colormap from matplotlib set

    """
    x = arange(0.00001, 0.51, 0.001)
    for i in range(0, 10, 1):
        ax.fill_between(x, ((1 - k[2 + i] / v) - x) / (x * (k[2 + i] - 1)), 0,
                        facecolor=cm.Greens(40 + i * 30))

    for i in range(2, 0, -1):
        ax.fill_between(x, ((1 - k[i] / v) - x) / (x * (k[i] - 1)), 25,
                        facecolors=cm.Reds(180 - i * 30))


def add_inscription():
    """Add inscriptions to graph: title, labels for x and y axes.

    """
    plt.title("Evaluation of vectorizing efficiency", fontsize=13)
    plt.xlabel(r'$p_2$', fontsize=15)
    plt.ylabel(r'$\frac{t_2}{t_1}$', labelpad=13, fontsize=20, rotation=0)


def plot_text():
    """Plot the inscription for the graphs on the plot.

    """
    plt.text(0.112, 6.48, r'$k = 2$', size=15, rotation=-45.)
    plt.text(0.07, 4.9, r'$k = 3$', size=15, rotation=-45.)


fig = plt.figure()
ax = fig.add_subplot(111)
xax = ax.xaxis
plt.ylim(0, 17.5) # limit the y-scale
plt.xlim(0, 0.5) # limit the x-scale
ax.grid(True) # add grid to the plot

k = arange(2, 17, 1)
v = 16

plot_a_function(2, 'black')
fill_areas()
plot_text()

plt.show()
