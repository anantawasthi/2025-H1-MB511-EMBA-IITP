

## 📘 Chapter 6: Grouping and Aggregation

---

### 📌 Introduction

In business settings, you often need to answer questions like:

- What is the **average salary per department**?

- How many employees joined **each year**?

- What is the **total bonus payout by location**?

Pandas makes it very easy to **group data** and then **apply aggregation functions** (like sum, mean, count) to each group. This technique is extremely powerful and forms the backbone of reporting and dashboarding.

---

### 🎯 Objectives

By the end of this chapter, you will be able to:

- Group rows based on a column (e.g., Department)

- Apply aggregation functions like `sum()`, `mean()`, `count()`

- Combine grouping with multiple statistics

- Interpret grouped summaries for decision-making

---

### 👥 6.2 Activity: Group by a Single Column

#### 📝 Description:

Let’s group employees by **Department** and calculate the average salary.

```python
"""
This code groups the dataset by 'Department' and calculates the average salary
for each group using the mean() function.
"""

avg_salary = df.groupby('Department')['Salary'].mean()
print(avg_salary)
```

---

### 📊 6.3 Activity: Count Entries in Each Group

#### 📝 Description:

Let’s count how many employees are there in each department.

```python
"""
This code counts the number of employees in each department using groupby and count().
"""

emp_count = df.groupby('Department')['Name'].count()
print(emp_count)
```

---

### 💰 6.4 Activity: Group by Multiple Columns

#### 📝 Description:

Let’s analyze the **total bonus** paid by both **Department** and **Location**.

```python
"""
This code groups the data by both 'Department' and 'Location',
and then sums the 'Bonus' for each group.
"""

bonus_summary = df.groupby(['Department', 'Location'])['Bonus'].sum()
print(bonus_summary)
```

---

### 🔧 6.5 Activity: Use Multiple Aggregations

#### 📝 Description:

We can use `.agg()` to apply **multiple statistics** on the same group. For example, both the average and maximum salary by department.

```python
"""
This code calculates both average and maximum salary by department
using the agg() function to apply multiple aggregations.
"""

summary_stats = df.groupby('Department')['Salary'].agg(['mean', 'max'])
print(summary_stats)
```


