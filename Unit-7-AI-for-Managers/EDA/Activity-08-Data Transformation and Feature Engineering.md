

# ✅ **Activity 8: Data Transformation and Feature Engineering**

---

### 🧭 1. Activity Introduction

**Raw data ≠ useful data.**  
We must convert existing columns or create new ones that reflect *business understanding*, such as:

- Grouping tenure into experience buckets

- Creating a risk flag for disengaged employees

- Transforming skewed variables (e.g., salary)

- Deriving ratios and interaction features

We’ll apply both **data transformation** (to make existing variables more usable) and **feature engineering** (to create new insights).

---

### 💻 2. Python Code — Transform & Engineer Features

```python
import numpy as np
import pandas as pd

# Step 1: Transformations — Log scale for right-skewed variables
df['Salary_Log'] = np.log1p(df['Salary_Capped'])  # log1p handles zeroes safely
df['Tenure_Log'] = np.log1p(df['Tenure_Capped'])

# Step 2: Binning tenure and age into meaningful categories
df['Tenure_Bucket'] = pd.cut(df['Tenure_Capped'],
                              bins=[0, 24, 60, 120],
                              labels=['<2 yrs', '2–5 yrs', '5+ yrs'])

df['Age_Group'] = pd.cut(df['Age'],
                         bins=[20, 30, 40, 50, 65],
                         labels=['20–30', '30–40', '40–50', '50+'])

# Step 3: Feature Engineering — ratios and conditions
df['Salary_per_Month_of_Service'] = (df['Salary'] / (df['Tenure_Months'].replace(0, np.nan))).fillna(0).round(2)

# Step 4: Risk flags
df['At_Risk'] = np.where(
    (df['Engagement_Score_Imputed'] < 5) & (df['Tenure_Capped'] < 24),
    1,
    0
)

# Step 5: Encoding target variable
df['Resigned_Flag'] = df['Resigned'].map({'Yes': 1, 'No': 0})
```

---

### 📊 3. Results (Sample Preview)

| Emp_ID | Age | Salary  | Tenure_Months | Salary_Log | Tenure_Bucket | At_Risk |
| ------ | --- | ------- | ------------- | ---------- | ------------- | ------- |
| 2001   | 27  | ₹48,000 | 18            | 10.78      | <2 yrs        | 1       |
| 2002   | 42  | ₹62,000 | 48            | 11.03      | 2–5 yrs       | 0       |
| 2003   | 35  | ₹55,000 | 6             | 10.91      | <2 yrs        | 1       |

---

### 🧠 4. Results Discussion

| Feature                         | Purpose                         | Example Value | Why It Matters                         |
| ------------------------------- | ------------------------------- | ------------- | -------------------------------------- |
| **Salary_Log**                  | Normalize salary for regression | 10.91         | Removes skew, stabilizes variance      |
| **Tenure_Bucket**               | Group experience logically      | 2–5 yrs       | Helps compare peer groups              |
| **Age_Group**                   | Segment workforce by age        | 30–40         | Useful for generational strategy       |
| **Salary_per_Month_of_Service** | Cost-efficiency metric          | ₹2,500        | Flags expensive short-term hires       |
| **At_Risk**                     | HR risk detection               | 1 (Yes)       | Combines low engagement + early tenure |

---


