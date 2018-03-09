#!/usr/bin/env python
import sys
test = False

input_data = sys.stdin if not test else ["A 100", "C 98", "B 99", "E 96", "D 97", "G 90", "F 96"]

for line in input_data:
    sys.stdout.write(line + '\n')

