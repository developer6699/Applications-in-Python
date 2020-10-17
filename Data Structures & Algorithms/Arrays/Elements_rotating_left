# HackerSolution
# for question visit: https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    count = d
    while count!=0:
        temp = a[0]
        a.append(temp)
        a.pop(0)
        count -= 1
    print(*a)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    rotLeft(a, d)

