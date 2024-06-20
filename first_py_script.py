#!/usr/bin/env python3

import sys

directory = sys.argv[1]

with open(directory, 'r') as f:
    print(f.readlines())

print("Hello there I hope I have created a conflict to merge")
#Added more nonsese line here
#Adding nonsense that shouldn't be here. This should be used as a comment.

