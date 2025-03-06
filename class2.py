# Arithmetic Operators
# Performs basic mathematical operations
x = 10
y = 3
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)

# Assignment Operators
# Assigns values to variables
x = 5
x += 3  # Equivalent to x = x + 3
print("Assignment (+=):", x)
x -= 2  # Equivalent to x = x - 2
print("Assignment (-=):", x)
x *= 3  # Equivalent to x = x * 3
print("Assignment (*=):", x)
x /= 3  # Equivalent to x = x / 3
print("Assignment (/=):", x)
x %= 3  # Equivalent to x = x % 3
print("Assignment (%=):", x)
x //= 3  # Equivalent to x = x // 3
print("Assignment (//=):", x)
x **= 3  # Equivalent to x = x ** 3
print("Assignment (**=):", x)
x = 5  # Ensure x is an integer before using bitwise operators
x &= 3  # Equivalent to x = x & 3
print("Assignment (&=):", x)

x |= 3  # Equivalent to x = x | 3
print("Assignment (|=):", x)

x ^= 3  # Equivalent to x = x ^ 3
print("Assignment (^=):", x)

x >>= 3  # Equivalent to x = x >> 3
print("Assignment (>>=):", x)

x <<= 3  # Equivalent to x = x << 3
print("Assignment (<<=):", x)

walrus = (n := 10)  # Walrus operator assigns and returns a value
print("Assignment (:=):", n)


# Comparison Operators
# Compares two values
print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater Than:", x > y)
print("Less Than:", x < y)
print("Greater or Equal:", x >= y)
print("Less or Equal:", x <= y)

# Logical Operators
# Combines conditional statements
print("Logical AND:", (x > 2 and y < 5))
print("Logical OR:", (x > 5 or y < 5))
print("Logical NOT:", not(x > 5))

# Identity Operators
# Checks if two variables reference the same object
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("Identity (is):", a is b)  # True, because b references the same object as a
print("Identity (is not):", a is not c)  # True, because c is a different object(
# returns True because a is not the same object as c, even if they have the same content)

# Membership Operators
# Tests membership in sequences
print("Membership (in):", 2 in a)
print("Membership (not in):", 4 not in a)

# Bitwise Operators
# Performs bitwise operations on integers
x = 5  # 0101 in binary
y = 3  # 0011 in binary
print("Bitwise AND:", x & y)  # 0001 -> 1
print("Bitwise OR:", x | y)   # 0111 -> 7
print("Bitwise XOR:", x ^ y)  # 0110 -> 6
print("Bitwise NOT:", ~x)    # -(x+1) -> -6
print("Bitwise Left Shift:", x << 1)  # 1010 -> 10
print("Bitwise Right Shift:", x >> 1) # 0010 -> 2
