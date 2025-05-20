#1.2 Elements of Programming

#1.2.1 Expressions
#primitive expressions.(numbers,Expressions representing numbers may be 
# combined with mathematical operators to form a compound expression, 
# which the interpreter will evaluate)
print(-1 - -1)
#0

#1.2.2 Call Expressions
#A call expression applies a function to some arguments

#1.2.3 Importing Library Functions
from math import sqrt
a=sqrt(4)
print(a)
#1.2.4 Names and the Environment
#In Python, names are often called variable names or variables 
# because they can be bound to different values in the course of executing a program. 
# When a name is bound to a new value through assignment, it is no longer bound to any previous value. 
# One can even bind built-in names to new values.
f = max
f(1,2,3)
#3
max = 5
max
#5
#max(1,2,3)
#error
##用funciton可以实时的调用初始的值
#1.2.5 Eluating Nested Ecpressions

#1.2.6 The Non-Pure Print Function

#Pure functions. Functions have some input (their arguments) and 
# return some output (the result of applying them). The built-in function
print(abs(-2))
#the function abs is pure.
# Pure functions have the property that applying them has no effects beyond returning a value. 
# Moreover, a pure function must always return the same value when called twice with the same arguments.

#non-pure function have some side effect beyond returning a value.

#1.3 Defining New Funcions
import 
def square(x):
    return mul(x,x)
#squirruled.（隐藏起来） not exercise until being called
#signature of function is important, it tell us how to build up the frame when we call the "squre"

x = 10
print(square(x))

#looking up nmaes in environments.

#1. an Environment is a sequence of frames. A frame is binding btws names and v alues,
#  one of the boxes in the enviroment diagram.
#2. A name, when evalueted, evaluates to the value bound to that name in the earliest frame
# of the current environment in which that name is found
 
# Assignment Statements
