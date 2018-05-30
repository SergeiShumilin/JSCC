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

tL = ['0', r'$\frac{1}{v}$', r'$\frac{2}{v}$', r'$\frac{3}{v}$', r'$\frac{4}{v}$', r'$\frac{5}{v}$', r'$\frac{6}{v}$',
      r'$\frac{7}{v}$', r'$\frac{8}{v}$',
      r'$\frac{9}{v}$', r'$\frac{10}{v}$', r'$\frac{11}{v}$', r'$\frac{12}{v}$', r'$\frac{13}{v}$', r'$\frac{14}{v}$',
      r'$\frac{15}{v}$', r'$1']
xax.set_ticklabels(tL)
for label in xax.get_ticklabels():
    label.set_fontsize(14)
# Лист значений параметра q
q = arange(1 / 16, 1, 1 / 16)

# Количество цветов в массиве должно равняться количеству итераций в plotAFunction
colors = ['#ccccff', '#b3b3ff', '#9999ff', '#8080ff', '#6666ff', '#4d4dff', '#3333ff',
          '#7070db', '#5c5cd6', '#2e2eb8', '#3333cc', '#2929a3', '#24248f', '#1f1f7a', '#0000ff']


# Функция наносящая множество графиков функции на график
# noinspection PyPep8Naming
def plotAFunction(q):

    k = 0
    alpha = 0.2
    for c in q:
        ax.axvline(x=c, linestyle="dashed", dashes=(20, 8), linewidth=0.5, color='black')  # ассимптота
        x = arange(0, c, 0.001)
        ax.plot(x, 1 + ((1 - 2 * c) / (c - x)), color='black', linewidth=1)  # сам график
        k += 1
        if k == 4:
            ax.axvline(x=c, linestyle="dashed", dashes=(20, 8), linewidth=0.5, color='black')
            ax.plot(x, 1 + ((1 - 2 * c) / (c - x)), color='black', linewidth=1.7)  # сам график

            x = arange(0, 0.250, 0.001)
            ax.fill_between(x, 1 + ((1 - 2 * c) / (c - x)), 0, facecolors='green', alpha=alpha)
            x = arange(0.249, 0.5, 0.001)
            ax.fill_between(x, 25, 0, facecolors='green', alpha=alpha, label='using vectorization is beneficial for $k=4$')
            x = arange(-0.1, c - 0.001, 0.001)
            ax.fill_between(x, 25, 1 + ((1 - 2 * c) / (c - x)), facecolors='red', alpha=alpha,
                            label='using vectorization is not beneficial for $k=4$')
            # установить легенду
            ax.legend(loc='upper left')



    # Размеры графика
    plt.ylim(0, 25)
    plt.xlim(0, 0.5)


# текст на графике
plt.text(0.035, 14.0, r'$k = 2$', size=15, rotation=73.)
plt.text(0.11, 14.0, r'$k = 3$', size=15, rotation=73.)
plt.text(0.18, 14.0, r'$k = 4$', size=15, rotation=73.)
plt.text(0.255, 14.0, r'$k = 5$', size=15, rotation=75.)
plt.text(0.33, 14.0, r'$k = 6$', size=15, rotation=80.)
plt.text(0.40, 14.0, r'$k = 7$', size=15, rotation=80.)
plt.text(0.44, 1.2, r'$k = 8$', size=15, rotation=0.)




# Тектовое и графическое оформление графика
plt.title("Evaluation of vectorizing efficiency", fontsize=13)
plt.xlabel(r'$p_2$', fontsize=15)
plt.ylabel(r'$\frac{t_2}{t_1}$', fontsize=20, rotation=0)
ax.set_facecolor('w')  ##f0f5f5

ax.yaxis.grid(True)

plotAFunction(q)
plt.show()
