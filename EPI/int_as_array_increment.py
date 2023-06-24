from typing import List

from test_framework import generic_test


def plus_one_extra_mem(A: List[int]) -> List[int]:
    B = [0]*(len(A)+1)
    carry = 0
    for i in range(len(A) - 1, -1, -1):
        if i == len(A) - 1:
            result = A[i] + 1
        else:
            result = A[i] + carry
        
        if result > 9:
            B[i+1] = 0
            carry = 1
        else:
            B[i+1]=result
            carry = 0
    
    if carry > 0:
        B[0] = carry
    else:
        del B[0]
        
    return B

def plus_one(A: List[int]) -> List[int]:
    A[-1] += 1
    for i in range(len(A) - 1, 0, -1):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
