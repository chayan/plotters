import math
import random

n_vals = [10 * 10**i for i in range(7)]
for n in n_vals:
    exp = []
    for i in range(n):
        s = 0
        count = 0

        while True:
            count += 1
            s += random.random()
            if s >= 1:
                break
        exp.append(count)

    print(sum(exp)/n)

print(math.e)
