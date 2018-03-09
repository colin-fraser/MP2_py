#!/usr/bin/env python
import sys
test = False

input_data = sys.stdin if not test else ["1\t2", "2\t3\t4", "3\t2\t4"]

for line in input_data:
    pages = line.split('\t')
    sys.stdout.write('%s\t0\n' % pages[0].strip())
    for p in pages[1:]:
        sys.stdout.write('%s\t1\n' % p.strip())
