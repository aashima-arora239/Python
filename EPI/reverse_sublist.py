from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    
    dummy = curr = L
    prev = None
    idx = 1
    
    if L is None or start == finish:
        return L

    while idx < start:
        prev = curr
        curr = curr.next
        idx += 1
    
    first_half = prev
    end = curr
    
    prev_start = None
    while idx <= finish:
        #reversal logic
        temp = curr.next
        curr.next, prev_start = prev_start, curr
        curr = temp
        idx += 1
    #connect reversed
    if first_half:
        first_half.next = prev_start
    else:
        dummy = prev_start
    if end:
        end.next = curr
    
    return dummy
    
    
        
        
        
    

if __name__ == '__main__':
#     l = ListNode(1)
#     l.next = ListNode(2)
#     l.next.next = ListNode(3)
    
#     start = 1
#     finish = 2
#     ret = reverse_sublist(l,start,finish)
#     print(ret)
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
