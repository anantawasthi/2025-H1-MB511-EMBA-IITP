## 📘 Chapter 9: Exploratory Data Analysis (EDA)

---

### 📌 Introduction

Once your data is clean and structured, the next step is to **explore it** to uncover patterns, trends, and insights. This process is called **Exploratory Data Analysis (EDA)** and is a key part of any data-driven decision-making.

Pandas provides powerful tools to:

- Understand distributions

- Identify correlations

- Spot unusual data

- Generate quick summaries

This chapter introduces basic EDA tools, perfect for business users and managers who need to interpret reports or dashboards.

---

### 🎯 Objectives

By the end of this chapter, you will be able to:

- Summarize data using key statistics

- Use `value_counts()` and `crosstab()` for categorical insights

- Identify correlations between numerical variables

- Create basic visualizations using Pandas

---

### 📊 9.2 Activity: Summary Statistics

#### 📝 Description:

Let’s generate descriptive statistics (like mean, median, count, etc.) for our dataset.

```python
"""
This code provides summary statistics for numerical columns
using the describe() function in Pandas.
"""

print(df.describe())
```

---

### 📋 9.3 Activity: Frequency Count of Categories

#### 📝 Description:

We can count how many employees belong to each department using `value_counts()`.

```python
"""
This code counts the number of entries in each department.
Useful for understanding the distribution of categorical data.
"""

print(df['Department'].value_counts())
```

---

### 🔀 9.4 Activity: Cross Tabulation

#### 📝 Description:

Use `crosstab()` to analyze the relationship between two categorical columns—like Department and Level.

```python
"""
This code creates a cross-tab that shows how many Seniors and Juniors
exist in each department.
"""

pd.crosstab(df['Department'], df['Level'])
```

---

### 📈 9.5 Activity: Correlation Matrix

#### 📝 Description:

Let’s see how numeric columns (like Salary and Bonus) relate to each other.

```python
"""
This code calculates correlation between numerical columns
to help identify positive or negative relationships.
"""

print(df[['Salary', 'Bonus']].corr())
```

---

### 📉 9.6 Activity: Simple Visualization

#### 📝 Description:

You can create simple plots with Pandas without any extra libraries.

```python
"""
This code creates a bar chart showing average salary by department.
"""

df.groupby('Department')['Salary'].mean().plot(kind='bar', title='Average Salary by Department')
```

> 📝 *Note: Add `%matplotlib inline` if using Jupyter Notebook.*


