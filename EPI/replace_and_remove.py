import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove_extra_space(size: int, s: List[str]) -> int:
    # TODO - you fill in here.
    new_size = size
    for index,char in enumerate(s):
        if char == 'a':
            s[index] = 'dd'
            new_size += 1
        if char == 'b':
            s[index] = ''
            new_size -= 1
    mutated = ''.join(s)
    for index,char in enumerate(mutated):
        s[index] = char
    return new_size

def replace_and_remove(size: int, s: List[str]) -> int:
    # TODO - you fill in here.
    write_idx, count = 0,0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
     
        if s[i] == 'a':
            count += 1
      
    
    read_idx = write_idx - 1
    write_idx += count - 1
    new_size = write_idx + 1
    while read_idx >= 0:
        if s[read_idx] == 'a':
            s[write_idx-1:write_idx+1] = 'dd'
            write_idx -= 2
        else:
            s[write_idx] = s[read_idx]
            write_idx -= 1
        read_idx -= 1
    return new_size

@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
