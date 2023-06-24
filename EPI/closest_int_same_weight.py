from test_framework import generic_test
from swap_bits import swap_bits

def closest_int_same_bit_count(x: int) -> int:
    prev_bit = x & 1
    k = 0
    temp = x
    while x:
        bit = x & 1
        if bit == prev_bit:
            k += 1
        else: 
            break
        prev_bit = bit
        x >>= 1
    
        
    return swap_bits(temp,k,k-1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
