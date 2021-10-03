# 1.1
def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    else:
        return m + multiply(m, n - 1)

# 1.2
# Drawn

# 1.3
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.
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
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return hailstone(n // 2) + 1
    else:
        return hailstone(n * 3 + 1) + 1

# 1.4
def merge(n1, n2):
    """ Merges two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    else:
        new_n1, last_of_n1 = n1 // 10, n1 % 10
        new_n2, last_of_n2 = n2 // 10, n2 % 10
        if last_of_n1 > last_of_n2:
            return merge(n1, new_n2) * 10 + last_of_n2
        else:
            return merge(new_n1, n2) * 10 + last_of_n1

# 1.5
def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    >>> incr_2 = make_func_repeater(lambda x: x + 2, 3)
    >>> incr_2(2) #same as f(f(x))
    8
    >>> incr_2(5)
    11
    """
    # I understood that function applies x times the function to y lol
    # def repeat(y):
    #     if x == 1:
    #         return f(y) 
    #     else:
    #         return f(make_func_repeater(f, x-1)(y))
    # return repeat

    # correct solution: Apply f to x ... y times
    def repeat(y):
        if y == 0:
            return x
        else:
            return f(repeat(y - 1))
    return repeat

# 1.6
def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    # lol, the disc03.pdf has the function prime_helper outside the is_prime

    def prime_helper(i):
        if n == i:
            return True
        elif n % i == 0 or n == 1:
            return False
        else:
            return prime_helper(i + 1)
        
    return prime_helper(2)