# **🔹 Introduction to Python**  

Python is a **high-level, interpreted programming language** designed with an emphasis on readability and simplicity. It is widely used in fields such as **web development**, **data science**, **machine learning**, and **automation**. Python’s syntax is easy to understand, making it one of the most popular languages for beginners and experts alike.

---

# **🔹 Introduction to Python**  

Python is a **high-level, interpreted programming language** designed with an emphasis on readability and simplicity. It is widely used in fields such as **web development**, **data science**, **machine learning**, and **automation**. Python’s syntax is easy to understand, making it one of the most popular languages for beginners and experts alike.

---

## **🔹 Python Operators**  

Operators are special symbols in Python that perform operations on variables and values. Python provides several types of operators:

### **1️⃣ Arithmetic Operators**  
These operators perform mathematical operations:
- `+` (Addition): `x + y`
- `-` (Subtraction): `x - y`
- `*` (Multiplication): `x * y`
- `/` (Division): `x / y`
- `//` (Floor Division): `x // y`
- `%` (Modulus): `x % y`
- `**` (Exponentiation): `x ** y`

### **2️⃣ Assignment Operators**  
These operators assign values to variables:
- `=` (Assign): `x = 10`
- `+=` (Add and assign): `x += 5` (same as `x = x + 5`)
- `-=` (Subtract and assign): `x -= 5`
- `*=` (Multiply and assign): `x *= 5`
- `/=` (Divide and assign): `x /= 5`
- `//=` (Floor divide and assign): `x //= 5`
- `%=` (Modulus and assign): `x %= 5`
- `**=` (Exponentiate and assign): `x **= 5`
- `&=` (Bitwise AND and assign): `x &= 5`
- `|=` (Bitwise OR and assign): `x |= 5`
- `^=` (Bitwise XOR and assign): `x ^= 5`
- `>>=` (Right shift and assign): `x >>= 5`
- `<<=` (Left shift and assign): `x <<= 5`
- `:=` (Walrus operator - assigns and returns a value): `if (n := len(data)) > 0:`

### **3️⃣ Comparison Operators**  
These operators compare values and return `True` or `False`:
- `==` (Equal to): `x == y`
- `!=` (Not equal to): `x != y`
- `>` (Greater than): `x > y`
- `<` (Less than): `x < y`
- `>=` (Greater than or equal to): `x >= y`
- `<=` (Less than or equal to): `x <= y`

### **4️⃣ Logical Operators**  
These operators perform logical operations:
- `and` (Logical AND): `x > 5 and y < 10`
- `or` (Logical OR): `x > 5 or y < 10`
- `not` (Logical NOT): `not(x > 5)`

### **5️⃣ Identity Operators**  
These operators compare the memory location of two objects:
- `is`: `x is y`
- `is not`: `x is not y`

### **6️⃣ Membership Operators**  
These operators check for membership in a sequence:
- `in`: `x in y`
- `not in`: `x not in y`

### **7️⃣ Bitwise Operators**  
These operators perform bit-level operations:
- `&` (AND): `x & y`
- `|` (OR): `x | y`
- `^` (XOR): `x ^ y`
- `~` (NOT): `~x`
- `<<` (Left shift): `x << 2`
- `>>` (Right shift): `x >> 2`

---

## **🔹 Python Data Types**  

Python has several built-in data types to define the kind of data a variable can hold. Here’s a breakdown:

### **1️⃣ Numeric Types**  
- **`int`**: Integer numbers (e.g., `10`, `-5`, `1000`)  
- **`float`**: Decimal numbers (e.g., `3.14`, `-2.5`, `0.0001`)  
- **`complex`**: Complex numbers (e.g., `3 + 4j`, `2 - 7j`)

### **2️⃣ Sequence Types**  
- **`str`**: String (e.g., `"Hello"`, `'Python'`)  
- **`list`**: An ordered, mutable collection (e.g., `[1, 2, 3]`, `['a', 'b']`)  
- **`tuple`**: An ordered, immutable collection (e.g., `(1, 2, 3)`, `('x', 'y')`)  
- **`range`**: A sequence of numbers (e.g., `range(5)` → 0, 1, 2, 3, 4)

### **3️⃣ Set Types**  
- **`set`**: An unordered collection of unique elements (e.g., `{1, 2, 3}`)  
- **`frozenset`**: An immutable set (e.g., `frozenset([1, 2, 3])`)

### **4️⃣ Mapping Type**  
- **`dict`**: A collection of key-value pairs (e.g., `{'name': 'Ayman', 'age': 25}`)

### **5️⃣ Boolean Type**  
- **`bool`**: Represents `True` or `False`

### **6️⃣ Binary Types**  
- **`bytes`**: Immutable byte sequence  
- **`bytearray`**: Mutable byte sequence  
- **`memoryview`**: Memory view object for working with binary data

### **7️⃣ None Type**  
- **`NoneType`**: Represents the absence of a value (`None`)

---

## **🔹 List of 39 Python Keywords**  

Below is the list of **39 Python keywords** with a brief description and syntax for their use in Python. These keywords are reserved and cannot be used as variable names.

### **1. False**
- **Description**: Represents the Boolean false value.
- **Syntax**: `False`
  
### **2. None**
- **Description**: Represents the absence of a value or null.
- **Syntax**: `None`

### **3. True**
- **Description**: Represents the Boolean true value.
- **Syntax**: `True`

### **4. and**
- **Description**: Logical AND operator.
- **Syntax**: `if x > 0 and y > 0:`

### **5. as**
- **Description**: Used to create an alias when importing a module.
- **Syntax**: `import numpy as np`

### **6. assert**
- **Description**: Used for debugging to test conditions.
- **Syntax**: `assert x > 0, "x must be positive"`

### **7. async**
- **Description**: Declares an asynchronous function.
- **Syntax**: `async def my_function():`

### **8. await**
- **Description**: Pauses the execution of an async function until the result is available.
- **Syntax**: `result = await my_function()`

### **9. break**
- **Description**: Exits the closest enclosing loop.
- **Syntax**: `while True: break`

### **10. class**
- **Description**: Defines a class.
- **Syntax**: `class MyClass:`

### **11. continue**
- **Description**: Skips the current iteration of a loop and proceeds to the next iteration.
- **Syntax**: `for i in range(5): if i == 2: continue`

### **12. def**
- **Description**: Defines a function.
- **Syntax**: `def my_function():`

### **13. del**
- **Description**: Deletes an object or variable.
- **Syntax**: `del my_variable`

### **14. elif**
- **Description**: Specifies an alternate condition if the initial `if` condition is false.
- **Syntax**: `elif x > 10:`

### **15. else**
- **Description**: Defines a block of code to execute if none of the `if` or `elif` conditions are true.
- **Syntax**: `else:`

### **16. except**
- **Description**: Handles exceptions raised in a `try` block.
- **Syntax**: `except ValueError:`

### **17. finally**
- **Description**: Defines a block that is always executed after `try`/`except`.
- **Syntax**: `finally:`

### **18. for**
- **Description**: Used to define a loop that iterates over a sequence.
- **Syntax**: `for x in range(5):`

### **19. from**
- **Description**: Used to import specific parts of a module.
- **Syntax**: `from math import sqrt`

### **20. global**
- **Description**: Declares a global variable inside a function.
- **Syntax**: `global x`

### **21. if**
- **Description**: Defines a conditional statement.
- **Syntax**: `if x > 0:`

### **22. import**
- **Description**: Imports a module into the current namespace.
- **Syntax**: `import math`

### **23. in**
- **Description**: Used to check membership in a sequence.
- **Syntax**: `if x in [1, 2, 3]:`

### **24. is**
- **Description**: Checks if two variables refer to the same object.
- **Syntax**: `if x is y:`

### **25. lambda**
- **Description**: Defines an anonymous function.
- **Syntax**: `lambda x: x + 2`

### **26. nonlocal**
- **Description**: Declares a variable in the nearest enclosing scope (not global).
- **Syntax**: `nonlocal x`

### **27. not**
- **Description**: Logical NOT operator.
- **Syntax**: `if not x:`

### **28. or**
- **Description**: Logical OR operator.
- **Syntax**: `if x > 0 or y < 10:`

### **29. pass**
- **Description**: A placeholder statement that does nothing.
- **Syntax**: `pass`

### **30. raise**
- **Description**: Raises an exception.
- **Syntax**: `raise ValueError("Invalid input")`

### **31. return**
- **Description**: Returns a value from a function.
- **Syntax**: `return x`

### **32. try**
- **Description**: Defines a block that tests a condition for exceptions.
- **Syntax**: `try:`

### **33. while**
- **Description**: Defines a loop that runs as long as a condition is true.
- **Syntax**: `while x < 10:`

### **34. with**
- **Description**: Used to simplify resource management (e.g., files).
- **Syntax**: `with open('file.txt', 'r') as file:`

### **35. yield**
- **Description**: Pauses a function and returns a generator value.
- **Syntax**: `yield x`

### **36. match**
- **Description**: Used for pattern matching (Python 3.10+).
- **Syntax**: `match x:`

### **37. case**
- **Description**: Used in a `match` statement to define patterns.
- **Syntax**: `case 1:`

### **38. __debug__**
- **Description**: A special constant used to check if Python is running in debug mode.
- **Syntax**: `if __debug__:`

### **39. __import__**
- **Description**: A function used to manually import a module (rarely used).
- **Syntax**: `__import__('math')`
