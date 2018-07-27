"""Plot a number of function with filled gaps between.

This code makes creating of multifunctional plot easier to depict.
It's filling the gaps between multiple functions using a colormaps
defined in matplotlib.

How to use this module
=======================
1. Call `plot_second_graph` with a set of parameters (see the function for description)

For example: plot_second_graph(3, cm.Greens, cm.Reds)
"""

import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import *

def plot_second_graph(k, colormap1, colormap2):
    """
    Plot the number of graphs with color filling.

    :param k: the k value (makes the k-th graph thicker and separates the color of filling on the plot)
    :param colormap1: matplotlib colormap for the left side https://matplotlib.org/users/colormaps.html
    :param colormap2: colormap for the right side https://matplotlib.org/users/colormaps.html
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    xax = ax.xaxis
    plt.ylim(0, 17.5) # limit the y-scale
    plt.xlim(0, 0.5) # limit the x-scale
    ax.grid(True) # add grid to the plot

    k_array = arange(2, 17, 1)
    v = 16

    plot_a_function(ax,k, k_array, v, 'black')
    fill_areas(ax,k,k_array,v,colormap1,colormap2)
    plot_text()

    plt.show()


def calculate_func(k, v, x, j):
    """Calculate the value of function

    Calculates the value of the function defined in return expression

    :param x: the function's argument
    :param j: the number of an element in array k

    """
    return ((1 - k[j] / v) - x) / (x * (k[j] - 1))


def plot_a_function(ax, i, k_array, v, color):
    """Plot the number of asymptotes and functions according to the q array.

        Plots the i-th function thicker then others.

        :param i: the exact number of function which need
            to be plotted thicker then others
        :param color: desired color of functions

    """
    for j in range(0, len(k_array)):
        x = arange(0.00001, 0.5, 0.001)
        ax.plot(x, calculate_func(k_array, v, x, j), color=color, linewidth=1)
        if j == i-2:
            ax.plot(x, calculate_func(k_array, v,x, j), color=color, linewidth=1.7)


def fill_areas(ax,k,k_array, v, colormap1,colormap2):
    """Fill areas between graphs with different colors.

        Colors are selected by defining colormap from matplotlib set

    """
    x = arange(0.00001, 0.51, 0.001)
    for i in range(0, 10, 1):
        ax.fill_between(x, ((1 - k_array[2 + i] / v) - x) / (x * (k_array[2 + i] - 1)), 0,
                        facecolor=colormap1(40 + i * 30))

    for i in range(k-2, -1, -1):
        ax.fill_between(x, ((1 - k_array[i] / v) - x) / (x * (k_array[i] - 1)), 25,
                        facecolors=colormap2(120 + i*30))


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

