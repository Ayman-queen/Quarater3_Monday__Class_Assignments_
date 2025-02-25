name :str = "GIAIC ..governor initiative for ai & cloud computing"
print("GIAIC stand for :", name)
# print("Hello World from ayman...")
# def giaic():
#     print("hello world from nasir")
# Python data types and special keywords

# 1. Integer (int) - Whole numbers
integer_num = 42
print(f"Integer: {integer_num}, Type: {type(integer_num)}")

# 2. Float (float) - Decimal numbers
float_num = 3.14159
print(f"Float: {float_num}, Type: {type(float_num)}")

# 3. String (str) - Text values
string_text = "Hello, Python!"
print(f"String: {string_text}, Type: {type(string_text)}")

# 4. Boolean (bool) - True or False values
bool_value = True
print(f"Boolean: {bool_value}, Type: {type(bool_value)}")

# 5. List (list) - Ordered, mutable collection
list_example = [10, 20, 30, "Apple"]
print(f"List: {list_example}, Type: {type(list_example)}")

# 6. Tuple (tuple) - Ordered, immutable collection
tuple_example = (5, 10, "Banana")
print(f"Tuple: {tuple_example}, Type: {type(tuple_example)}")

# 7. Dictionary (dict) - Key-value pairs
dict_example = {"name": "Nasir", "age": 22, "city": "Karachi"}
print(f"Dictionary: {dict_example}, Type: {type(dict_example)}")

# 8. Set (set) - Unordered collection of unique items
set_example = {1, 2, 3, 4, 4, 5}
print(f"Set: {set_example}, Type: {type(set_example)}")

# 9. NoneType (None) - Represents absence of a value
none_value = None
print(f"NoneType: {none_value}, Type: {type(none_value)}")

import keyword  
# 1. import
print("1. List of Python Keywords:", keyword.kwlist)

# 2. True, 3. False, 4. None
x = True
y = False
z = None
print(" x is:", x, ",  y is:", y, ",  z is:", z)

# 5. and, 6. or, 7. not
if x and not y:
    print(" x is True and  y is False (using 'and', 'not')")

# 8. is
if z is None:
    print(" z is None")

# 9. in
list_numbers = [1, 2, 3]
if 2 in list_numbers:
    print(" 2 is in list_numbers")

# 10. if, 11. elif, 12. else
num = 10
if num > 10:
    print(" Greater than 10")
elif num == 10:
    print(" Exactly 10")
else:
    print(" Less than 10")

# 13. for, 14. while, 15. break, 16. continue
for i in range(5):
    if i == 3:
        continue  # Skips 3
    print(f" for loop: {i}")
    if i == 4:
        break  # Stops loop

count = 0
while count < 2:
    print(f". while loop: {count}")
    count += 1

# 17. def, 18. return
def square(n):
    return n * n

print(". Function result:", square(4))

# 19. lambda
double = lambda x: x * 2
print(" Lambda function result:", double(5))

# 20. class
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f" Hello, my name is {self.name}")

p = Person("Nasir")
p.greet()

# 21. try, 22. except, 23. finally, 24. raise
try:
    print(" Trying to divide by zero...")
    print(10 / 0)
except ZeroDivisionError:
    print(" Cannot divide by zero!")
finally:
    print("Execution complete (finally)")

# raise ValueError("24. Custom error raised")

# 25. from, 26. as
from math import pi as circle_pi
print(" Imported pi as 'circle_pi':", circle_pi)

# 27. global, 28. nonlocal
global_var = 100

def outer():
    a = "outer"
    def inner():
        nonlocal a
        a = "inner"
        print(" Modified nonlocal variable:", a)
    inner()

outer()

# 29. pass
def some_function():
    pass  # Placeholder function

# 30. yield (generator function)
def generator():
    yield 1
    yield 2

g = generator()
print(" Yield function output:", list(g))

# 31. with (context manager)
with open("example.txt", "w") as f:
    f.write(" Testing with statement")

# 32. match, 33. case (Python 3.10+)
def check_status(code):
    match code:
        case 200:
            return " OK"
        case 404:
            return " Not Found"
        case _:
            return "Default"

print(check_status(200))

# 34. assert
x = 10
assert x > 5, " x should be greater than 5"

# 35. async, 36. await
import asyncio

async def async_function():
    await asyncio.sleep(1)
    print(" Async function executed")

asyncio.run(async_function())

# 37. del
del x
print(" x deleted")

# 38. NoneType (implicit keyword)
print(" NoneType is the type of None:", type(None))

# 39. __debug__ (Implicit debugging mode in Python)
if __debug__:
    print(" Debugging is enabled")