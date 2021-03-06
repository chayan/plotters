import math

import numpy as np
import matplotlib.pyplot as plt

p = np.arange(0, 1, 0.005)
n = 5

ps = np.power(1 - np.power(1-np.power(p, n), n), n)
pp = 1 - np.power(1 - np.power(p, n), math.pow(n, 2))

fig, ax = plt.subplots()
ax.plot(p, ps)
ax.plot(p, pp, '.')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.show()
