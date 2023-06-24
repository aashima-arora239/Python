import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates_slow(A: List[int]) -> int:
    start = 1
    i = 1
    length = len(A)
    while i < len(A):
        if A[i] != A[start - 1] and i == start:            
            i += 1
            start += 1
        else:
            while i < len(A) and A[i] == A[start - 1]:
                i += 1
            
            if i >= len(A):
                break
    
            A[start] = A[i]
            
            i += 1
            start += 1
    return start

def delete_duplicates(A: List[int]) -> int:
    write_index = 1
    
    for i in range(1,len(A)):
        if A[i] != A[write_index - 1]:
            A[write_index] = A[i]
            write_index += 1
    
    return write_index

@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    print('idx is', idx)
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
