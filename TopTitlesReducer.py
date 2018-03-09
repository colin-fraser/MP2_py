#!/usr/bin/env python
import sys
test = False
top_n = 10

input_data = sys.stdin if not test else ["A 100", "C 98", "B 99", "E 96", "D 97", "G 90", "F 96"]


lines = []
for line in input_data:
    word, count = line.split('\t')
    count = int(count)
    lines.append((count, word))

lines = sorted(lines)

for line in lines[-top_n:][::-1]:
    sys.stdout.write("%s\t%i\n" % (line[1], line[0]))

