# ✅ **Activity 2: Examine the Structure of the Dataset**

---

### 🧭 1. Activity Introduction

Before analyzing any data, it's important to understand:

- How many rows and columns are there?

- What are the column names and data types?

- Are there missing values?

- Do the values look sensible?

This activity builds a **mental map** of the dataset and helps you plan how to clean, visualize, and analyze it in later steps.

---

### 💻 2. Python Code (with explanations)

```python
# Step 1: Check the number of rows and columns
print("Shape of the dataset (rows, columns):")
print(df.shape)  # This tells us how many records and fields we have

# Step 2: View column names
print("\nColumn names in the dataset:")
print(df.columns.tolist())  # Shows a list of all variable names

# Step 3: Look at the first few rows of data
print("\nPreview of the first 5 rows:")
print(df.head())  # Gives a sample of the dataset to spot any strange values

# Step 4: View basic info about each column (including data types and non-null counts)
print("\nData types and non-null values for each column:")
print(df.info())  # Checks data types and whether there are missing values

# Step 5: Get a statistical summary of all numeric columns
print("\nSummary statistics for numeric columns:")
print(df.describe())  # Shows count, mean, std, min, max, percentiles
```

---

### 📊 3. Results

When you run this block, here’s the kind of output you’ll observe (summarized):

#### ✅ Shape:

```
(1000, 9)  # 1000 records, 9 columns
```

#### ✅ Columns:

```
['Emp_ID', 'Department', 'Age', 'Gender', 'Tenure_Months', 'Salary', 'Engagement_Score', 'Resigned', 'Resignation_Date']
```

#### ✅ Data Sample (via `head()`):

| Emp_ID | Department | Age | Gender | Tenure_Months | Salary | Engagement_Score | Resigned | Resignation_Date |
| ------ | ---------- | --- | ------ | ------------- | ------ | ---------------- | -------- | ---------------- |
| 2001   | Sales      | 29  | F      | 18            | 48000  | 6.5              | No       | NaT              |

#### ✅ Info:

Shows that:

- `Engagement_Score` and `Resignation_Date` have some missing values

- `Age`, `Tenure_Months`, and `Salary` are numeric

- `Resigned` and `Gender` are categorical (but stored as "object")

#### ✅ Describe:

Summarizes:

- Average salary, age, and tenure

- Range of engagement scores

- Spot any strange min/max values (e.g., salary too low or age too high)

---

### 🧠 4. Results Discussion

This activity helped us discover:

| **Observation**                         | **Interpretation / Action**                            |
| --------------------------------------- | ------------------------------------------------------ |
| 1000 rows × 9 columns                   | Large enough for patterns, small enough for manual EDA |
| Categorical variables as "object"       | We'll need to convert them later for modeling          |
| Some `Engagement_Score` values missing  | We'll investigate why and treat in Activity 6          |
| Some salaries might be unusually high   | Flag for Activity 7: Outlier detection                 |
| Resigned column has clear Yes/No labels | Will be the target variable in future modeling         |


