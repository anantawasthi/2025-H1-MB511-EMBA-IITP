## 📘 Chapter 5: Data Cleaning and Transformation

---

### 📌 Introduction

In real-world scenarios, data is often **messy**. It might contain missing values, inconsistent formats, or irrelevant records. Before any meaningful analysis can be done, data must be cleaned and transformed into a usable format.

This chapter introduces essential data cleaning tasks that a data scientist performs regularly—and that managers should be aware of when working with analytics teams.

---

### 🎯 Objectives

By the end of this chapter, you will be able to:

- Identify and handle missing values

- Convert data types

- Apply custom logic using `apply()`

- Perform basic string operations

- Remove duplicate records

---

### ⚠️ 5.2 Activity: Detect Missing Values

#### 📝 Description:

Let’s check where missing values exist in our dataset.

```python
"""
This code checks the dataset for missing (NaN) values in each column
and prints a count of missing entries.
"""

print(df.isnull().sum())
```

---

### ✅ 5.3 Activity: Fill or Replace Missing Values

#### 📝 Description:

We can fill missing values with a constant, an average, or any other logic.

```python
"""
This code fills missing salary values with the average salary from the dataset.
"""

mean_salary = df['Salary'].mean()
df['Salary'].fillna(mean_salary, inplace=True)
print(df[['Name', 'Salary']])
```

---

### 🔁 5.4 Activity: Convert Data Types

#### 📝 Description:

Let’s make sure each column has the right data type. For example, “Joining_Year” should be a number or a date.

```python
"""
This code converts the 'Joining_Year' column to integer type (if not already).
This ensures correct processing during calculations or filtering.
"""

df['Joining_Year'] = df['Joining_Year'].astype(int)
print(df.dtypes)
```

---

### 🧠 5.5 Activity: Apply a Custom Rule

#### 📝 Description:

We can use the `apply()` function to apply any logic. Let’s create a new column classifying employees as “Senior” if they joined before 2020.

```python
"""
This code uses a custom function to classify employees as 'Senior' or 'Junior'
based on their year of joining.
"""

df['Level'] = df['Joining_Year'].apply(lambda x: 'Senior' if x < 2020 else 'Junior')
print(df[['Name', 'Joining_Year', 'Level']])
```

---

### 🔤 5.6 Activity: Perform String Operations

#### 📝 Description:

We can clean or format textual data. For example, converting names to lowercase.

```python
"""
This code converts all employee names to lowercase for standardization.
"""

df['Name'] = df['Name'].str.lower()
print(df['Name'])
```

---

### 🧹 5.7 Activity: Remove Duplicate Records

#### 📝 Description:

In case some records are accidentally repeated, we can easily remove them.

```python
"""
This code removes duplicate rows from the dataset.
Only unique records will remain.
"""

df.drop_duplicates(inplace=True)
print(df)
```


