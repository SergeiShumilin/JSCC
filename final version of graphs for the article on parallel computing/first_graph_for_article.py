"""Plot a number of function with filled gaps between.2

This code makes creating of multifunctional plot easier to depict.
It filling the gaps between multiple functions using a colormaps
defined in matplotlib

"""

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from numpy import *


def plot_a_function(q, k, color):
    """Plot the number of asymptotes and functions according to the q array.

    Plots the k-th function thicker then others.

    :param q: array of values for x axis
    :param k: the exact number of function which need to be plotted thicker then others
    :param color: desired color of functions

     """
    i = 0
    for c in q:
        ax.axvline(x=c, linestyle="dashed", dashes=(20, 8), linewidth=0.5, color=color)  # asymptote
        x = arange(0, c, 0.001)
        ax.plot(x, 1 + ((1 - 2 * c) / (c - x)), color=color, linewidth=1)  # function graph
        i += 1

        if i == k:
            ax.axvline(x=c, linestyle="dashed", dashes=(20, 8), linewidth=0.5, color='black')  # thicker asymptote
            ax.plot(x, 1 + ((1 - 2 * c) / (c - x)), color=color, linewidth=1.7)  # thicker function graph


def fill_areas():
    """Fill areas between graphs with different colors.

    Colors are selected by defining colormap from matplotlib set

    """
    for i in range(3, 7, 1):
        x1 = arange(0, q[i], 0.001)
        ax.fill_between(x1, 1 + ((1 - 2 * q[i]) / (q[i] - x1)), 0, facecolors=cm.Greens(40 + i * 30))
        x2 = arange(q[i], 0.51, 0.001)
        ax.fill_between(x2 - 0.001, 25, 0, facecolors=cm.Greens(40 + i * 30))
    for i in range(3, 0, -1):
        x3 = arange(-0.1, q[i] - 0.001, 0.001)
        ax.fill_between(x3, 25, 1 + ((1 - 2 * q[i]) / (q[i] - x3)), facecolors=cm.Reds(180 - i * 30))


def set_x_values(xax, locator, formatter_pattern):
    """Set the values for the x axis.

    :param xax: the desired axis
    :param locator: locator sets the multiplicity of x values
    :param formatter_pattern: the form of x values

    """
    major_locator = MultipleLocator(locator)
    major_formatter = FormatStrFormatter(formatter_pattern)
    xax.set_major_locator(major_locator)
    xax.set_major_formatter(major_formatter)


def set_tick_labels(xax, number_of_labels, size):
    """Set ticklabels of the given axis.

    For rendering of x labels the TEX syntax is used.

    :param xax: The axes for which the labels are set
    :param number_of_labels: the desired number of labels to put into
            labels array
    :param size: desired size of labels

    """
    labels = ['0', '0']
    for i in range(1, number_of_labels):
        labels.append(r'$\frac{{{}}}{{{}}}$'.format(i, 'v'))
    print(labels)
    xax.set_ticklabels(labels)
    for label in xax.get_ticklabels():
        label.set_fontsize(size)


def plot_text():
    """Plot the inscription for the graphs on the plot.

    """
    plt.text(0.035, 14.0, r'$k = 2$', size=15, rotation=73.)
    plt.text(0.11, 14.0, r'$k = 3$', size=15, rotation=73.)
    plt.text(0.18, 14.0, r'$k = 4$', size=15, rotation=73.)
    plt.text(0.255, 14.0, r'$k = 5$', size=15, rotation=75.)
    plt.text(0.33, 14.0, r'$k = 6$', size=15, rotation=80.)
    plt.text(0.40, 14.0, r'$k = 7$', size=15, rotation=80.)
    plt.text(0.44, 1.2, r'$k = 8$', size=15, rotation=0.)


def add_inscription():
    """Add inscriptions to graph: title, labels for x and y axes.

    """
    plt.title("Evaluation of vectorizing efficiency", fontsize=13)
    plt.xlabel(r'$p_2$', fontsize=15)
    plt.ylabel(r'$\frac{t_2}{t_1}$', labelpad=13, fontsize=20, rotation=0)

def plot_first_graph():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    xax = ax.xaxis  # get x axis
    plt.ylim(0, 25)
    plt.xlim(0, 0.5)
    # Лист значений параметра q
    q = arange(1 / 16, 1, 1 / 16)

    set_x_values(xax, 1 / 16, '%.3f')
    set_tick_labels(xax, 16, 14)
    plot_a_function(q, 4, 'black')
    plot_text()
    fill_areas()
    add_inscription()
    plt.show()
