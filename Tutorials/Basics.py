# https://www.learnpython.org/en/Welcome
"""
print("Hello")

x = 1
if x == 1:
    print("x == 1")
"""

#########################################
#Variables and Types
#########################################
"""
myint = 7
print(myint)

myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

a, b = 3, 4
print(a,b)
"""

# This will not work!
"""
one = 1
two = 2
hello = "hello"

print(one + two + hello)
"""

#########################################
# Lists
#########################################
"""
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for num in mylist:
    print(num)

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("Hello")
strings.append("World")
second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
"""

#########################################
# Basic Operators
#########################################


#########################################
# String Formatting
#########################################
name = "John"
age = 23
print("%s is %d years old." % (name, age))

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)


#########################################
# Basic String Operations
#########################################
astring = "Hello world!"
print(astring[::-1])

#########################################
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
