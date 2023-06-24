from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    # TODO - you fill in here.
    s = ""
    sign = '+'
    
    if x == 0:
        return "0"

    if x < 0:
        sign = '-'
        x *= -1
    
    while x > 0:
        rem = x % 10
        x = x // 10
        s = chr(rem + ord('0')) + s
    return sign + s


def string_to_int(s: str) -> int:
    neg = 1
    index = 0
    num = 0
    if s.startswith('-'):
        neg = -1
        index = 1
    elif s.startswith('+'):
        index = 1

    for i in range(index,len(s)):
        if not s[i].isdigit():
            break
        num = num*10 + ord(s[i]) - ord('0')
    print(neg*num)
    return neg*num
        
    


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
