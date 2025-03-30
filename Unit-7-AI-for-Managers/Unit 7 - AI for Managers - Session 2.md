

## ✅ **Chapter 1: Lists and Basic Data Structures**

---

### 🔹 1.1 List

```python
"""
Demonstrate basic list creation and element access.
Show how indexing works including negative indexing.
"""
fruits = ['apple', 'banana', 'mango']
print(fruits[0])   # Output: 'apple' (first item)
print(fruits[-1])  # Output: 'mango' (last item)
```

```python
"""
Demonstrate list modification using append, remove, and update by index.
Also show how the list structure changes after these operations.
"""
fruits.append('orange')       # Adds 'orange' at the end
fruits.remove('banana')       # Removes 'banana' from the list
fruits[0] = 'grapes'          # Updates first item to 'grapes'
print(fruits)                 # Output: ['grapes', 'mango', 'orange']
```

---

### 🔹 1.2 Tuple

```python
"""
Introduce tuples as immutable sequences and show element access.
Explain that they are useful when data should not change.
"""
dimensions = (10, 20)
print(dimensions[1])  # Output: 20

# Uncommenting the line below would raise a TypeError because tuples are immutable
# dimensions[0] = 30
```

---

### 🔹 1.3 Dictionary

```python
"""
Demonstrate how to create and work with dictionaries using key-value pairs.
Add a new key to the dictionary dynamically.
"""
employee = {'name': 'Anant', 'role': 'Mentor'}
print(employee['name'])  # Output: Anant

employee['department'] = 'Data Science'  # Adding a new key-value pair
print(employee)
```

---

### 🔹 1.4 Set

```python
"""
Showcase set behavior: automatic removal of duplicates and set operations.
Add a new item and display the updated set.
"""
skills = {'Python', 'SQL', 'Python'}  # 'Python' is duplicated

print(skills)         # Output: {'Python', 'SQL'}
skills.add('Excel')   # Adding 'Excel' to the set
print(skills)         # Output: {'Python', 'SQL', 'Excel'}
```

---

### 🔹 1.5 List Comprehension

```python
"""
Use list comprehension to generate squares of numbers 0–4.
Illustrates concise syntax as alternative to traditional loops.
"""
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
```

```python
"""
Use list comprehension to filter even numbers from 0–9.
Includes an 'if' condition for filtering.
"""
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]
```

```python
"""
Use list comprehension with conditional expressions ('if-else').
Label each number as 'even' or 'odd' in a new list.
"""
labels = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
print(labels)  # Output: ['even', 'odd', 'even', 'odd', 'even']
```

---

Perfect! Let’s continue with **Chapter 2: Loops in Python** using your preferred format—**docstring at the top + inline comments**.

---

## ✅ **Chapter 2: Loops in Python**

---

### 🔹 2.1 `for` Loop – Iterating Over a List

```python
"""
Demonstrate how to use a for loop to iterate over elements in a list.
Each element is accessed and printed sequentially.
"""
fruits = ['apple', 'banana', 'mango']

for fruit in fruits:
    print("Fruit:", fruit)  # Prints each fruit in the list
```

---

### 🔹 2.2 `while` Loop – Controlled Repetition

```python
"""
Use a while loop to print numbers from 1 to 5.
Illustrates use of a condition that gets updated inside the loop.
"""
counter = 1

while counter <= 5:
    print("Counter:", counter)  # Output current counter value
    counter += 1                # Increment to avoid infinite loop
```

---

### 🔹 2.3 Summing Items in a List with a `for` Loop

```python
"""
Use a for loop to calculate the total of all numbers in a list.
Illustrates the accumulation pattern using a loop.
"""
sales = [100, 200, 150, 300]
total = 0  # Initialize a variable to accumulate the sum

for amount in sales:
    total += amount  # Add each sale to the total

print("Total Sales:", total)  # Output: 750
```

---

### 🔹 2.4 Using `break` in a Loop

```python
"""
Demonstrate early termination of a loop using 'break'.
Stops the loop if a target is found.
"""
targets = [2, 4, 6, 8, 10]

for number in targets:
    if number == 6:
        print("Target found:", number)
        break  # Exit the loop immediately
    print("Checking:", number)
```

---

### 🔹 2.5 Using `continue` in a Loop

```python
"""
Demonstrate how 'continue' skips the current iteration.
This example skips even numbers and prints only odd ones.
"""
for x in range(1, 6):
    if x % 2 == 0:
        continue  # Skip even numbers
    print("Odd Number:", x)
```

---

Great! Here's **Chapter 3: Functions and Scope** with the same structured template — including docstrings and inline comments for clarity.

---

## ✅ **Chapter 3: Functions and Scope**

---

### 🔹 3.1 Defining and Calling a Function

```python
"""
Define a basic function that takes an input and returns a greeting message.
Demonstrates how to create and call a user-defined function.
"""
def greet(name):
    return f"Hello, {name}!"  # Return a formatted greeting

# Calling the function and displaying the result
print(greet("Anant"))  # Output: Hello, Anant!
```

---

### 🔹 3.2 Local vs Global Scope

```python
"""
Illustrate the concept of local and global variable scope.
Shows how variable names inside and outside functions can differ.
"""
x = 10  # Global variable

def show():
    x = 5  # Local variable (shadows the global variable)
    print("Inside function, x:", x)

show()
print("Outside function, x:", x)  # Confirms that global x is unaffected
```

---

### 🔹 3.3 Enclosing Scope (Nested Functions)

```python
"""
Demonstrate enclosing (nonlocal) scope using nested functions.
The inner function can access variables from the outer function.
"""
def outer():
    course = "MB511"  # Enclosing variable
    def inner():
        print("Course inside inner function:", course)
    inner()

outer()
```

---

### 🔹 3.4 Built-in Functions

```python
"""
Use common built-in functions provided by Python.
These do not require any import and are available by default.
"""
print(len("Python"))     # Output: 6
print(sum([1, 2, 3]))     # Output: 6
print(type(42))           # Output: <class 'int'>
```

---

### 🔹 3.5 Lambda (Anonymous) Functions

```python
"""
Show how to use a lambda function for simple, one-line operations.
Useful for quick, throwaway functionality without defining a full function.
"""
square = lambda x: x * x  # Define a lambda function to compute squares
print(square(5))          # Output: 25
```

---



## ✅ **Chapter 4: Python Libraries and Importing**

---

### 🔹 4.1 Standard Library Import

```python
"""
Demonstrate how to import a standard Python library and use its functions.
Example: using the math module to calculate square root.
"""
import math  # Importing the entire math module

print("Square root of 49:", math.sqrt(49))  # Output: 7.0
```

---

### 🔹 4.2 Import with Alias

```python
"""
Use aliases to simplify references to commonly used libraries.
This improves readability and typing speed.
"""
import pandas as pd  # 'pd' is the conventional alias for pandas
import numpy as np   # 'np' is the standard alias for numpy

# Example usage (basic structure shown here)
print("Pi using NumPy:", np.pi)  # Accessing NumPy's constant
```

---

### 🔹 4.3 Import Specific Functions

```python
"""
Import only a specific function from a module instead of the whole module.
This is memory-efficient and improves clarity when only one function is needed.
"""
from math import ceil  # Importing only the 'ceil' function

print("Ceiling of 4.3:", ceil(4.3))  # Output: 5
```

---

### 🔹 4.4 Import All Functions (Not Recommended)

```python
"""
Importing all functions using * is discouraged.
It can lead to confusion and unexpected behavior due to name collisions.
"""
from math import *  # Not recommended in production code

print(sqrt(36))  # Works, but unclear where 'sqrt' is from
```

---

### 🔹 4.5 Best Practices for Imports

```python
"""
Follow import best practices:
1. Keep all imports at the top of the file.
2. Use aliases for clarity and convention.
3. Avoid wildcard imports.
"""
# Example of clean imports at the top:
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
```

---


