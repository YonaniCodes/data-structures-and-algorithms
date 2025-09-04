# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    t = arr[-1]
    added = False
    for i in range(n-2, -1, -1):
        if arr[i] > t:
            arr[i+1] = arr[i]
        else:
            arr[i+1] = t
            print(*arr)
            added = True
            break
        print(*arr)
    if not added:
        arr[0] = t
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
