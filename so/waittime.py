import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statistics import NormalDist


def gaussian_pdf(x, m, v):
    return 1.0 / np.sqrt(2 * np.pi * v) * np.exp(-0.5 * (x - m) ** 2 / v)


df = pd.read_csv('./waittime.csv')
df_filtered = df[df['wtime'].between(550, 650, True)]

norm = NormalDist.from_samples(df_filtered['wtime'])
mean = norm.mean
stdev = norm.stdev
var = stdev * stdev
print("mean, standard deviation, variance:", mean, stdev, var)

pdf_x = np.arange(np.min(df_filtered['wtime']), np.max(df_filtered['wtime']), 2)

pdf_y = gaussian_pdf(pdf_x, mean, var)

plt.figure()
plt.plot([], [], ' ', label='mu=579.53, sigma=12.18')
plt.plot(pdf_x, pdf_y, 'k--', label='gaussian fit')
plt.hist(df_filtered[['wtime']], 50, color='c', label='batch wait-time histogram')
plt.xticks([560, 579.52, 600, 620, 640], ['560', 'mu=579.53', '600', '620', '640'])
plt.axvline(x=mean-stdev, ymax=0.28, color='k', alpha=0.6, linestyle='--')
plt.axvline(x=mean+stdev, ymax=0.28, color='k', alpha=0.6, linestyle='--')
plt.xlabel('batch wait time')
plt.ylabel('frequency')
plt.legend()
# plt.show()
plt.savefig('batch_wait_time.png', dpi=1000)

