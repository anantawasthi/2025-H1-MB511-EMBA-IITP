

# ✅ **Activity 3.1: Descriptive Exploratory Data Analysis (Univariate)**

---

### 🧭 1. Activity Introduction

In univariate analysis, we study **one variable at a time** to understand:

- Its **central tendency** (mean, median, mode)

- Its **spread or variability** (min, max, standard deviation, range, IQR)

- The **distribution** (skewed? uniform? outliers?)

- The **frequency of categories** (for non-numeric variables)

This step helps identify:

- Strange values

- Variables with little or no variation

- Initial business interpretations

We'll categorize variables into:

- **Numerical Variables**: Age, Salary, Engagement Score, Tenure

- **Categorical Variables**: Department, Gender, Resigned

---

### 💻 2. Python Code: Descriptive EDA for All Variables

```python
# Step 1: Identify numeric and categorical columns
numeric_cols = ['Age', 'Tenure_Months', 'Salary', 'Engagement_Score']
categorical_cols = ['Department', 'Gender', 'Resigned']

# Step 2: Descriptive summary for numeric columns
print("📊 Descriptive statistics for numeric variables:\n")
print(df[numeric_cols].describe().T)  # Transposed for readability

# Step 3: Additional spread metrics (Range and IQR)
print("\n📏 Additional spread metrics (Range and IQR):\n")
for col in numeric_cols:
    col_range = df[col].max() - df[col].min()
    iqr = df[col].quantile(0.75) - df[col].quantile(0.25)
    print(f"{col} → Range: {col_range}, IQR: {iqr}")

# Step 4: Descriptive frequency for categorical variables
print("\n📋 Frequency distribution of categorical variables:\n")
for col in categorical_cols:
    print(f"\n{col} value counts:\n{df[col].value_counts()}")
    print(f"\n{col} value counts (%):\n{df[col].value_counts(normalize=True) * 100}")
```

---

### 📊 3. Results (Sample Summary)

#### ✅ Numeric Variable Summary:

| Variable         | Mean  | Std   | Min   | 25%   | 50% (Median) | 75%   | Max   |
| ---------------- | ----- | ----- | ----- | ----- | ------------ | ----- | ----- |
| Age              | 35.4  | 9.1   | 22    | 28    | 34           | 43    | 59    |
| Tenure_Months    | 38.7  | 29.5  | 1     | 12    | 36           | 60    | 119   |
| Salary           | 55200 | 10020 | 30000 | 47500 | 55000        | 63000 | 95000 |
| Engagement_Score | 5.9   | 1.5   | 1.2   | 4.8   | 5.9          | 7.1   | 10    |

> *Engagement Score has some missing values — we'll handle that in Activity 6.*

---

#### ✅ Categorical Variable Frequency (Examples):

**Department**:

```
Sales         36.2%
IT            30.4%
HR            15.1%
Finance       9.8%
Operations    8.5%
```

**Resigned**:

```
No     71.5%
Yes    28.5%
```

> Interpretation: Resigned column shows ~28% attrition rate, which aligns with earlier synthetic logic.

---

### 🧠 4. Results Discussion

#### ✅ Numeric Variables:

| Variable          | Insight                                                                        |
| ----------------- | ------------------------------------------------------------------------------ |
| **Age**           | Normal distribution, no unusual min/max. Median = 34. Majority are mid-career. |
| **Tenure_Months** | Long-tailed. Median = 36. Some very new and very long-term employees.          |
| **Salary**        | Slight right skew. Median = ₹55K. Range: ₹30K–₹95K.                            |
| **Engagement**    | Range = 1.2 to 10. Distribution is broad, possible low-engagement clusters.    |

#### ✅ Categorical Variables:

| Variable       | Insight                                                                          |
| -------------- | -------------------------------------------------------------------------------- |
| **Department** | Sales + IT dominate (66% of workforce). Ensure fair department-wise comparisons. |
| **Gender**     | Reasonably balanced sample — no major skew.                                      |
| **Resigned**   | Attrition is significant (almost 3 in 10). A valid use case for deeper analysis. |


