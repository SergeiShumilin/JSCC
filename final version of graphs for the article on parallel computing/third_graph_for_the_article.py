"""



https://matplotlib.org/users/colormaps.html

r'$k = 2$'
size=15, rotation=73.
"""

from numpy import *
import matplotlib.pyplot as plt
from matplotlib import cm
import first_graph_for_article



def plot_third_graph(highlight_the_curves,little_area_color,big_area_color,coords_and_text,title_size=15):

    fig = plt.figure()
    subplot = fig.add_subplot(111)
    q = arange(1 / 16, 1, 1 / 16)

    plot_asympthotes(subplot,q)

    plot_first_graph(subplot,q,highlight_the_curves)
    plot_second_graph(subplot,highlight_the_curves)

    set_tick_labels(subplot)

    fill_area(subplot,big_area_color)
    fill_third_graph(subplot,big_area_color)

    fill_the_gap_between(subplot,highlight_the_curves,little_area_color)

    set_axes_limits(0,0.5,0,25)

    plot_text(subplot,coords_and_text)

    add_inscription(title_size)

    plt.show()


def plot_asympthotes(plot,x_values):
    for x in x_values:
        plot.axvline(x=x, linestyle="dashed", dashes=(20, 8), linewidth=0.5, color='black')  # ассимптота


def plot_first_graph(plot,q_values,thicker_the_curve):
    k = 0
    for q in q_values:
        x = arange(1/16, q, 0.001)
        plot.plot(x, 1 + ((1 - 2 * q) / (q - x)), color='black', linewidth=1)  # сам график
        k += 1
        if k == thicker_the_curve:
            plot.axvline(x=q, linestyle="dashed", dashes=(20, 8), linewidth=0.5, color='black')
            plot.plot(x, 1 + ((1 - 2 * q) / (q - x)), color='black', linewidth=1.7)  # сам график


def plot_second_graph(plot,thicker_the_curve):
    """

    :type plot: matplotlib plot
    """
    t = arange(2, 17, 1)
    j = 0
    i=1
    for c in t:
        plot.axvline(x=c, linestyle="dashed", dashes=(20, 8), linewidth=0.5, color='black')  # ассимптота
        x = arange(0.00001, 1/16, 0.001)
        plot.plot(x, calculateFunc(x,t[j]), color='black', linewidth=1)

        j += 1
        if j == thicker_the_curve:
            plot.axvline(x=c, linestyle="dashed", dashes=(20, 8), linewidth=0.5, color='black')
            plot.plot(x, calculateFunc(x,j), color='black', linewidth=1.7)


def calculateFunc(x, j):
    return ((1-j/16)-x)/(x*(j-1))

def fill_area(subplot,colormap):
    q = arange(1/16, 1, 1 / 16)
    for i in range(1, 8, 1):
        x1 = arange(1/16, 1, 0.0001)
        subplot.fill_between(x1, 1 + ((1 - 2 * q[i]) / (q[i] - x1)), 0, facecolors=colormap(40 + i * 30))
        x1 = arange(q[i],1, 0.001)
        subplot.fill_between(x1-0.0001,25, 0, facecolors=colormap(40 + i * 30))

def fill_third_graph(subplot,colormap):
    j=0
    for i in range(1, 8, 1):
        t = arange(2, 17, 1)
        x = arange(0.00001, 1 / 16, 0.00001)
        subplot.fill_between(x, calculateFunc(x, t[j]), 0, facecolors=colormap(40 + i * 30))
        j+=1

def fill_the_gap_between(subplot,number_of_curve,colormap):
    x = arange(0, 0.0625, 0.000001)
    y2 = calculateFunc(x, number_of_curve)
    subplot.fill_between(x, y2, 25, facecolors=colormap, interpolate=True)

    x = arange(0.0625,number_of_curve/16 , 0.0001)
    y1 = 1 + ((1 - 2 * number_of_curve / 16) / (number_of_curve / 16 - x))
    subplot.fill_between(x, y1, 25, facecolors=colormap, interpolate=True)

def set_tick_labels(subplot):
    ax = subplot.xaxis
    first_graph_for_article.set_x_values(ax, 1 / 16, '%.3f')
    first_graph_for_article.set_tick_labels(ax,16,14)

def add_inscription(title_size):
    """Add inscriptions to graph: title, labels for x and y axes.

    """
    plt.title("Evaluation of vectorizing efficiency", fontsize=title_size)
    plt.xlabel(r'$p_2$', fontsize=15)
    plt.ylabel(r'$\frac{t_2}{t_1}$', labelpad=13, fontsize=20, rotation=0)

def set_axes_limits(x1,x2,y1,y2):
    plt.xlim(x1, x2)
    plt.ylim(y1, y2)



def plot_text(subplot, coords_and_texts):
    for text in coords_and_texts:
        subplot.text(text[0], text[1], text[2], size=text[3], rotation=text[4])


plot_third_graph(3, cm.Reds(150),cm.magma,[(0.1, 14.0, r'$k = 2$',15,73.)])