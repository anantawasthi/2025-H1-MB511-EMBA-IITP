## 📘 Chapter 4: Core Data Operations

---

### 📌 Introduction

Once you're comfortable with viewing and selecting data, the next step is to **manipulate and transform your dataset**. This chapter introduces operations such as adding or removing columns, sorting data, handling missing values, and renaming or updating records.

These operations are essential when preparing data for analysis—what we often refer to as **data wrangling**.

---

### 🎯 Objectives

By the end of this chapter, you will be able to:

- Add, rename, and remove columns

- Sort and reorder data

- Handle missing or null values

- Modify existing values

---

### 🛠️ 4.2 Activity: Add a New Column

#### 📝 Description:

Let’s derive a new column called “Bonus” which is 10% of the employee’s salary.

```python
"""
This code creates a new column named 'Bonus' in the dataset.
The value is calculated as 10% of each employee's salary.
"""

df['Bonus'] = df['Salary'] * 0.10
print(df[['Employee_Name', 'Salary', 'Bonus']])
```

---

### ✏️ 4.3 Activity: Rename Columns

#### 📝 Description:

We may want to give columns more meaningful or standardized names. Let’s rename “Employee_Name” to “Name”.

```python
"""
This code renames the 'Employee_Name' column to 'Name' for better readability.
"""

df.rename(columns={'Employee_Name': 'Name'}, inplace=True)
print(df.head())
```

---

### 🗑️ 4.4 Activity: Delete a Column

#### 📝 Description:

Sometimes we want to remove unnecessary data. Here, we’ll drop the “Bonus” column.

```python
"""
This code removes the 'Bonus' column from the dataset using the drop function.
"""

df.drop(columns=['Bonus'], inplace=True)
print(df.head())
```

---

### 🔃 4.5 Activity: Sorting Data

#### 📝 Description:

Let’s sort employees by their salary, from highest to lowest.

```python
"""
This code sorts the dataset by the 'Salary' column in descending order.
"""

sorted_df = df.sort_values(by='Salary', ascending=False)
print(sorted_df[['Name', 'Salary']])
```

---

### ⚠️ 4.6 Activity: Handle Missing Values

#### 📝 Description:

Let’s assume we have missing salary data. We’ll simulate this by adding a missing value and then handling it.

```python
"""
This code adds a missing value (NaN) to the 'Salary' column,
then fills missing values with the average salary.
"""

import numpy as np

# Simulate a missing value
df.loc[0, 'Salary'] = np.nan

# Fill missing values with average salary
mean_salary = df['Salary'].mean()
df['Salary'].fillna(mean_salary, inplace=True)

print(df[['Name', 'Salary']])
```


