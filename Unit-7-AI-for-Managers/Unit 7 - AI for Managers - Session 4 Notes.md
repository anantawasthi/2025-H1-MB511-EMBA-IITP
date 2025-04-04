## 📘 Chapter 1: What is Pandas?

---

### 📌 Introduction

In the world of data analysis, tools like Excel and SQL are widely used to organize, manipulate, and understand data. However, for large-scale data tasks, especially those requiring automation, **Pandas** offers a robust solution. It is a Python library that makes data handling **fast**, **easy**, and **powerful**, especially when working with structured data like rows and columns.

---

### 🎯 Learning Objectives

After completing this chapter, you will be able to:

- Understand what Pandas is and why it's useful

- Identify real-world problems where Pandas can help

- Recognize the core components of Pandas (`Series`, `DataFrame`)

- Load and inspect basic data using Pandas

- Relate Pandas to familiar tools like Excel

---

### 📖 Concept: What is Pandas?

**Pandas** is an open-source Python library that provides easy-to-use data structures and data analysis tools. It is built on top of another library called **NumPy** and is tailored for working with **tabular data**, i.e., data arranged in rows and columns.

The name "Pandas" is derived from:

- **Panel Data** (multi-dimensional data sets used in economics and statistics)

- **Python Data Analysis**

---

### 🕰️ A Brief History of Pandas

- **2008**: Created by Wes McKinney while working at AQR Capital, a hedge fund

- **2009**: Open-sourced for public use

- **2015 onward**: Became a core part of the data science ecosystem in Python

- **Today**: Maintained by a large open-source community and widely used in finance, healthcare, HR, education, and government sectors

---

### 🧠 Real-World Analogy

Think of Pandas as a **supercharged version of Excel** that you can control programmatically:

- Like Excel, you can work with rows and columns

- Unlike Excel, Pandas can handle **millions of rows effortlessly**

- It allows **automation, reproducibility, and customization** through Python

---

### 🔍 Why Use Pandas?

| Scenario                     | Pandas Makes It Easy To...                     |
| ---------------------------- | ---------------------------------------------- |
| Clean employee records       | Remove missing or duplicate entries            |
| Analyze sales data           | Group and summarize by region or product       |
| Create reports               | Export filtered datasets into Excel or CSV     |
| Merge HR and payroll records | Use join operations similar to VLOOKUP         |
| Study customer churn         | Identify patterns based on transaction history |

---

### 🧱 Core Components

| Component   | Description                        | Analogy             |
| ----------- | ---------------------------------- | ------------------- |
| `Series`    | A single column of data            | One column in Excel |
| `DataFrame` | A full table with rows and columns | Excel worksheet     |

---

### 💻 Code Example: Creating Your First DataFrame

```python
"""
This code creates a simple employee table using a dictionary.
The dictionary is passed to pd.DataFrame to create a structured table.
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

**Output:**

```
  Employee Department  Salary
0   Anita         HR   55000
1    Ravi    Finance   60000
2   Meena         IT   58000
```

---

### 🧪 Sample Use Case: HR Manager – Average Salary by Department

Let’s say you're an HR manager and want to calculate the **average salary** per department.

```python
"""
This code groups the data by Department and calculates the average salary.
"""

df.groupby('Department')['Salary'].mean()
```

---

### 📁 Practice Dataset

To help you practice, download the Excel file below that contains a sample dataset for this chapter.

📎 Download employee_salary_data_ch1.xlsx

This dataset contains the following columns:

- `Employee_ID`

- `Employee_Name`

- `Department`

- `Salary`

Use this to try grouping, filtering, and calculating basic statistics.

---

### 🧠 Key Takeaways

- **Pandas** is a Python library for fast and efficient data handling

- It's especially good for structured/tabular data (rows and columns)

- The two primary objects in Pandas are `Series` (1D) and `DataFrame` (2D)

- Pandas is widely used in real-world business and management analytics

- You can start simple—with just a few lines of code

---

### 📝 Reflection Questions

1. How is Pandas similar to Excel? How is it different?

2. What are some examples in your domain where Pandas could be helpful?

3. Why do you think Pandas is useful in managerial decision-making?

---

## 📘 Chapter 2: Getting Started with Pandas

---

### 📌 Introduction

Before diving deeper into analysis, it's important to understand the **basic usage** of Pandas. This chapter introduces how to import the Pandas library, create basic data structures, and read data from files. These operations are the starting point for all analysis work.

---

### 🎯 Learning Objectives

After completing this chapter, you will be able to:

- Import the Pandas library in Python

- Create basic `DataFrame` and `Series` objects

- Read data from Excel and CSV files

- Understand how data is structured inside a DataFrame

---

### 🧰 Importing Pandas

```python
"""
This line imports the Pandas library and gives it a shorter alias 'pd'.
"""

import pandas as pd
```

---

### 🧱 Core Structures: Series and DataFrame

```python
"""
This code creates a DataFrame from a dictionary representing employee records.
"""

data = {
    'Employee': ['Anita', 'Ravi', 'Meena'],
    'Department': ['HR', 'Finance', 'IT'],
    'Salary': [55000, 60000, 58000]
}

df = pd.DataFrame(data)
print(df)
```

Output:

```
  Employee Department  Salary
0   Anita         HR   55000
1    Ravi    Finance   60000
2   Meena         IT   58000
```

---

### 📥 Reading Data from an Excel File

```python
"""
This code loads employee data from an Excel file and prints the first 5 rows.
"""

df = pd.read_excel('employee_data_ch2.xlsx')
print(df.head())
```

---

### 🔍 Exploring the Dataset

```python
"""
This code shows key information about the dataset:
- Shape (rows and columns)
- Data types of each column
- Descriptive statistics for numeric columns
"""

print("Shape:", df.shape)
print("Column Names:", df.columns.tolist())
print("\nData Types:\n", df.dtypes)
print("\nSummary Statistics:\n", df.describe())
```

---

### 📁 Practice Dataset

Use this dataset to try out reading and inspecting your first DataFrame:
📎 Download employee_data_ch2.xlsx

Columns include:

- `Employee_ID`

- `Employee_Name`

- `Department`

- `Salary`

- `Joining_Year`

- `Location`

---

### 🧠 Key Takeaways

- You can create a DataFrame from Python data structures

- Pandas makes it easy to read Excel and CSV files

- Use `.head()`, `.shape`, `.describe()` to understand your data quickly

---

### 📝 Reflection Questions

1. What is the difference between `Series` and `DataFrame`?

2. What does `df.describe()` tell you?

3. Which method would you use to load an Excel file?

---

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

### 🛠️ Activity: Create a DataFrame from Scratch

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

### 📂 Activity: Load a DataFrame from Excel

```python
"""
This code reads data from an Excel file into a DataFrame using Pandas.
It then prints the first 5 rows to preview the content.
"""

df = pd.read_excel('employee_data_ch3.xlsx')
print(df.head())
```

---

### 🔍 Activity: Inspect the Data

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

### 🎯 Activity: Selecting Columns

```python
"""
This code selects and displays only the 'Employee_Name' and 'Salary' columns
from the full dataset.
"""

print(df[['Employee_Name', 'Salary']])
```

---

### 🔎 Activity: Selecting Specific Rows

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

### ✅ Activity: Filter Rows Using Conditions

```python
"""
This code filters the dataset to show only those rows
where the 'Salary' column is greater than 55000.
"""

print(df[df['Salary'] > 55000])
```

---

### 📁 Excel File for Practice

📎 Download employee_data_ch3.xlsx

This dataset includes fields like:

- `Employee_ID`

- `Employee_Name`

- `Department`

- `Salary`

- `Joining_Year`

- `Location`

---

### 🧠 Recap

- You created DataFrames manually and from Excel

- You viewed and summarized data with `head()`, `shape`, `describe()`

- You selected rows and columns using basic indexing

- You filtered records using simple conditions



## 📘 Chapter 4: Core Data Operations

---

### 📌 Introduction

Once you're comfortable with viewing and selecting data, the next step is to manipulate and transform your dataset. This chapter introduces operations such as adding or removing columns, sorting data, handling missing values, and renaming or updating records.

---

### 🎯 Objectives

By the end of this chapter, you will be able to:

- Add, rename, and remove columns

- Sort and reorder data

- Handle missing or null values

- Modify existing values

---

### 🛠️ Activity: Add a New Column

```python
"""
This code creates a new column named 'Bonus' in the dataset.
The value is calculated as 10% of each employee's salary.
"""

df['Bonus'] = df['Salary'] * 0.10
print(df[['Employee_Name', 'Salary', 'Bonus']])
```

---

### ✏️ Activity: Rename Columns

```python
"""
This code renames the 'Employee_Name' column to 'Name' for better readability.
"""

df.rename(columns={'Employee_Name': 'Name'}, inplace=True)
print(df.head())
```

---

### 🗑️ Activity: Delete a Column

```python
"""
This code removes the 'Bonus' column from the dataset using the drop function.
"""

df.drop(columns=['Bonus'], inplace=True)
print(df.head())
```

---

### 🔃 Activity: Sorting Data

```python
"""
This code sorts the dataset by the 'Salary' column in descending order.
"""

sorted_df = df.sort_values(by='Salary', ascending=False)
print(sorted_df[['Name', 'Salary']])
```

---

### ⚠️ Activity: Handle Missing Values

```python
"""
This code adds a missing value (NaN) to the 'Salary' column,
then fills missing values with the average salary.
"""

import numpy as np

df.loc[0, 'Salary'] = np.nan
mean_salary = df['Salary'].mean()
df['Salary'].fillna(mean_salary, inplace=True)
print(df[['Name', 'Salary']])
```

---

### 📁 Excel File for Practice

📎 Download employee_data_ch4.xlsx

---

### 🧠 Recap

- You added, renamed, and deleted columns in a DataFrame

- You sorted records by numerical columns

- You handled missing data using fill strategies

---

## 📘 Chapter 5: Data Cleaning and Transformation

---

### 📌 Introduction

In real-world scenarios, data is often messy. It might contain missing values, inconsistent formats, or irrelevant records. Before any meaningful analysis can be done, data must be cleaned and transformed into a usable format.

---

### 🎯 Objectives

By the end of this chapter, you will be able to:

- Identify and handle missing values

- Convert data types

- Apply custom logic using `apply()`

- Perform basic string operations

- Remove duplicate records

---

### ⚠️ Activity: Detect Missing Values

```python
"""
This code checks the dataset for missing (NaN) values in each column
and prints a count of missing entries.
"""

print(df.isnull().sum())
```

---

### ✅ Activity: Fill or Replace Missing Values

```python
"""
This code fills missing salary values with the average salary from the dataset.
"""

mean_salary = df['Salary'].mean()
df['Salary'].fillna(mean_salary, inplace=True)
print(df[['Name', 'Salary']])
```

---

### 🔁 Activity: Convert Data Types

```python
"""
This code converts the 'Joining_Year' column to integer type (if not already).
"""

df['Joining_Year'] = df['Joining_Year'].astype(int)
print(df.dtypes)
```

---

### 🧠 Activity: Apply a Custom Rule

```python
"""
This code uses a custom function to classify employees as 'Senior' or 'Junior'
based on their year of joining.
"""

df['Level'] = df['Joining_Year'].apply(lambda x: 'Senior' if x < 2020 else 'Junior')
print(df[['Name', 'Joining_Year', 'Level']])
```

---

### 🔤 Activity: Perform String Operations

```python
"""
This code converts all employee names to lowercase for standardization.
"""

df['Name'] = df['Name'].str.lower()
print(df['Name'])
```

---

### 🧹 Activity: Remove Duplicate Records

```python
"""
This code removes duplicate rows from the dataset.
Only unique records will remain.
"""

df.drop_duplicates(inplace=True)
print(df)
```

---

### 📁 Excel File for Practice

📎 Download employee_data_ch5.xlsx

---

### 🧠 Recap

- You detected and filled missing values

- You converted data types and applied custom logic

- You cleaned and standardized string data

- You removed duplicate records

---

## 📘 Chapter 6: Grouping and Aggregation

---

### 📌 Introduction

In business settings, you often need to answer questions like:

- What is the average salary per department?

- How many employees joined each year?

- What is the total bonus payout by location?

Pandas makes it easy to group data and apply aggregation functions (like sum, mean, count) to each group. This chapter introduces these techniques.

---

### 🎯 Objectives

By the end of this chapter, you will be able to:

- Group rows based on a column (e.g., Department)

- Apply aggregation functions like `sum()`, `mean()`, `count()`

- Combine grouping with multiple statistics

---

### 👥 Activity: Group by a Single Column

```python
"""
This code groups the dataset by 'Department' and calculates the average salary
for each group using the mean() function.
"""

avg_salary = df.groupby('Department')['Salary'].mean()
print(avg_salary)
```

---

### 📊 Activity: Count Entries in Each Group

```python
"""
This code counts the number of employees in each department using groupby and count().
"""

emp_count = df.groupby('Department')['Name'].count()
print(emp_count)
```

---

### 💰 Activity: Group by Multiple Columns

```python
"""
This code groups the data by both 'Department' and 'Location',
and then sums the 'Bonus' for each group.
"""

bonus_summary = df.groupby(['Department', 'Location'])['Bonus'].sum()
print(bonus_summary)
```

---

### 🔧 Activity: Use Multiple Aggregations

```python
"""
This code calculates both average and maximum salary by department
using the agg() function to apply multiple aggregations.
"""

summary_stats = df.groupby('Department')['Salary'].agg(['mean', 'max'])
print(summary_stats)
```

---

### 📁 Excel File for Practice

📎 Download employee_data_ch6.xlsx

---

### 🧠 Recap

- You grouped data using `groupby()`

- You performed aggregations like count, mean, sum, and max

- You learned to group by single and multiple columns



## 📘 Chapter 7: Merging and Joining DataFrames

---

### 📌 Introduction

Often, data is split across multiple tables—just like different Excel sheets for employees, departments, or salary bands. In such cases, we need to merge or join the data based on a common column.

---

### 🎯 Objectives

By the end of this chapter, you will be able to:

- Understand different types of joins (inner, left, right, outer)

- Combine two DataFrames using `merge()`

- Append rows using `concat()`

- Apply merges similar to SQL joins or Excel VLOOKUP

---

### 🔗 Activity: Merge Two DataFrames (Basic)

```python
"""
This code merges the employee dataset with department details
using a common 'Department' column, similar to a VLOOKUP in Excel.
"""

merged_df = pd.merge(df_emp, df_dept, on='Department', how='inner')
print(merged_df)
```

---

### 🧩 Activity: Left Join

```python
"""
This code performs a left join to retain all employees,
even if some departments don’t have manager information.
"""

merged_left = pd.merge(df_emp, df_dept, on='Department', how='left')
print(merged_left)
```

---

### ➕ Activity: Concatenate Rows

```python
"""
This code combines two DataFrames vertically (row-wise),
like appending new records from another month's dataset.
"""

combined_df = pd.concat([df_jan, df_feb], ignore_index=True)
print(combined_df)
```

---

### 🧱 Activity: Merge on Multiple Columns

```python
"""
This code merges two DataFrames using both 'Department' and 'Location'
to match records more precisely.
"""

merged_multi = pd.merge(df1, df2, on=['Department', 'Location'], how='inner')
print(merged_multi)
```

---

### 📁 Excel Files for Practice

📎 Download employee_master.xlsx  
📎 Download department_info.xlsx

---

### 🧠 Recap

- You used `merge()` to perform inner and left joins

- You combined data from multiple sources

- You appended records using `concat()`

---

## 📘 Chapter 8: Input and Output in Pandas

---

### 📌 Introduction

In any data analysis task, the first and last steps often involve reading data from a file (like Excel or CSV) and saving results to a new file. Pandas provides simple and efficient tools to work with external data sources.

---

### 🎯 Objectives

By the end of this chapter, you will be able to:

- Read data from Excel and CSV files using Pandas

- Save DataFrames into CSV or Excel formats

- Understand file-related parameters like `sheet_name`, `index`, and `header`

---

### 📥 Activity: Read a CSV File

```python
"""
This code reads data from a CSV file using Pandas
and displays the first 5 rows of the DataFrame.
"""

df_csv = pd.read_csv('employee_data_ch6.csv')
print(df_csv.head())
```

---

### 📥 Activity: Read an Excel File

```python
"""
This code reads data from an Excel file into a DataFrame.
"""

df_excel = pd.read_excel('employee_data_ch6.xlsx')
print(df_excel.head())
```

---

### 📤 Activity: Save a DataFrame to CSV

```python
"""
This code saves the DataFrame into a CSV file.
The index (row numbers) are not included in the file.
"""

df_excel.to_csv('processed_data.csv', index=False)
```

---

### 📤 Activity: Save a DataFrame to Excel

```python
"""
This code saves the DataFrame into an Excel file.
"""

df_excel.to_excel('processed_data.xlsx', index=False)
```

---

### 🛠️ Optional Parameters to Know

| Parameter      | Description                                         |
| -------------- | --------------------------------------------------- |
| `index=False`  | Prevents Pandas from writing row numbers to file    |
| `sheet_name`   | Allows naming a specific Excel sheet during writing |
| `header=False` | Skips writing column names (usually avoided)        |

---

### 📁 Sample Files for Practice

📎 Download employee_data_ch6.csv  
📎 Download employee_data_ch6.xlsx

---

### 🧠 Recap

- You learned to load data from Excel and CSV files

- You explored saving DataFrames using `to_csv()` and `to_excel()`

- You reviewed common parameters for file I/O

---

## 📘 Chapter 9: Exploratory Data Analysis (EDA)

---

### 📌 Introduction

Once your data is clean and structured, the next step is to explore it to uncover patterns, trends, and insights. This process is called Exploratory Data Analysis (EDA).

---

### 🎯 Objectives

By the end of this chapter, you will be able to:

- Summarize data using key statistics

- Use `value_counts()` and `crosstab()` for categorical insights

- Identify correlations between numerical variables

- Create basic visualizations using Pandas

---

### 📊 Activity: Summary Statistics

```python
"""
This code provides summary statistics for numerical columns
using the describe() function in Pandas.
"""

print(df.describe())
```

---

### 📋 Activity: Frequency Count of Categories

```python
"""
This code counts the number of entries in each department.
Useful for understanding the distribution of categorical data.
"""

print(df['Department'].value_counts())
```

---

### 🔀 Activity: Cross Tabulation

```python
"""
This code creates a cross-tab that shows how many Seniors and Juniors
exist in each department.
"""

pd.crosstab(df['Department'], df['Level'])
```

---

### 📈 Activity: Correlation Matrix

```python
"""
This code calculates correlation between numerical columns
like Salary and Bonus.
"""

print(df[['Salary', 'Bonus']].corr())
```

---

### 📉 Activity: Simple Visualization

```python
"""
This code creates a bar chart showing average salary by department.
"""

df.groupby('Department')['Salary'].mean().plot(kind='bar', title='Average Salary by Department')
```

---

### 📁 Excel File for Practice

📎 Download employee_data_ch9.xlsx

---

### 🧠 Recap

- You summarized your dataset using describe(), value_counts(), and crosstab()

- You calculated correlations between numerical fields

- You created quick bar charts using Pandas

---

## 📘 Chapter 10: Pandas in Action – Crash Course

---

### 📌 Introduction

This final chapter walks through real-world mini-projects that simulate how Pandas is used in managerial decision-making. Each scenario builds on the concepts learned so far.

---

### 🎯 Objectives

By the end of this chapter, you will be able to:

- Use Pandas to perform real-world data analysis tasks

- Apply cleaning, transformation, grouping, filtering, and visualization

- Interpret results for managerial decision-making

---

### 🧩 Mini-Project 1: HR Manager – Employee Attrition Insights

```python
"""
Filter employees who joined before 2019 and group by department.
"""

at_risk = df[df['Joining_Year'] < 2019]
summary = at_risk.groupby('Department')['Name'].count()
print(summary)
```

---

### 🧩 Mini-Project 2: Finance – Total Bonus by Location

```python
"""
Calculate total bonus paid by location.
"""

total_bonus = df.groupby('Location')['Bonus'].sum()
print(total_bonus)
```

---

### 🧩 Mini-Project 3: Operations – Staffing Level Overview

```python
"""
Show staffing level by department using cross-tab.
"""

pd.crosstab(df['Department'], df['Level'])
```

---

### 🧩 Mini-Project 4: Reporting – Export Clean Summary

```python
"""
Export only Name, Department, and Level columns to Excel.
"""

export_df = df[['Name', 'Department', 'Level']]
export_df.to_excel('clean_summary_report.xlsx', index=False)
```

---

### 📁 Final Excel File

📎 Download clean_summary_report.xlsx

---

### 🧠 Recap

- You applied Pandas skills in real-world problem solving

- You practiced filtering, aggregation, exporting, and reporting

- You created clean outputs ready for managerial use
