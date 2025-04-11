

# ✅ **Activity 3.3: Statistical Properties of Univariate Features**

---

### 🧭 1. Activity Introduction

Here, we evaluate the **distribution shape** of numeric variables using two core statistics:

| Metric       | Meaning                                                             |
| ------------ | ------------------------------------------------------------------- |
| **Skewness** | Measures asymmetry. Positive = right skew, Negative = left skew     |
| **Kurtosis** | Measures tailedness. High = heavy tails/outliers, Low = flat/normal |

We’ll also run:

- **Normality Tests** (Shapiro-Wilk)

- Identify **need for transformations** (e.g., log, sqrt)

---

### 💻 2. Python Code (Statistical Shape Analysis)

```python
from scipy.stats import skew, kurtosis, shapiro

# List of numeric variables to analyze
numeric_cols = ['Age', 'Tenure_Months', 'Salary', 'Engagement_Score']

print("📊 Skewness, Kurtosis, and Normality Tests:\n")
for col in numeric_cols:
    # Drop missing values
    values = df[col].dropna()

    # Compute shape statistics
    col_skew = skew(values)
    col_kurt = kurtosis(values)
    stat, p_value = shapiro(values[:500])  # Shapiro works best < 500 samples

    print(f"📌 {col}")
    print(f"   Skewness: {col_skew:.2f}")
    print(f"   Kurtosis: {col_kurt:.2f}")
    print(f"   Shapiro-Wilk Test p-value: {p_value:.4f}")

    # Interpretation
    if abs(col_skew) > 1:
        print("   ⚠️ Highly skewed distribution.")
    elif abs(col_skew) > 0.5:
        print("   ⚠️ Moderately skewed.")
    else:
        print("   ✅ Fairly symmetric.")

    if p_value < 0.05:
        print("   ❌ Likely not normally distributed (reject H0)")
    else:
        print("   ✅ Likely normal (fail to reject H0)")
    print("-" * 60)
```

---

### 📊 3. Results (Sample)

| Variable         | Skewness | Kurtosis | Shapiro p-value | Normality?        |
| ---------------- | -------- | -------- | --------------- | ----------------- |
| Age              | 0.20     | -0.18    | 0.20            | ✅ Likely normal   |
| Tenure_Months    | 0.85     | 0.65     | 0.001           | ❌ Not normal      |
| Salary           | 1.25     | 1.45     | 0.0004          | ❌ Highly skewed   |
| Engagement_Score | -0.30    | -0.75    | 0.14            | ✅ Close to normal |

---

### 🧠 4. Results Discussion

| Insight                         | Interpretation and Action                                              |
| ------------------------------- | ---------------------------------------------------------------------- |
| **Salary is highly skewed**     | Log transformation may help normalize for modeling                     |
| **Tenure is long-tailed**       | Consider binning or log/sqrt transform                                 |
| **Engagement is nearly normal** | No action needed unless modeling assumptions require perfect normality |
| **Age is symmetric**            | Safe for regression, parametric comparisons                            |
| **Normality test for Salary**   | Rejects H0 → Not normally distributed → prefer non-parametric stats    |

---

> 🧠 *Statistical shape tells us what transformation is appropriate — but business logic tells us if it’s necessary.*

---


