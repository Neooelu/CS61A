"""our first python source file。"""

from operator import floordiv, mod

def divide_exact(n,d=10):
    """ Retrun the quotient and remainder of dividing N by D.

    >>> q,r = divide_exact(2013,10)
    >>> q
    201
    >>> r
    2
    """
    return floordiv(n,d),mod(n,d)

def absolute_value(x):
    """Return the absolute value of x.
    """
    if x < 0 :
        return -x
    elif x == 0 :
        return 0
    else:
        return x
