import math
import random

n_vals = [10 * 10**i for i in range(7)]

n = 3

# buckets = [0, 1/3), [1/3, 2/3), [2/3, 3/3]

for n in n_vals:
    buckets = [0] * n
    for i in range(n):
        rand_number = random.random()
        bucket = math.floor(rand_number * n)
        buckets[bucket] += 1

    empty_buckets = 0
    for hit in buckets:
        if hit == 0:
            empty_buckets += 1

    if empty_buckets == 0:
        print('no empty buckets')
    else:
        estimate = n / empty_buckets
        print('estimate of e for {} is {}. error %{}'.format(n, estimate, math.fabs(math.e - estimate)/math.e))