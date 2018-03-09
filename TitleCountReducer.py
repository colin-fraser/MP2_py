#!/usr/bin/env python
from operator import itemgetter
import sys
test = False


#TODO

input_data = sys.stdin if not test else ["hello 1", "hello 1", "world 1"]

out = dict()
for line in input_data:
    word, count = line.split(' ')
    count = int(count   )
    if word in out:
        out[word] += count
    else:
        out[word] = count

for word, count in out.items():
    sys.stdout.write("%s\t%i\n" % (word, count))

