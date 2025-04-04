

## 📘 Chapter 7: Merging and Joining DataFrames

---

### 📌 Introduction

Often, data is split across multiple tables—just like different Excel sheets for employees, departments, or salary bands. In such cases, we need to **merge** or **join** the data based on a common column.

Pandas makes this easy with functions like `merge()`, `concat()`, and `join()`, allowing you to **combine datasets just like VLOOKUP in Excel**—but with more control and flexibility.

---

### 🎯 Objectives

By the end of this chapter, you will be able to:

- Understand different types of joins (inner, left, right, outer)

- Combine two DataFrames using `merge()`

- Append rows using `concat()`

- Apply merges similar to SQL joins or Excel VLOOKUP

---

### 🔗 7.2 Activity: Merge Two DataFrames (Basic)

#### 📝 Description:

Let’s merge an **employee** dataset with a **department details** dataset using `merge()` on the “Department” column.

```python
"""
This code merges the employee dataset with department details
using a common 'Department' column, similar to a VLOOKUP in Excel.
"""

# Employee dataset
df_emp = pd.DataFrame({
    'Name': ['anita', 'ravi', 'meena'],
    'Department': ['HR', 'Finance', 'IT'],
    'Salary': [55000, 60000, 58000]
})

# Department details dataset
df_dept = pd.DataFrame({
    'Department': ['HR', 'Finance', 'IT'],
    'Manager': ['Alok', 'Sunita', 'Ramesh']
})

# Merge on 'Department'
merged_df = pd.merge(df_emp, df_dept, on='Department', how='inner')
print(merged_df)
```

---

### 🧩 7.3 Activity: Left Join

#### 📝 Description:

What if some employees belong to departments that aren’t listed in the department table? We use a **left join** to keep all employee records.

```python
"""
This code performs a left join to retain all employees,
even if some departments don’t have manager information.
"""

merged_left = pd.merge(df_emp, df_dept, on='Department', how='left')
print(merged_left)
```

---

### ➕ 7.4 Activity: Concatenate Rows

#### 📝 Description:

Let’s say you get two monthly datasets—how do you **stack** them? Use `concat()`.

```python
"""
This code combines two DataFrames vertically (row-wise),
like appending new records from another month's dataset.
"""

df_jan = pd.DataFrame({'Name': ['anita', 'ravi'], 'Salary': [55000, 60000]})
df_feb = pd.DataFrame({'Name': ['meena', 'sohan'], 'Salary': [58000, 54000]})

combined_df = pd.concat([df_jan, df_feb], ignore_index=True)
print(combined_df)
```

---

### 🧱 7.5 Activity: Merge on Multiple Columns

#### 📝 Description:

When joining datasets, you may need to match on multiple keys (e.g., Department and Location).

```python
"""
This code merges two DataFrames using both 'Department' and 'Location'
to match records more precisely.
"""

df1 = pd.DataFrame({
    'Department': ['HR', 'Finance', 'IT'],
    'Location': ['Delhi', 'Mumbai', 'Chennai'],
    'Headcount': [10, 12, 9]
})

df2 = pd.DataFrame({
    'Department': ['HR', 'Finance', 'IT'],
    'Location': ['Delhi', 'Mumbai', 'Chennai'],
    'Manager': ['Alok', 'Sunita', 'Ramesh']
})

merged_multi = pd.merge(df1, df2, on=['Department', 'Location'], how='inner')
print(merged_multi)
```



---

## ✅ Best Practices for Running Joins in Pandas

---

### 1. **Always Inspect the Join Columns First**

Before merging, check:

- Column names (ensure spelling and casing match)

- Data types (object vs int vs category can cause silent errors)

- Presence of duplicates or nulls in key columns

```python
print(df1['Department'].unique())
print(df1.dtypes)
```

---

### 2. **Use `how='inner'` When You Only Want Matched Records**

Default `merge()` does an inner join. Use this when:

- You only want records that exist in **both** datasets.

- Example: Only show departments that exist in both employee and manager tables.

```python
pd.merge(df1, df2, on='Department', how='inner')
```

---

### 3. **Use `how='left'` to Keep All Records from the Left Table**

Best when one table is a **master table** (e.g., employee list), and you want to enrich it with additional info.

```python
pd.merge(employee_df, manager_df, on='Department', how='left')
```

---

### 4. **Handle Duplicates Carefully**

If the join key has duplicate values in either table, you may get **unexpected row duplications** in the result.

> 🔍 Always check for duplicates using:

```python
df.duplicated(subset=['join_column']).sum()
```

---

### 5. **Use `validate=` to Catch Unintended Join Behavior**

This is a **hidden gem** in Pandas! Helps detect when your join isn't what you expect.

```python
pd.merge(df1, df2, on='ID', how='left', validate='one_to_one')  # Or 'many_to_one', etc.
```

---

### 6. **Prefix or Suffix Overlapping Columns**

Avoid confusion if both tables have similarly named columns.

```python
pd.merge(df1, df2, on='Department', suffixes=('_emp', '_mgr'))
```

---

### 7. **Watch Out for Nulls in Join Columns**

Nulls will not match with anything, so rows with nulls in join columns are **dropped in inner joins**, or remain **unmatched in left/right joins**.

```python
df[df['join_column'].isnull()]
```

---

### 8. **Always Review the Output**

After merging, review a few rows with `.head()` and validate the merge worked as intended.

```python
print(merged_df.head())
```

---

### 9. **For Multi-Key Joins, Check Both Columns for Integrity**

If joining on multiple columns (e.g., `['Department', 'Location']`), make sure:

- Both columns exist in both DataFrames

- They are clean (no typos, consistent formats)

---

### 10. **Document Your Join Logic**

If you're writing scripts for others (or teaching), make sure to comment your code explaining:

- Why a specific `how` method was chosen

- What the expected output is


