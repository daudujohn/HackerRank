#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    def swap(a, x, y):
        temp = a[y]
        a[y] = a[x]
        a[x] = temp
            
    numberOfSwaps = 0
    for i in range(len(a)):
        
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                swap(a, j, j + 1)
                numberOfSwaps += 1
            
        if numberOfSwaps == 0:
            break;  
            
    print(f'Array is sorted in {numberOfSwaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
            
            
            