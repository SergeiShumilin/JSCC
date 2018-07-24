from numpy import *
import matplotlib.pyplot as plt
from matplotlib import cm


def plot_third_graph():
    fig = plt.figure()
    subplot = fig.add_subplot(111)
    q = arange(1 / 16, 1, 1 / 16)

    plot_asympthotes(subplot,q)
    plot_first_graph(subplot,q)
    plot_second_graph(subplot)
 #   fill_area(subplot)
  #  fill_third_graph(subplot)
    fill_the_gap_between(subplot)

    plt.ylim(0, 25)
    plt.xlim(0, 0.5)
    plt.show()




def plot_asympthotes(plot,x_values):
    for x in x_values:
        plot.axvline(x=x, linestyle="dashed", dashes=(20, 8), linewidth=0.5, color='black')  # ассимптота


def plot_first_graph(plot,q_values):
    k = 0
    for q in q_values:
        x = arange(1/16, q, 0.001)
        plot.plot(x, 1 + ((1 - 2 * q) / (q - x)), color='black', linewidth=1)  # сам график
        k += 1
        if k == 4:
            plot.axvline(x=q, linestyle="dashed", dashes=(20, 8), linewidth=0.5, color='black')
            plot.plot(x, 1 + ((1 - 2 * q) / (q - x)), color='black', linewidth=1.7)  # сам график


def plot_second_graph(plot):
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
        if j == 4:
            plot.axvline(x=c, linestyle="dashed", dashes=(20, 8), linewidth=0.5, color='black')
            plot.plot(x, calculateFunc(x,j), color='black', linewidth=1.7)


def calculateFunc(x, j):
    return ((1-j/16)-x)/(x*(j-1))

def fill_area(subplot):
    q = arange(1/16, 1, 1 / 16)
    for i in range(1, 8, 1):
        x1 = arange(1/16, 1, 0.001)
        subplot.fill_between(x1, 1 + ((1 - 2 * q[i]) / (q[i] - x1)), 0, facecolors=cm.Greens(40 + i * 30))
        x1 = arange(q[i],1, 0.001)
        subplot.fill_between(x1,25, 0, facecolors=cm.Greens(40 + i * 30))

def fill_third_graph(subplot):
    j=0
    for i in range(1, 8, 1):
        t = arange(2, 17, 1)
        x = arange(0.00001, 1 / 16, 0.001)
        subplot.fill_between(x, calculateFunc(x, t[j]), 0, facecolors=cm.Greens(40 + i * 30))
        j+=1

def fill_the_gap_between(subplot):
    x = arange(0, 0.125, 0.001)
    y1 =  1 + ((1 - 2 * 2/16) / (2/16 - x))
    y2=    calculateFunc(x, 2)
    subplot.fill_between(x,y2, y1,where=(y2>y1)&(y1>y2), facecolors=cm.Greens(40))



plot_third_graph()