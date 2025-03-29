# Unit 7 - AI for Managers

---

## 🐍 1. Introduction to Python

Python is a high-level, interpreted programming language that emphasizes readability and simplicity. It is widely used in business analytics, machine learning, automation, and web development due to its vast ecosystem and easy syntax.

**Why Python for Managers?**

- **Quick to learn**: Python’s syntax is similar to plain English, making it approachable for beginners.

- **Data-friendly**: It allows quick manipulation of data formats like Excel files, CSVs, and database outputs.

- **Tool Integration**: Python works well with tools you may already use, like Excel, Tableau, and SQL.

- **Community & Libraries**: Python has an active global community and thousands of free libraries to simplify tasks such as data cleaning, visualization, and forecasting.

---

## 📈 2. Why Python is Popular

- **Readable Syntax**: You don’t need to be a programmer to understand basic Python code.

- **Extensive Libraries**: With tools like `pandas` for data analysis, `matplotlib` for visualizations, and `scikit-learn` for machine learning, much of the heavy lifting is already done.

- **Community Support**: Whenever you're stuck, a quick web search leads to ready solutions.

- **Versatility**: Python is used in banking, healthcare, logistics, education, HR analytics, and more.

---

## 🧱 3. Data Types in Python

Python has various types of data, just like we do in real life (e.g., numbers, names, Yes/No answers).

### 📌 3.1 String

Strings are sequences of characters. These can be names, comments, email addresses, or product descriptions.

```python
name = "Anant"              # Assigning text to a variable
print(name)                 # Output: Anant
print(type(name))           # Output: <class 'str'> - this shows the variable is a string
```

You can combine strings using `+` and use functions like `.upper()`, `.lower()`, and `.replace()` for formatting.

---

### 🔢 3.2 Numeric

Used for numbers in your data.

- **Integer**: Whole numbers (e.g., number of employees, days)

- **Float**: Numbers with decimal points (e.g., salary, interest rate)

```python
age = 35                   # Integer - number without a decimal
salary = 75250.5           # Float - number with decimal

print(type(age))           # Output: <class 'int'>
print(type(salary))        # Output: <class 'float'>
```

#### 🔢 3.2.1 Variants of Float

Float values in Python support different styles:

- **Standard Float**: Most common decimal format
  
  ```python
  price = 10.75            # Could be used for pricing a product
  print(price)
  ```

- **Scientific Notation**: Useful for very large or small values
  
  ```python
  population_growth = 3.2e6  # 3.2 million people (3.2 * 10^6)
  print(population_growth)
  ```

- **Negative Float**: Used to indicate loss or drop in performance
  
  ```python
  loss = -1523.45           # Negative float
  print(loss)
  ```

- **High Precision Float**: For financial applications where cents and decimals matter a lot

```python
from decimal import Decimal
value = Decimal('10.123456789123456789')  # Accurate to many decimal places
print(value)
```

---

### 🔘 3.3 Boolean

Boolean values help represent True/False or Yes/No scenarios in business logic.

```python
is_manager = True                     # Indicates employee is a manager
print(is_manager)                     # Output: True
print(type(is_manager))               # Output: <class 'bool'>
```

Booleans are used in decision-making rules, like eligibility for bonus, approval status, etc.

---

## 🔄 4. Type Conversion

Often, data comes in the wrong format (like numbers as text). We can convert between types using built-in functions:

```python
# Convert float to integer - decimal part is discarded
x = 10.5
print(int(x))       # Output: 10

# Convert integer to string - useful for reports or labels
y = 20
print(str(y))       # Output: "20"

# Convert string to float - required for calculations
s = "99.9"
print(float(s))     # Output: 99.9
```

---

## ➕ 5. Arithmetic Operations

You can do basic math operations to support business analysis (e.g., profit/loss, budgeting).

```python
a = 15
b = 4

print(a + b)    # Addition: Total sales from two branches
print(a - b)    # Subtraction: Net savings
print(a * b)    # Multiplication: Cost per item * number of items
print(a / b)    # Division: Average per unit
print(a // b)   # Floor Division: Whole units only
print(a % b)    # Modulo: Remainder or leftovers
print(a ** b)   # Exponentiation: Compound interest or growth
```

---

## 🧠 6. Logical Operators (`and`, `or`, `not`)

Used when you need to check multiple conditions before making a decision.

```python
x = 5

# Both conditions must be true
print(x > 2 and x < 10)  # True: because x is between 2 and 10

# At least one condition must be true
print(x > 2 or x > 20)   # True: x > 2 is true

# Reverses the result
print(not(x > 2))        # False: x > 2 is true, so 'not' makes it false
```

Example: You might use this logic to check if an employee has served >5 years AND met targets before approving a promotion.

---

## 🔀 7. Conditional Statements: if, elif, else

These allow a program to make decisions based on the value of data.

```python
sales = 120000

if sales > 100000:
    print("Excellent Performance Bonus Eligible")
elif sales > 50000:
    print("Meets Expectations")
else:
    print("Needs Improvement")
```

**Managerial Use Case**: Classify employees or business units into performance bands based on KPIs like sales, revenue, customer feedback, etc.

---

## 📝 Quick Practice Exercise for Class

Let’s try applying what we learned!

Write a script that classifies monthly sales input into business performance tiers:

```python
# Input: monthly sales
# Output: categorize into Bronze, Silver, Gold

sales = float(input("Enter monthly sales: "))  # Accept input as decimal

if sales >= 100000:
    print("Gold Tier")          # Best performance category
elif sales >= 50000:
    print("Silver Tier")        # Middle category
else:
    print("Bronze Tier")        # Needs improvement category
```

Encourage students to adapt this logic to real-life contexts:

- Student grading systems

- Customer segmentation

- Vendor rating scales

- Financial risk classifications

---


