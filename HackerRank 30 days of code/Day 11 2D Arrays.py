#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    arr_of_hours = []
    dict_of_hour_glass = {}
    for i in range(4):
        for j in range(4):
            arr_of_hours.extend(arr[i][j:j + 3])
            arr_of_hours.append(arr[i + 1][j + 1])
            arr_of_hours.extend(arr[i + 2][j:j + 3])
            dict_of_hour_glass[sum(arr_of_hours)] = arr_of_hours

            arr_of_hours = []
        
        
    print(max(dict_of_hour_glass.keys()))