#PartialFunctions

from functools import partial

def multiply(x,y):
        return x * y

# create a new function that multiplies by 2
dbl = partial(multiply,2)
print(dbl(4))

def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function to get 60
#The partial gets shifted to the left, so the new "1" value goes at the end of the function.
x = partial(func, 10, 5, 2)
print(x(1))