#!/bin/python3
from array import *
import math
import os
import random
import re
import sys

def sum(i,j):
    return (arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])

# Complete the hourglassSum function below.
def hourglassSum(arr):
    for i in range(0,4):
        for j in range(0,4):
            t=sum(i,j)
            max_sum.append(t)
    return max(max_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []
    max_sum = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
