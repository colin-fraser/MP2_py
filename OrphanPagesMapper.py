#!/usr/bin/env python
import sys
test = False

input_data = sys.stdin if not test else ["1: 2", "2: 3 4", "3: 2 4"]

for line in input_data:
    head, body = line.split(':')
    sys.stdout.write('%s\t0\n' % head.strip())
    pages = body.split(' ')
    for p in pages[1:]:
        sys.stdout.write('%s\t1\n' % p.strip())
