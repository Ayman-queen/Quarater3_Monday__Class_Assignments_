1️⃣ Control Flow 
# if-Else Statement
x =5
if x>10:
    print("x is greater than 10")
else:
    print("x is less than 10 or equal to 10")
# if-Elif-Else Statement
x =5
if x>10:
    print("x is greater than 10")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 10")
x = 10
if x > 0:
    print("Positive number")
elif x < 0:
    print("Negative number")
else:
    print("Zero")
    
2️⃣ Loops (for, while)
    
# For loop example
for i in range(5):
    print(i)

# While loop example
count = 0
while count < 5:
    print(count)
    count += 1

3️⃣ Lists (Ordered, Mutable, Allows Duplicates)

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Adding elements
my_list.append(6)  # Adds 6 at the end
my_list.insert(2, 10)  # Inserts 10 at index 2

# Removing elements
my_list.remove(3)  # Removes the first occurrence of 3
popped_value = my_list.pop()  # Removes and returns the last element

# Finding elements
index = my_list.index(2)  # Returns index of first occurrence of 2
count = my_list.count(10)  # Counts occurrences of 10

# Sorting and reversing
my_list.sort()  # Sorts list in ascending order
my_list.reverse()  # Reverses the list

# Copying and clearing
copy_list = my_list.copy()  # Creates a copy
my_list.clear()  # Removes all elements

print(copy_list)  # Output the copied list

4️⃣ Dictionaries (Key-Value Pairs, Mutable)  

# Creating a dictionary
my_dict = {"name": "Nasir", "age": 25, "city": "Karachi"}

# Accessing values
print(my_dict["name"])  # Access value using key
print(my_dict.get("age"))  # Safer way to get a value

# Adding and updating values
my_dict["age"] = 26  # Updating value
my_dict["gender"] = "Male"  # Adding new key-value pair

# Removing items
removed_value = my_dict.pop("city")  # Removes 'city' and returns its value
last_item = my_dict.popitem()  # Removes and returns the last inserted item

# Checking keys and values
keys = my_dict.keys()  # Returns all keys
values = my_dict.values()  # Returns all values
items = my_dict.items()  # Returns all key-value pairs

# Copying and clearing
copy_dict = my_dict.copy()  # Creates a copy
my_dict.clear()  # Removes all elements

print(copy_dict)  # Output the copied dictionary

5️⃣ Sets (Unordered, Unique Elements, Mutable)

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements
my_set.add(6)  # Adds 6 to the set

# Removing elements
my_set.remove(3)  # Removes 3 (raises error if not found)
my_set.discard(10)  # Removes 10 if it exists (no error if missing)
popped_value = my_set.pop()  # Removes and returns an arbitrary element

# Set operations
another_set = {4, 5, 6, 7, 8}

union_set = my_set.union(another_set)  # Combines both sets
intersection_set = my_set.intersection(another_set)  # Common elements
difference_set = my_set.difference(another_set)  # Elements in my_set but not in another_set

# Copying and clearing
copy_set = my_set.copy()  # Creates a copy
my_set.clear()  # Removes all elements

print(copy_set)  # Output the copied set

6️⃣ Frozensets (Immutable Set, Unique Elements)

# Creating a frozenset
my_frozenset = frozenset({1, 2, 3, 4, 5})

# Set operations (allowed)
another_frozenset = frozenset({4, 5, 6, 7})
union_fs = my_frozenset.union(another_frozenset)  # Combines both
intersection_fs = my_frozenset.intersection(another_frozenset)  # Common elements
difference_fs = my_frozenset.difference(another_frozenset)  # Unique to my_frozenset

# ❌ Immutable – cannot modify elements
# my_frozenset.add(6)  # ❌ Error: Frozensets are immutable

print(union_fs)  # Output the union of both frozensets

    