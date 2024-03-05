#!/bin/python3

import math
import os
import random
import re
import sys


def interpolate_by_newton(x_axis, y_axis, x_target):
    n = len(x_axis)
    arr = [[y_axis[j]] for j in range(n)]
    for i in range(1, n):
        for j in range(n - i):
            if x_axis[j + i] != x_axis[j]:
                arr[j].append((arr[j + 1][i - 1] - arr[j][i - 1]) / (x_axis[j + i] - x_axis[j]))
            else:
                arr[j].append(arr[j][i - 1])

    result = arr[0][0]
    for i in range(1, n):
        c = 1
        for j in range(i):
            c *= (x_target - x_axis[j])
        result += arr[0][i] * c
        
    return result



def run_tests ():
    if round(interpolate_by_newton([0, 1, 2, 3, 4], [1, 2, 3, 4, 5], 2.5), 2) == 3.5: print("Test 1 passed")
    else: print("Test 1 failed")

    if round(interpolate_by_newton([0, 1, 2, 3, 4], [0, 1, 4, 9, 16], 2.5), 2) == 6.25: print("Test 2 passed")
    else: print("Test 2 failed")

    if round(interpolate_by_newton([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4], -2.5), 2) == 6.25: print("Test 3 passed")
    else: print("Test 3 failed")

    if round(interpolate_by_newton([0, 1, 2, 3, 4], [0, 1, 8, 27, 64], 2.5), 2) == 15.62: print("Test 4 passed")
    else: print("Test 4 failed")

    if round(interpolate_by_newton([200, 400, 600, 800, 1000], [5, 10, 15, 20, 25], 750), 2) == 18.75: print("Test 5 passed")
    else: print("Test 5 failed")




if __name__ == '__main__':
    # run_tests()
    
    axis_count = int(input().strip())

    x_axis = list(map(float, input().rstrip().split()))

    y_axis = list(map(float, input().rstrip().split()))

    x = float(input().strip())

    result = interpolate_by_newton(x_axis, y_axis, x)

    print(str(result) + '\n')