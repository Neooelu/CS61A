#higher level of abstraction.#
'''Generalization.'''

def identity(k):
    return k  

def cube(k):
    return pow(k, 3)



def summation(n, term):
    '''sum the first n terms of a sequence.

    >>> summation(5, cube)
    225
    >>> summation(5, identity)
    15
    '''
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total
