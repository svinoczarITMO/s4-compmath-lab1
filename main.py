#!/bin/python3

import math
import os
import random
import re
import sys


def interpolate_by_newton(x, y, x_target):
    n = len(x)
    arr = [[y[j]] for j in range(n)]
    for i in range(1, n):
        for j in range(n - i):
            if x[j + i] != x[j]:
                arr[j].append((arr[j + 1][i - 1] - arr[j][i - 1]) / (x[j + i] - x[j]))
            else:
                arr[j].append(arr[j][i - 1])

    result = arr[0][0]
    for i in range(1, n):
        c = 1
        for j in range(i):
            c *= (x_target - x[j])
        result += arr[0][i] * c

    return result


if __name__ == '__main__':
    axis_count = int(input().strip())

    x_axis = list(map(float, input().rstrip().split()))

    y_axis = list(map(float, input().rstrip().split()))

    x = float(input().strip())

    result = interpolate_by_newton(x_axis, y_axis, x)

    print(str(result) + '\n')