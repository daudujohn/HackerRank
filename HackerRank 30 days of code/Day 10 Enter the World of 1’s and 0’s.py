#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    binary_input = bin(n)[2:]
    count = 0
    temp = 0
    
    for num in binary_input:
        if num == '1':
            count += 1
            if count > temp:
                temp = count
        else:
            count = 0
            continue
    print(temp) 