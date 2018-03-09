#!/usr/bin/env python
import sys
test = False

counts = dict()
input_data = sys.stdin if not test else ["1\t0\n", "2\t1\n", "2\t0\n", "3\t1\n", "4\t1\n", "3\t0\n", "2\t1\n","4\t1\n",
                                         "5\t0\n"]

# input comes from STDIN
for line in input_data:
    key, value = line.split('\t')
    value = int(value.strip())
    if key in counts:
        counts[key] += value
    else:
        counts[key] = value

orphans = [k for k, v in counts.items() if v == 0]
for o in sorted(orphans):
    sys.stdout.write(o + '\n')