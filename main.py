import numpy as np
import matplotlib.pyplot as plt

x = np.arange(- 0.52, 0.52, 0.01)
y = np.sin(1 / x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.show()
