# coding:utf-8
from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    # python中一切都是对象，名字只是一个符号
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    # 平方函数在x>0时，单调递增
    return max(a*a + b*b, a*a + c*c, b*b + c*c)

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    for i in range(1, n)[::-1]: # 从后向前找，第一个能整除的是最大因子
        if n % i == 0:
            return i

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

# 函数调用时，是将实参表达式计算结果的值赋值给形参，所以在执行with_if_function函数体内的语句之前
# 要进行的操作是：
# condition = c(), true_result = t(), false_result = f()

# if_statement 表达式在c()表达式为True时，会产生截断，f函数将不会被执行，with_if_statement只会执行
# t或者f中的一个，相比之下，在调用with_if_function时，t和f，c都会被执行

def c():
    "*** YOUR CODE HERE ***"
    return True

def t():
    "*** YOUR CODE HERE ***"
    return 1

def f():
    "*** YOUR CODE HERE ***"
    raise Exception()

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    steps = 1
    print(n)
    while n != 1:
        # n = n//2 if n%2 == 0 else 3*n+1 # 地板除
        n = if_function(n%2==0, n//2, 3*n+1)
        print(n)
        steps = steps + 1
    return steps
if __name__ == "__main__":
    print(hailstone(10))
    #print(a_plus_abs_b(1, 1))
    #print(a_plus_abs_b(1, -1))
    #print(largest_factor(80))
    #print(largest_factor(13))
    print(with_if_statement())
    print(with_if_function())
