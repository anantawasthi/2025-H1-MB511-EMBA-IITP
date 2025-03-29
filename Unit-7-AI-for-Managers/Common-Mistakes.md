

# ⚠️ **Common Mistakes in Python Programming – and How to Avoid Them**

---

Learning Python is fun and intuitive, but beginners often fall into a few traps. This chapter covers **the most common mistakes** made by new programmers and explains how to fix or avoid them—with simple, relatable examples.

---

## 🧱 1. Mistake: Confusing `=` and `==`

### ❌ Problem:

```python
if score = 100:
    print("Perfect Score")
```

### 💥 Why it Fails:

- `=` is used for **assignment** (e.g., `x = 10`)

- `==` is used for **comparison** (e.g., `x == 10`)

### ✅ Correct Code:

```python
if score == 100:
    print("Perfect Score")
```

🧠 **Tip**: Read `==` as “is equal to.” Use it in conditions only.

---

## 🔍 2. Mistake: Forgetting Colons (`:`) After Conditions or Loops

### ❌ Problem:

```python
if age > 18
    print("Adult")
```

### 💥 Why it Fails:

- Python requires a `:` at the end of `if`, `elif`, `else`, `for`, and `while` blocks.

### ✅ Correct Code:

```python
if age > 18:
    print("Adult")
```

🧠 **Tip**: Think of `:` as opening a decision block—just like you’d start a paragraph after a heading.

---

## 🧱 3. Mistake: Wrong Indentation

### ❌ Problem:

```python
if salary > 50000:
print("Bonus Eligible")
```

### 💥 Why it Fails:

- Python uses **indentation** (spaces) to define blocks of code.

- All lines in a block must be indented equally.

### ✅ Correct Code:

```python
if salary > 50000:
    print("Bonus Eligible")
```

🧠 **Tip**: Use 4 spaces for each indent. Never mix tabs and spaces.

---

## 🔄 4. Mistake: Mixing Data Types in Operations

### ❌ Problem:

```python
age = 30
print("Age is " + age)
```

### 💥 Why it Fails:

- You can’t directly combine a string with an integer.

### ✅ Correct Code:

```python
age = 30
print("Age is " + str(age))  # Convert number to string
```

🧠 **Tip**: Use `str()`, `int()`, `float()` to **convert data types** when combining values.

---

## 📚 5. Mistake: Misunderstanding `and` vs `or`

### ❌ Problem:

```python
age = 25
experience = 1

if age > 18 or experience > 2:
    print("Eligible")
```

### 💥 Why it's Risky:

- The candidate may be too young or inexperienced, but still get marked as eligible.

- Use `and` when **both conditions must be true**.

### ✅ Correct Code:

```python
if age > 18 and experience > 2:
    print("Eligible")
```

🧠 **Tip**:

- `and` = **both** conditions must be true

- `or` = **at least one** must be true

---

## 📉 6. Mistake: Off-by-One Errors in Ranges

### ❌ Problem:

```python
for i in range(1, 5):
    print(i)
```

### 💥 Surprise:

This prints:

```
1
2
3
4
```

But many beginners expect it to print up to 5.

### ✅ Correct Code:

```python
for i in range(1, 6):  # range is up to but not including 6
    print(i)
```

🧠 **Tip**: `range(a, b)` means from `a` to `b-1`

---

## 🧠 7. Mistake: Using `input()` Without Conversion

### ❌ Problem:

```python
x = input("Enter a number: ")
print(x + 5)
```

### 💥 Why it Fails:

- `input()` returns a string, not a number.

- You’re trying to add a number to a string.

### ✅ Correct Code:

```python
x = float(input("Enter a number: "))
print(x + 5)
```

🧠 **Tip**: Always **convert input** to the correct type using `int()` or `float()` when needed.

---

## 📦 8. Mistake: Overwriting Built-In Function Names

### ❌ Problem:

```python
list = [1, 2, 3]
print(list)
```

Then later you try:

```python
list("123")  # Error!
```

### 💥 Why it Fails:

- You’ve overwritten Python’s built-in `list()` function by using the same name for a variable.

### ✅ Correct Approach:

```python
my_list = [1, 2, 3]
```

🧠 **Tip**: Avoid using keywords like `list`, `str`, `input`, `sum` as variable names.

---

## 🚨 9. Mistake: Assuming Case Doesn’t Matter

### ❌ Problem:

```python
status = "active"
if status == "Active":
    print("Proceed")
```

### 💥 Why it Fails:

- Python is **case-sensitive**. `"active"` ≠ `"Active"`

### ✅ Correct Code:

```python
if status.lower() == "active":
    print("Proceed")
```

🧠 **Tip**: Use `.lower()` or `.upper()` for case-insensitive comparisons.

---

## 🛑 10. Mistake: Ignoring Error Messages

Many beginners get scared by error messages and don’t read them.

### 🧠 Example Error:

```
TypeError: can only concatenate str (not "int") to str
```

This tells you exactly what's wrong: you're trying to combine a string with an integer without converting it.

---

## ✅ Summary Table

| Mistake                      | How to Avoid                                 |
| ---------------------------- | -------------------------------------------- |
| `=` vs `==`                  | Use `==` in conditions, `=` to assign        |
| Missing colon (`:`)          | Always end `if`, `elif`, `else` with `:`     |
| Wrong indentation            | Use consistent 4-space indents               |
| Mixing data types            | Use `str()`, `int()`, or `float()`           |
| `and` vs `or` confusion      | Think logically: both vs. either             |
| Misusing `range()`           | Remember it's exclusive of the end           |
| Using `input()` without cast | Convert to number using `int()` or `float()` |
| Naming variables like `list` | Use descriptive variable names               |
| Case-sensitive issues        | Use `.lower()` for comparisons               |
| Ignoring error messages      | Read them—they’re often self-explanatory     |


