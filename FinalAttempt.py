from matplotlib.patches import Polygon
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from numpy import *
import matplotlib.pyplot as plt
random.seed(1977)

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
t = arange(2,17,1)
v = 16

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


            ax.legend(loc='upper right')


def plotImg():
    x1 = arange(0, 10, 0.01)
    x2 = arange(0, 10, 0.01)

    X = [x1, x2]
    X = [[.3, .6], [.4, .6],[.5, .6],[.6, .9]]
    v = 16
    im1 = ax.imshow(X, cmap='winter', origin='upper',
                    extent=[0, 1, 0, 20],alpha=1,zorder=0,interpolation='bicubic')

    im2 = ax.imshow(X, cmap='spring_r', origin='upper',
                    extent=[0, 1, 0, 20],alpha=1,zorder=1,interpolation='bicubic')

    plt.ylim(0, 17.5)
    plt.xlim(0, 0.51)
    x = arange(0.00001, 0.5, 0.001)

    ax.set_aspect('auto')

    array = [((1 - t[2] / v) - x) / (x * (t[2] - 1)) for x in x]
    xy = column_stack([x, array])
    clip_path = Polygon(xy, facecolor='none', edgecolor='none', closed=False)
    ax.add_patch(clip_path)
    im2.set_clip_path(clip_path)


plotImg()
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




