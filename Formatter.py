import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import *

N = 10
x = np.arange(-N, N + 1, 1)
y = (np.random.random(len(x)) * 2. - 1) * N

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

# место для изменения формата
majorFormatter = FormatStrFormatter('%.0f')

ax.plot(x, y, )  # применяется сглаживание

xax = ax.xaxis;
xax.set_major_formatter(majorFormatter)
plt.show()
