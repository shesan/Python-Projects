# Set

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

# Where A AND B match
print("intersection ", a.intersection(b))
print("intersection ", b.intersection(a))

# Where A XOR B
print("symmetric_difference ", a.symmetric_difference(b))
print("symmetric_difference ", b.symmetric_difference(a))

# Where A XOR or B XOR. Basically A - B
print("difference ", a.difference(b))
print("difference ", b.difference(a))

# Where A, B set
print("union ", a.union(b))
