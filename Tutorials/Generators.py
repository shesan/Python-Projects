# Generators

import random


def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)


for random_number in lottery():
    print("And the next number is... %d!" % (random_number))

# fill in this function


def fib():
    a, b = 1, 1
    for i in range(100):
        yield a
        a, b = b, a + b


# testing code
counter = 0
for n in fib():
    print(n)
    counter += 1
    if counter == 10:
        break
