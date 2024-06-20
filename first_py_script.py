#!/usr/bin/env python3

import os
import sys

directory = sys.argv[1]

with open(directory, 'r') as f:
    print(f.readlines())

