# ✅ **Activity 5.3: Statistical Multivariate Relationships**

---

### 🧭 1. Activity Introduction

In multivariate analysis, we’re interested in:

- **How multiple variables interact**

- **Whether a third variable modifies the relationship between two others**

- **Which features might combine to influence attrition or engagement**

Here, we’ll apply:

- **Two-way ANOVA** → for interaction effects

- **Multivariate correlation matrix** → for strength and direction

- **Grouped means + standard deviation** → to observe combined influence

---

### 💻 2. Python Code — Statistical Analysis with 3 Variables

```python
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Step 1: Two-way ANOVA: Engagement Score ~ Department + Resigned + Department*Resigned
print("📊 Two-Way ANOVA: Engagement ~ Department * Resigned\n")
anova_data = df.dropna(subset=['Engagement_Score'])  # ANOVA can't handle nulls
model = ols('Engagement_Score ~ C(Department) + C(Resigned) + C(Department):C(Resigned)', data=anova_data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table.round(3))

# Step 2: Expanded correlation matrix (including binary Resigned)
df['Resigned_Flag'] = df['Resigned'].map({'Yes': 1, 'No': 0})
extended_corr = df[['Age', 'Tenure_Months', 'Salary', 'Engagement_Score', 'Resigned_Flag']].corr()
print("\n🔗 Multivariate Correlation Matrix:")
print(extended_corr.round(2))

# Step 3: Grouped Mean Engagement Score by Department & Resigned
print("\n📋 Grouped Mean Engagement Score by Department & Resigned:")
group_means = df.groupby(['Department', 'Resigned'])['Engagement_Score'].agg(['mean', 'std']).round(2)
print(group_means)
```

---

### 📊 3. Results (Sample Output)

#### ✅ Two-Way ANOVA:

| Source                | Sum Sq | df  | F     | PR(>F) |
| --------------------- | ------ | --- | ----- | ------ |
| C(Department)         | 60.20  | 4   | 10.42 | 0.000  |
| C(Resigned)           | 112.87 | 1   | 78.20 | 0.000  |
| Department × Resigned | 18.53  | 4   | 3.21  | 0.012  |
| Residual              | 1392.6 | 983 |       |        |

#### ✅ Extended Correlation Matrix:

|            | Age | Tenure | Salary | Engagement | Resigned_Flag |
| ---------- | --- | ------ | ------ | ---------- | ------------- |
| Age        | 1.0 | 0.63   | 0.45   | 0.10       | -0.12         |
| Tenure     |     | 1.0    | 0.51   | 0.15       | -0.22         |
| Salary     |     |        | 1.0    | 0.18       | -0.17         |
| Engagement |     |        |        | 1.0        | -0.34         |

#### ✅ Grouped Engagement Means:

| Department | Resigned | Mean | Std  |
| ---------- | -------- | ---- | ---- |
| Sales      | Yes      | 5.14 | 1.23 |
| Sales      | No       | 6.12 | 1.06 |
| IT         | Yes      | 6.25 | 1.12 |
| IT         | No       | 6.72 | 0.94 |

---

### 🧠 4. Results Discussion

| Insight                                                               | Interpretation                                                                                          |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **ANOVA: Dept × Resigned interaction is significant**                 | Attrition impacts engagement differently across departments — HR vs Sales vs IT show different patterns |
| **Engagement correlates with Resigned_Flag (r = -0.34)**              | Lower engagement → higher chance of attrition                                                           |
| **Tenure has negative correlation with attrition**                    | Long-term employees are more likely to stay                                                             |
| **Grouped Means** show lowest engagement for resigned Sales employees | Confirms Sales is a high-risk group for disengagement + churn                                           |

---


