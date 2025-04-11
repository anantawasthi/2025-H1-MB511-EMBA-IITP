# ✅ **Activity 4.3: Statistical Relationship Testing (Bi-variate)**

---

### 🧭 1. Activity Introduction

Once we’ve **seen** relationships, the next step is to **test** whether those relationships are statistically significant.

In this activity, we will:

- Use **correlation coefficients** for numeric ↔ numeric

- Apply **independent t-tests** for numeric ↔ binary categorical

- Run **Chi-square tests** for categorical ↔ categorical variables

These help answer:

- Do resigned employees have significantly lower engagement?

- Does department influence attrition?

- Are salary and tenure truly correlated?

---

### 💻 2. Python Code — Statistical Relationship Testing

```python
from scipy.stats import pearsonr, ttest_ind, chi2_contingency

# 1. Correlation Test: Salary vs Tenure
print("🔗 Correlation Test: Salary vs Tenure")
salary_tenure_corr, salary_tenure_p = pearsonr(df['Salary'], df['Tenure_Months'])
print(f"  Pearson r = {salary_tenure_corr:.2f}, p-value = {salary_tenure_p:.4f}")
if salary_tenure_p < 0.05:
    print("  ✅ Significant positive correlation.\n")
else:
    print("  ❌ Not statistically significant.\n")

# 2. T-test: Engagement Score vs Resigned
print("📉 T-Test: Engagement Score for Resigned vs Stayed")
engaged_yes = df[df['Resigned'] == 'Yes']['Engagement_Score'].dropna()
engaged_no = df[df['Resigned'] == 'No']['Engagement_Score'].dropna()
t_stat, p_val = ttest_ind(engaged_yes, engaged_no, equal_var=False)  # Welch's t-test
print(f"  t-statistic = {t_stat:.2f}, p-value = {p_val:.4f}")
if p_val < 0.05:
    print("  ✅ Significant difference in engagement between groups.\n")
else:
    print("  ❌ No significant difference.\n")

# 3. Chi-square Test: Department vs Resigned
print("👥 Chi-Square Test: Department vs Attrition")
contingency_table = pd.crosstab(df['Department'], df['Resigned'])
chi2, p_chi, dof, expected = chi2_contingency(contingency_table)
print(f"  Chi2 = {chi2:.2f}, p-value = {p_chi:.4f}")
if p_chi < 0.05:
    print("  ✅ Department is significantly associated with attrition.\n")
else:
    print("  ❌ No significant relationship.\n")
```

---

### 📊 3. Results (Sample Output)

#### ✅ Pearson Correlation (Salary vs Tenure):

```
Pearson r = 0.51, p-value = 0.0000 → ✅ Significant
```

#### ✅ T-Test (Engagement Score by Resigned):

```
t-statistic = -6.28, p-value = 0.0000 → ✅ Significant
```

#### ✅ Chi-square (Department vs Resigned):

```
Chi2 = 26.47, p-value = 0.0002 → ✅ Significant
```

---

### 🧠 4. Results Discussion

| Test                            | Result             | Interpretation                                                       |
| ------------------------------- | ------------------ | -------------------------------------------------------------------- |
| **Salary vs Tenure (r = 0.51)** | Significant        | Tenure is a strong predictor of salary — likely policy-driven        |
| **Engagement by Resignation**   | Highly significant | Lower engagement strongly linked to attrition — invest in monitoring |
| **Department vs Attrition**     | Significant        | Attrition is not random across departments — Sales = hotspot         |

> ✅ These tests provide **statistical backing** to what we’ve seen visually and descriptively.

---


