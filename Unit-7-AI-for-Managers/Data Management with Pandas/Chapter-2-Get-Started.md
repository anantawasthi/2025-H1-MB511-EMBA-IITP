

## 📘 Chapter 2: Getting Started with Pandas

---

### 🧠 2.1 Installing and Importing Pandas

Although installation might not be required in your learning environment, it's good to know how Pandas is added to a Python project.

```bash
pip install pandas
```

To use Pandas in your Python code, you need to import it:

```python
import pandas as pd
```

We typically use `pd` as a short alias for `pandas`.

---

### 📦 2.2 Core Data Structures in Pandas

Pandas is built around two main data structures:

| Data Structure | Description                                   | Real-World Analogy                |
| -------------- | --------------------------------------------- | --------------------------------- |
| `Series`       | A one-dimensional labeled array               | A single column in an Excel sheet |
| `DataFrame`    | A two-dimensional table with rows and columns | An entire Excel sheet             |

---

### 🛠️ 2.3 Creating a DataFrame

We’ll start with a simple example using synthetic employee data (provided in Excel). But first, let's manually create a DataFrame from a dictionary:

```python
import pandas as pd

# Creating a sample DataFrame manually
data = {
    'Employee': ['Anita', 'Ravi', 'Meena'],
    'Department': ['HR', 'Finance', 'IT'],
    'Salary': [55000, 60000, 58000]
}

df = pd.DataFrame(data)

# View the DataFrame
print(df)
```

---

### 📊 2.4 Loading Data from an Excel File

Let’s use a sample Excel file that mimics a typical HR record.

```python
# Load an Excel file into a DataFrame
df = pd.read_excel('employee_salary_data_ch1.xlsx')

# Show the first few rows
print(df.head())
```

---

### 🧪 2.5 Exploring the Data

Once loaded, you can explore and understand your data using some key functions:

| Function        | Purpose                                        |
| --------------- | ---------------------------------------------- |
| `df.head()`     | Displays the first 5 rows                      |
| `df.tail()`     | Displays the last 5 rows                       |
| `df.shape`      | Returns the number of rows and columns         |
| `df.info()`     | Summary: data types, non-null values, etc.     |
| `df.describe()` | Statistical summary (only for numeric columns) |

#### Example:

```python
# Get summary info
df.info()

# Basic stats
df.describe()
```


