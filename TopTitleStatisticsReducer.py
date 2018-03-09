#!/usr/bin/env python
import sys

test = False

total_sum = 0
maximum = 0
minimum = 10e10
n = 0
counts = list()
sq_err = 0

input_data = sys.stdin if not test else ["A\t100\n", "C\t98\n", "B\t99\n", "E\t96\n", "D\t97\n", "G\t90\n", "F\t96\n"]
for line in input_data:
    word, count = line.split('\t')
    count = int(count)

    total_sum += count
    if count > maximum:
        maximum = count
    if count < minimum:
        minimum = count
    n += 1
    counts.append(count)

mean = total_sum / n

sq_err = sum([(c - mean)**2 for c in counts])
var = sq_err / n

sys.stdout.write('Mean\t%i\n' % mean)
sys.stdout.write('Sum\t%i\n' % total_sum)
sys.stdout.write('Min\t%i\n' % minimum)
sys.stdout.write('Max\t%i\n' % maximum)
sys.stdout.write('Var\t%i' % var)