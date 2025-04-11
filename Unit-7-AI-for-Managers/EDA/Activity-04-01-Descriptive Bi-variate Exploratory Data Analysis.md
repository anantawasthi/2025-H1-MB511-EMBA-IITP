

# ✅ **Activity 4.1: Descriptive Bi-variate Exploratory Data Analysis**

---

### 🧭 1. Activity Introduction

Univariate analysis shows how variables behave in isolation, but **bi-variate analysis helps uncover connections** between two variables:

- Does salary increase with age?

- Is attrition higher in certain departments?

- Do engagement scores differ by gender or department?

We’ll use **group-wise summaries** to compare:

- Numeric ↔ Categorical (e.g., Salary across Departments)

- Categorical ↔ Categorical (e.g., Resigned across Genders)

- Numeric ↔ Numeric (e.g., Age vs Salary correlation)

---

### 💻 2. Python Code – Descriptive Comparisons Across Pairs

```python
# Step 1: Group-wise summary: Salary, Engagement, Tenure by Department
print("📊 Average metrics by Department:\n")
dept_summary = df.groupby("Department")[['Salary', 'Tenure_Months', 'Engagement_Score']].mean().round(2)
print(dept_summary)

# Step 2: Resignation rate by Department
print("\n📉 Resignation Rate by Department:\n")
resignation_rate = df.groupby("Department")['Resigned'].value_counts(normalize=True).unstack().fillna(0) * 100
print(resignation_rate.round(1))

# Step 3: Cross-tab: Gender vs Resigned
print("\n📋 Cross-tab of Gender and Resigned (%):\n")
gender_attrition = pd.crosstab(df['Gender'], df['Resigned'], normalize='index') * 100
print(gender_attrition.round(1))

# Step 4: Correlation matrix of numeric variables
print("\n🔗 Correlation between numeric variables:\n")
correlation_matrix = df[['Age', 'Tenure_Months', 'Salary', 'Engagement_Score']].corr()
print(correlation_matrix.round(2))
```

---

### 📊 3. Results (Sample Output)

#### ✅ Summary by Department

| Department | Salary (₹) | Tenure (months) | Engagement Score |
| ---------- | ---------- | --------------- | ---------------- |
| Sales      | 53,100     | 32.4            | 5.3              |
| IT         | 57,800     | 41.7            | 6.4              |
| HR         | 49,200     | 36.1            | 6.0              |

#### ✅ Resignation Rate by Department

| Department | Yes (%) | No (%) |
| ---------- | ------- | ------ |
| Sales      | 33.2    | 66.8   |
| IT         | 18.1    | 81.9   |
| HR         | 25.0    | 75.0   |

#### ✅ Gender vs Resigned

| Gender | Yes (%) | No (%) |
| ------ | ------- | ------ |
| F      | 26.7    | 73.3   |
| M      | 29.8    | 70.2   |

#### ✅ Correlation Matrix

|                  | Age | Tenure_Months | Salary | Engagement_Score |
| ---------------- | --- | ------------- | ------ | ---------------- |
| Age              | 1.0 | 0.63          | 0.45   | 0.10             |
| Tenure_Months    |     | 1.0           | 0.51   | 0.15             |
| Salary           |     |               | 1.0    | 0.18             |
| Engagement_Score |     |               |        | 1.0              |

---

### 🧠 4. Results Discussion

| Finding                                             | Interpretation                                            |
| --------------------------------------------------- | --------------------------------------------------------- |
| **Sales has lowest engagement + highest attrition** | Intervention needed in Sales team onboarding, environment |
| **IT has highest salary + lowest attrition**        | Compensation may be working as a retention lever          |
| **Women have slightly lower resignation rates**     | Possible early indicator of retention resilience          |
| **Tenure and Age are correlated (0.63)**            | Older employees tend to stay longer                       |
| **Salary correlates with both Age and Tenure**      | Logical: more experienced employees earn more             |
| **Engagement has low correlation with salary**      | Engagement may be non-monetary in nature                  |

---


