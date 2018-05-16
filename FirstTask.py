from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from numpy import *
import matplotlib.pyplot as plt



fig = plt.figure()
ax = fig.add_subplot(111)
xax = ax.xaxis

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
q = arange(1 / 16, 1, 1 / 16)

# Количество цветов в массиве должно равняться количеству итераций в plotAFunction
colors = ['#ff0000', '#ffff00', '#00cc00', '#80ccff', '#ff6600', '#9999ff', '#00cc66',
          '#ff0000', '#ff0066', '#00cc00', '#0000ff', '#ff6600', '#9999ff', '#ff00ff', '#0000ff']


# Функция наносящая множество графиков функции на график
def plotAFunction(q):
    i = 0
    for c in q:
        ax.axvline(x=c, linestyle="dashed", dashes=(20, 8), linewidth=1, color=colors[i]) #ассимптота
        x = arange(0, c, 0.001)
        ax.plot(x, 1 + ((1 - 2 * c) / (c - x)), color=colors[i], linewidth=2) #сам график
        i += 1

    # Размеры графика
    plt.ylim(0, 25)
    plt.xlim(0, 0.5)


# Тектовое и графическое оформление графика
plt.title("Graphic's name", fontsize=13)
plt.xlabel('X values', fontsize=11)
plt.ylabel('Y values', fontsize=11)
ax.set_facecolor('w') ##f0f5f5
plt.grid(True)

plotAFunction(q)
plt.show()
