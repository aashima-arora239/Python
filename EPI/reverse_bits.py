from test_framework import generic_test

def rev(x):
    temp = x
    y = 0
    num = 15
    while num >= 0:
        bit = x & 1
        x = x >> 1
        y = y | (bit << num)
        num -= 1

    return y
    
def reverse_bits(x: int) -> int:
    mask = 0xFFFF
    num_bits = 16
    x1 = rev(x & mask)
    x2 = rev((x >> num_bits) & mask)
    x3 = rev((x >> (2 * num_bits)) & mask)
    x4 = rev((x >> (3 * num_bits)) & mask)

    ret =  (x1 << (3 * num_bits)) | \
           (x2 << (2 * num_bits)) | \
           (x3 << (1 * num_bits)) | \
            x4
    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
