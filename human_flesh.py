import math

N = [2, 3, 4]
flips = [10, 50, 100, 150]

for n in N:
    for f in flips:
        combined_probability = 0
        for k in range(f):
            combined_probability += math.pow(math.comb(f, k) * math.pow(2, -f),  n)

        print(n, f, combined_probability)


