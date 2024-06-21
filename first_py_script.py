#!/usr/bin/env python3

import sys
import os
import shutil

directory = sys.argv[1]

with open(directory, 'r') as f:
    print(f.readlines())

print("Hello there I hope I have created a conflict to merge")
#Added more nonsese line here
#Adding nonsense that shouldn't be here. This should be used as a comment.


#Added comments here to test the rebase
def check_disk_full(disk, min_gb, min_percent):
    du=shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gb_free = du.free / 2**30
    if gb_free < min_gb or percent_free < min_percent:
        return True
    return False

def check_root_full1():
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def check_root_full2():
    return check_disk_full("/", 3, 20)

def main():
    checks = [(check_root_full1, "Root is partition is full using 2GB and 10%"), (check_root_full2, "Root is partition is full using 3GB and 20%")]
    for check, msg in checks:
        if check():
            print(msg)
            sys.exit(1)
    print("Everything is okay")
    sys.exit(0)

#Added a line into this code here git branch
# Added seconed line into this code here git branch
main()
