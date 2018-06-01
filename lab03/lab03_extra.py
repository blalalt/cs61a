""" Optional problems for Lab 3 """

from lab03 import *

## Higher order functions

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    # orign = lambda x : x
    funcs = [f1, f2, f3]
    def func(ntimes):
        def res_func(x):
            res = x
            for i in range(ntimes):
                res = funcs[i%3](res)
            return res
        return res_func
    return func

## Lambda expressions

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: y*10 + x%10
    while x > 0:
        x, y = x//10, f()
    return y == n

## More recursion practice

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n * skip_mul(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def func(i, bound):
        if i > bound: return True
        return False if n%i==0 \
                else func(i+1, bound)

    from math import sqrt
    return func(3, int(sqrt(n)+1))

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
    def func(i):
        return even_term(i) if i%2==0 else odd_term(i)

    return sum(map(func, range(1, n+1)), 0)


def times(x):
    if x == 0: return 0
    elif x == 1: return 1
    else: return x * times(x-1)

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    from collections import Counter

    c = Counter(str(n))
    res = 0
    for index, i in enumerate(c.keys()):
        for j in list(c.keys())[index:]:
            if int(i) + int(j) == 10:
                if i == j:
                    res += times(c[i]-1)
                    #print("i={}, res={}".format(i, res))
                else:
                    res += c[i] * c[j]
                    #print("j={}, res={}".format(j, res))
    return res