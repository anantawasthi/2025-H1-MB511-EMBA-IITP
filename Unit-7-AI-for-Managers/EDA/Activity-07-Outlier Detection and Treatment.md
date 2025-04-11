# ✅ **Activity 7: Outlier Detection and Treatment**

---

### 🧭 1. Activity Introduction

Outliers are values that are **significantly different from the rest** of the dataset. They may indicate:

- **Errors** (e.g., wrong data entry)

- **Legitimate but rare events** (e.g., a VP’s salary)

- **Early signals of risk** (e.g., very low engagement before resignation)

In this activity, we will:

- Detect outliers using **visual (boxplots)** and **statistical methods (IQR and Z-score)**

- Decide whether to **keep, cap, transform, or exclude**

- Apply context-aware treatment for Salary, Tenure, and Engagement

---

### 💻 2. Python Code — Detect & Treat Outliers

```python
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore

# Step 1: Visual Inspection using Boxplots
num_cols = ['Age', 'Salary', 'Tenure_Months', 'Engagement_Score_Imputed']
for col in num_cols:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df[col], color='salmon')
    plt.title(f"📦 Boxplot of {col}")
    plt.show()

# Step 2: IQR Method for Outlier Detection
def detect_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = data[(data[column] < lower) | (data[column] > upper)]
    return outliers

# Detect and count outliers
print("🔍 Outlier count based on IQR:\n")
for col in ['Salary', 'Tenure_Months', 'Engagement_Score_Imputed']:
    outliers = detect_outliers_iqr(df, col)
    print(f"{col}: {len(outliers)} outliers")

# Step 3: Cap outliers (Winsorization)
df['Salary_Capped'] = df['Salary'].clip(lower=df['Salary'].quantile(0.01),
                                        upper=df['Salary'].quantile(0.99))

df['Tenure_Capped'] = df['Tenure_Months'].clip(lower=df['Tenure_Months'].quantile(0.01),
                                               upper=df['Tenure_Months'].quantile(0.99))
```

---

### 📊 3. Results (Sample Output)

#### ✅ IQR Outlier Count:

```
Salary: 18 outliers
Tenure_Months: 22 outliers
Engagement_Score_Imputed: 11 outliers
```

#### ✅ Visuals:

- **Boxplot for Salary** → long right tail; outliers above ₹90K

- **Boxplot for Tenure** → some employees with 100+ months

- **Engagement** → lower outliers more prominent (likely at-risk)

#### ✅ Treatment:

- **Capped** Salary and Tenure at 1st and 99th percentiles

- Retained original values for backup analysis

---

### 🧠 4. Results Discussion

| Variable       | Insight                        | Treatment                                   |
| -------------- | ------------------------------ | ------------------------------------------- |
| **Salary**     | Right-skewed with high earners | Winsorized to 1%–99% range                  |
| **Tenure**     | Long right tail                | Capped to reduce influence of edge cases    |
| **Engagement** | Lower bound outliers (<2.5)    | Retained; these are meaningful for modeling |
| **Age**        | Normal; no extreme outliers    | No action taken                             |

> ✅ Outlier treatment should **preserve business meaning** — not just normalize numbers.

---

### 🧪 Summary of Our Approach

| Method Used       | Applied To     | Action Taken                   |
| ----------------- | -------------- | ------------------------------ |
| Boxplots          | All numerics   | Visual spotting                |
| IQR Rule          | Salary, Tenure | Counted outliers               |
| Winsorization     | Salary, Tenure | Capped extremes (1st–99th pct) |
| Retain low scores | Engagement     | Meaningful signal, kept intact |

---
