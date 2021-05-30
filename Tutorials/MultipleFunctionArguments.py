# Multiple Function Arguments

def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" % (first + second + third))

    if options.get("number") == "first":
        return first


result = bar(1, 2, 3, action="sum", number="first")
print("Result: %d" % (result))


# The * symbol is used to pass a variable number of arguments to a function. Typically, this syntax is
# used to avoid the code failing when we don’t know how many arguments will be sent to the function.
def foo(a, b, c, *extra):
    val = 0
    for i in extra:
        val += 1
    return val

# The ** symbol is used before an argument to pass a keyword argument dictionary to a function, this syntax
# used to successfully run the code when we don’t know how many keyword arguments will be sent to the function.


def bar(a, b, c, **extra):
    if extra.get("magicnumber") == 7:
        return True
    else:
        return False


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")
