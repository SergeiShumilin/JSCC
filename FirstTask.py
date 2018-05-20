from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from numpy import *
import matplotlib.pyplot as plt
import seaborn

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
colors = ['#ccccff', '#b3b3ff', '#9999ff', '#8080ff', '#6666ff', '#4d4dff', '#3333ff',
          '#7070db', '#5c5cd6', '#2e2eb8', '#3333cc', '#2929a3', '#24248f', '#1f1f7a', '#0000ff']
colors2 = ['#ffad99', '#ff9980', '#ff8566', '#ff704d', '#ff5c33', '#ff471a', '#ff3300',
           '#e62e00', '#cc2900', '#b32400', '#991f00', '#801a00', '#661400', '#ff00ff', '#0000ff']


# Функция наносящая множество графиков функции на график
def plotAFunction(q):
    i = 0
    k = 0
    alpha = 0.2
    for c in q:
        ax.axvline(x=c, linestyle="dashed", dashes=(20, 8), linewidth=1, color=colors[i])  # ассимптота
        x = arange(0, c, 0.001)
        ax.plot(x, 1 + ((1 - 2 * c) / (c - x)), color=colors[i], linewidth=2)  # сам график
        k += 1
        if k == 4:
            ax.axvline(x=c, linestyle="dashed", dashes=(20, 8), linewidth=2, color=colors[i])
            ax.plot(x, 1 + ((1 - 2 * c) / (c - x)), color=colors[i], linewidth=4)  # сам график

            x = arange(0, 0.5, 0.001)
            ax.fill_between(x, 1 + ((1 - 2 * c) / (c - x)), 0, facecolors='green', alpha=alpha)
            x = arange(0.249, 0.5, 0.001)
            ax.fill_between(x, 25, 0, facecolors='green', alpha=alpha, label='using vectorization is beneficial')
            x = arange(-0.1, c - 0.001, 0.001)
            ax.fill_between(x, 25, 1 + ((1 - 2 * c) / (c - x)), facecolors='red', alpha=alpha,
                            label='using vectorization is not beneficial')

        # установить легенду
        ax.legend(loc='upper left')
        i += 1

    # Размеры графика
    plt.ylim(0, 25)
    plt.xlim(0, 0.45)


# текст
plt.text(0.17, 13.0, 'k = 4', size=15, rotation=73.)

# Тектовое и графическое оформление графика
plt.title("Graphic's name", fontsize=13)
plt.xlabel('X values', fontsize=11)
plt.ylabel('Y values', fontsize=11)
ax.set_facecolor('w')  ##f0f5f5

ax.yaxis.grid(True)

plotAFunction(q)
plt.show()

