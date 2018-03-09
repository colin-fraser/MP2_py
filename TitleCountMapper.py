#!/usr/bin/env python
import sys
import string

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]
test = False

# TODO
with open(stopWordsPath) as f:
    stop_words = [s.strip() for s in f.readlines()]

with open(delimitersPath) as f:
    delimiters = f.read()

input_data = sys.stdin if not test else ["Hello", "Hello, World (what is this)"]

for line in input_data:
  
    chunks = [line]
    for delimiter in delimiters:
        new_chunks = []
        for chunk in chunks:
            new_chunks += [c.lower().strip() for c in chunk.split(delimiter) if c]
        chunks = new_chunks

    for word in chunks:
        if word not in stop_words:
            sys.stdout.write("%s 1\n" % word)
