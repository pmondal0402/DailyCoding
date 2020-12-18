import numpy as np

import math

def solution(N):
    # write your code in Python 3.6
    # Convert N to binary and store in list 
    # Save each each character in an array
    bin_representation = [int(i) for i in list('{0:0b}'.format(N))]
    # print('bin is', bin_representation)
    dim = len(bin_representation)
    ind1 = [item for item in range(dim) if bin_representation[item] == 1]   
    # print('ind1', ind1)         
    dim2 = len(ind1)
    if dim2 <=1:
        # Returns 0 if there is only one 1. 
        return 0
    else:
        # print('dim2 is', dim2)
        diff1 = [ind1[it+1] - ind1[it]-1 for it in range(0, dim2-1)] 
        # print('diff1', diff1)
        return max(diff1)

print(solution(1041))
