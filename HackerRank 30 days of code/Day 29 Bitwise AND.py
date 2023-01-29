#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

def bitwiseAnd(N, K):
    # Write your code here
    my_set = [x + 1 for x in range (N)]
    maxi = 0
    for num in my_set[:len(my_set) - 2]:
        for other in my_set[num:]:
            result = num & other
            if result == K - 1:
                return result
            if (maxi < result) and (result < K):
                maxi = result
    return maxi
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()