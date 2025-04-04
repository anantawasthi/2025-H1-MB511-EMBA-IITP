

## 📘 Chapter 3: Pandas Fundamentals

---

### 📌 Introduction

In this chapter, we begin working directly with data using Pandas. After learning how to load data, it's essential to understand the **structure and behavior of a Pandas DataFrame**, which is the core object used in data analysis.

We will explore the foundational operations that help you get familiar with your dataset—viewing, selecting, slicing, and filtering data, much like what you do in Excel, but using Python.

---

### 🎯 Objective

By the end of this chapter, you will be able to:

- Create DataFrames using dictionaries or files (Excel/CSV)

- Understand the structure and key properties of a DataFrame

- Select specific rows and columns using indexing

- Filter rows based on conditions (e.g., salaries above a threshold)

---

### 🛠️ 3.2 Activity: Create a DataFrame from Scratch

#### 📝 Description:

Let’s manually create a table with employee data using a Python dictionary. This simulates building a small dataset from scratch.

```python
"""
This code creates a small employee table using a Python dictionary.
It uses Pandas to convert the dictionary into a DataFrame (like a table).
"""

import pandas as pd

data = {
    'Employee': ['Anita', 'Ravi', 'Meena'],
    'Department': ['HR', 'Finance', 'IT'],
    'Salary': [55000, 60000, 58000]
}

df = pd.DataFrame(data)
print(df)
```

---

### 📂 3.3 Activity: Load a DataFrame from Excel

#### 📝 Description:

Most real-world data is stored in Excel files. Let’s load an Excel sheet into Pandas so we can analyze it.

```python
"""
This code reads data from an Excel file into a DataFrame using Pandas.
It then prints the first 5 rows to preview the content.
"""

df = pd.read_excel('employee_data_ch3.xlsx')
print(df.head())
```

---

### 🔍 3.4 Activity: Inspect the Data

#### 📝 Description:

Once we load a dataset, it’s important to understand its size, structure, and contents. These basic commands help with that.

```python
"""
This code prints key details about the dataset:
- Shape (rows and columns)
- Column names
- Data types
- Summary statistics (only for numbers)
"""

print("Shape of the data:", df.shape)
print("Column names:", df.columns.tolist())
print("\nData types:")
print(df.dtypes)
print("\nSummary statistics:")
print(df.describe())
```

---

### 🎯 3.5 Activity: Selecting Columns

#### 📝 Description:

Sometimes we only need a few columns from the table. Here’s how to extract just the employee names and their salaries.

```python
"""
This code selects and displays only the 'Employee_Name' and 'Salary' columns
from the full dataset.
"""

print(df[['Employee_Name', 'Salary']])
```

---

### 🔎 3.6 Activity: Selecting Specific Rows

#### 📝 Description:

We can select rows based on their number or based on a condition (e.g., Employee name = Meena).

```python
"""
This code shows two types of row selection:
1. Using the row number (iloc) to select the 3rd row.
2. Using a condition (loc) to find the row where Employee_Name is 'Meena'.
"""

print("3rd Row (Index 2):")
print(df.iloc[2])

print("\nRow where Employee_Name is 'Meena':")
print(df.loc[df['Employee_Name'] == 'Meena'])
```

---

### ✅ 3.7 Activity: Filter Rows Using Conditions

#### 📝 Description:

Just like in Excel, we can apply conditions to filter rows. Here we display employees earning more than ₹55,000.

```python
"""
This code filters the dataset to show only those rows
where the 'Salary' column is greater than 55000.
"""

print(df[df['Salary'] > 55000])
```

---

### 📁 3.8 Excel File for Practice

You can download and practice with this dataset:

📎 Download employee_data_ch3.xlsx

---

### 🧠 Recap

- You created DataFrames manually and from Excel

- You viewed and summarized data with `head()`, `shape`, `describe()`

- You selected rows and columns using basic indexing

- You filtered records using simple conditions


