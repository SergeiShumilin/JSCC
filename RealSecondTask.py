from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from numpy import *
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
xax = ax.xaxis

colorsGREEN = ['#ccffdd', '#b3ffcc', '#99ffbb', '#80ffaa', '#66ff99', '#4dff88', '#33ff77',
          '#1aff66', '#00ff55', '#00e64d', '#00cc44', '#00b33c', '#009933', '#00802b', '#006622']
colorsRED = ['#ffd6cc', '#ffc2b3', '#ffad99', '#ff9980', '#ff8566', '#ff704d', '#ff5c33',
          '#ff471a', '#ff3300', '#e62e00', '#cc2900', '#b32400', '#991f00', '#801a00', '#661400']

# классы Formatter и Locator применяются к каждому объекту label
# Locator располагает деления кратными к указанному числу
majorLocator = MultipleLocator(1 / 16)
majorFormatter = FormatStrFormatter('%.3f')
xax.set_major_locator(majorLocator)
xax.set_major_formatter(majorFormatter)

# Различные преобразования с массивом labels
for label in xax.get_ticklabels():
    label.set_fontsize(10)
# Лист значений параметра q
t = arange(2,17,1)
v = 16
g = 0
# Количество цветов в массиве должно равняться количеству итераций в plotAFunction
colors = ['#ccccff', '#b3b3ff', '#9999ff', '#8080ff', '#6666ff', '#4d4dff', '#3333ff',
          '#7070db', '#5c5cd6', '#2e2eb8', '#3333cc', '#2929a3', '#24248f', '#1f1f7a', '#0000ff']

def calculateFunc(x, j):
    return ((1-t[j]/v)-x)/(x*(t[j]-1))


# Функция наносящая множество графиков функции на график
def plotAFunction():
    j = 0
    alpha = 0.2
    for c in t:
        ax.axvline(x=c, linestyle="dashed", dashes=(20, 8), linewidth=0.5, color='black')  # ассимптота
        x = arange(0.00001, 0.5, 0.001)
        ax.plot(x, calculateFunc(x,j), color='black', linewidth=1)  # сам график
        j += 1
        if j == 2:
            ax.axvline(x=c, linestyle="dashed", dashes=(20, 8), linewidth=0.5, color='black')
            ax.plot(x, calculateFunc(x,j), color='black', linewidth=1.7)  # сам график

            """ax.fill_between(x, calculateFunc(x,j), 0, alpha=alpha,label="using vectorization is not beneficial for $k=4$",cmap="pink")
            ax.fill_between(x, calculateFunc(x,j), 25, facecolors=(0.1, 0.2, 0.5, 0.3), alpha=alpha,label='using vectorization is beneficial for $k=4$')"""
            ax.legend(loc='upper right')



x = arange(0.00001, 0.5, 0.001)

for i in range(0,10,1):
    ax.fill_between(x, ((1 - t[2+i] / v) - x) / (x * (t[2+i] - 1)), 0, facecolor=colorsGREEN[i])

ax.fill_between(x, ((1-t[2]/v)-x)/(x*(t[2]-1)), 25, facecolors=colorsRED[3])
ax.fill_between(x, ((1-t[1]/v)-x)/(x*(t[1]-1)), 25, facecolors=colorsRED[4])
ax.fill_between(x, ((1-t[0]/v)-x)/(x*(t[0]-1)), 25, facecolors=colorsRED[5])


 # Размеры графика
plt.ylim(0, 17.5)
plt.xlim(0, 0.5)

# Тектовое и графическое оформление графика
plt.title("Evaluation of vectorizing efficiency", fontsize=13)
plt.xlabel(r'$p_2$', fontsize=15)
plt.ylabel(r'$\frac{t_2}{t_1}$', fontsize=20, rotation=0)
ax.set_facecolor('w')  ##f0f5f5


ax.grid(True)
plt.text(0.112, 6.48, r'$k = 2$', size=15, rotation=-45.)
plt.text(0.07, 4.9, r'$k = 3$', size=15, rotation=-45.)

plotAFunction()
plt.show()