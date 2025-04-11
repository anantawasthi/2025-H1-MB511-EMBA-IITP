

# ✅ **Activity 6: Missing Value Detection and Imputation**

---

### 🧭 1. Activity Introduction

Real-world datasets are rarely complete. Missing data can arise due to:

- Process gaps (e.g., skipped engagement surveys)

- Business logic (e.g., resignation date only available if resigned)

- Human behavior (e.g., refusal to disclose income)

In this activity, we will:

- Identify **where and how much data is missing**

- Diagnose **why** data is missing (MCAR, MAR, MNAR)

- Choose appropriate imputation or handling strategies

- Flag missingness if meaningful for modeling

---

### 💻 2. Python Code — Missing Value Diagnosis & Treatment

```python
import missingno as msno
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Check number and % of missing values
print("📋 Missing value summary:\n")
missing_counts = df.isnull().sum()
missing_percent = df.isnull().mean() * 100
missing_df = pd.DataFrame({'Missing_Count': missing_counts, 'Missing_%': missing_percent})
print(missing_df[missing_df['Missing_Count'] > 0].round(1))

# Step 2: Visualize missing values
msno.matrix(df)
plt.title("🔍 Missing Value Matrix", fontsize=14)
plt.show()

msno.heatmap(df)
plt.title("🔍 Missing Value Correlation Heatmap", fontsize=14)
plt.show()

# Step 3: Investigate where Engagement_Score is missing
print("\n🧠 Check if missing engagement score correlates with attrition:\n")
print(pd.crosstab(df['Engagement_Score'].isna(), df['Resigned'], normalize='index') * 100)

# Step 4: Impute Engagement_Score using department-wise median (MAR assumption)
df['Engagement_Score_Imputed'] = df['Engagement_Score']  # Create a copy to preserve original

# Group-wise imputation
df['Engagement_Score_Imputed'] = df.groupby('Department')['Engagement_Score_Imputed']\
                                   .transform(lambda x: x.fillna(x.median()))

# Step 5: Add missing flag for modeling (optional)
df['Engagement_Missing_Flag'] = df['Engagement_Score'].isna().astype(int)
```

---

### 📊 3. Results (Sample Output)

#### ✅ Missing Summary:

| Variable         | Missing Count | Missing %                      |
| ---------------- | ------------- | ------------------------------ |
| Engagement_Score | 101           | 10.1%                          |
| Resignation_Date | ~720          | 72% (expected if not resigned) |

#### ✅ Crosstab:

| Missing Engagement | Resigned = Yes (%) | Resigned = No (%) |
| ------------------ | ------------------ | ----------------- |
| True               | 41.2               | 58.8              |
| False              | 27.4               | 72.6              |

> Suggests engagement is **not missing at random** → possibly **MAR** or **MNAR**

---

### 🧠 4. Results Discussion

| Insight                                    | Interpretation                                                    |
| ------------------------------------------ | ----------------------------------------------------------------- |
| **Engagement missing ~10%**                | Not MCAR — looks correlated with resignation behavior             |
| **Imputation by Department Median**        | Best option when you suspect MAR — department drives work culture |
| **Flag retained for modeling**             | Helps models learn from missingness patterns (important if MNAR)  |
| **Resignation Date missing only for 'No'** | Expected business logic — do not impute or drop                   |

> ✅ This method maintains data integrity and keeps modeling fair.

---

### 🧪 Summary of Strategy Used

| Variable         | Type    | Missingness Type    | Strategy                      |
| ---------------- | ------- | ------------------- | ----------------------------- |
| Engagement_Score | Numeric | MAR (possibly MNAR) | Department-wise median + flag |
| Resignation_Date | Date    | Not Applicable      | Leave as-is (logical missing) |

---


