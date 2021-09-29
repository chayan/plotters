import math
import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(-40, 50, 0.1)
#
# s1 = 1 / (1 + np.exp(-(x+10))) * (1 - np.heaviside(x-10, 0))
# s2 = 1 / (1 + np.exp(-0.5 * (x+10))) * (1 - np.heaviside(x-10, 1))
# s3 = 1 / (1 + np.exp(-0.3 * (x+10))) * (1 - np.heaviside(x-10, 1))
#
# s1 += (1 - 1 / (1 + np.exp(-(x-30)))) * np.heaviside(x-10, 1)
# s2 += (1 - 1 / (1 + np.exp(-0.5 * (x-30)))) * np.heaviside(x-10, 1)
# s3 += (1 - 1 / (1 + np.exp(-0.3 * (x-30)))) * np.heaviside(x-10, 1)
#
# fig, ax = plt.subplots()
# ax.plot(x, s1)
# ax.plot(x, s2)
# ax.plot(x, s3)
#
# # ax.plot(x, np.heaviside(x+10, 1))
#
# plt.legend(["c2 = 1", "c2 = 0.5", "c2 = 0.2"], loc="upper left")
# ax.axhline(y=0, color='k')
# ax.axvline(x=0, color='k')
# plt.grid()
# plt.show()


fig, ax = plt.subplots()

x = np.arange(400, 700, 0.1)
mu = 579.53
sigma = 12.18
h = np.heaviside(x-mu, 1)

ax.plot([], [], ' ', label='mu=579.53, sigma=12.18\n')
ax.plot(x, h, label='step function', color='b')

s1 = 1 / (1 + np.exp(-2*(x-mu)))
s2 = 1 / (1 + np.exp(-0.2*(x-mu)))

ax.plot(x, s1)
ax.plot(x, s2, label='sigmoid approximation \nX ~ N(mu, sigma)')
plt.xticks([540, mu-2*sigma, mu, mu+2*sigma, 630], ['540', 'mu-2*sigma', 'mu=579.53', 'mu+2*sigma', '630'])
ax.axhline(y=0, color='k', alpha=0.6, linewidth=1)
plt.xlabel('time')
plt.ylabel('effective demand')
plt.xlim([540, 630])
plt.ylim([-0.03, 1.05])
plt.legend(loc='best')
# plt.show()
plt.savefig('sigmoid_approximation_step.png', dpi=1000)
