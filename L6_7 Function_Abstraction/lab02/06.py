#Short circuit of python
"""
Short-circuiting happens when the operator reaches an operand 
that allows them to make a conclusion about the expression. 
For example, and will short-circuit as soon as it reaches 
the first false value because it then knows 
that not all the values are true.

If and and or do not short-circuit, they just return the last value; 
another way to remember this is that and and or always return 
the last thing they evaluate, whether they short circuit or not. 
Keep in mind that and and or don't always return booleans 
when using values other than True and False.
"""
# A string is a true value. 
#0 is false. None is false. False is false

#Environment Diagrams with Lambda

def search(f):
    x = 0
    while not f(x):
        x += 1
    return x

def inverse(f):
    return lambda y: search(lambda x: f(x) == y)



# Zero-args

y = lambda: 2*x
x = 3
y()
x = 4
y()

# Dice

from random import randint

def six_sided():
    return randint(1, 6)

def eight_sided():
    return randint(1, 8)

def repeats(n, dice):
    "Return how many times a dice roll is the same as the previous one in n rolls."
    count = 0
    previous = None
    while n:
        outcome = dice()
        print(outcome)
        if previous == outcome:
            count += 1
        previous = outcome
        n -= 1
    return count

# Loops

def reprint(n):
    def a(word):
        k = n
        while k:
            print(word)
            k -= 1
    return a


# Lambdas

(lambda f: lambda x: f(f(x)))(lambda y: y * y)(3)

def twice(f):
    # g = lambda x: f(f(x))
    def g(x):
        return f(f(x))
    return g

square = lambda y: y * y

def square(y):
    return y * y



snap = lambda chat: lambda: snap(chat)
snap, chat = print, snap(2020)
chat()


chat()
