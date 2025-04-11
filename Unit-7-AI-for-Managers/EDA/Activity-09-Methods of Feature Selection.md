

Here’s the fully revised, book-style version:

---

# ✅ **Activity 9: Methods of Feature Selection**

**(Including Weight of Evidence and Information Value)**

---

### 🧭 1. Activity Introduction

After creating new features, it's essential to evaluate which of them actually **influence the target variable** (in our case, `Resigned_Flag`).

Why feature selection matters:

- Improves model **efficiency** and **generalizability**

- Removes redundant or irrelevant variables

- Enhances **explainability** of results

- Enables **cleaner business insights**

We’ll explore two major strategies:

- **General-purpose feature selection** using:
  
  - Correlation heatmaps (for redundancy)
  
  - Mutual Information (for importance)

- **Interpretable modeling prep** using:
  
  - Weight of Evidence (WoE)
  
  - Information Value (IV)

---

## 🧪 2. Feature Selection with Correlation & Mutual Information

---

### 💻 Code Block 1: Correlation & MI

```python
from sklearn.feature_selection import mutual_info_classif
import seaborn as sns
import matplotlib.pyplot as plt

# Define candidate features and target
feature_cols = [
    'Age', 'Tenure_Capped', 'Salary_Capped',
    'Engagement_Score_Imputed', 'Salary_Log',
    'Salary_per_Month_of_Service', 'At_Risk'
]
X = df[feature_cols]
y = df['Resigned_Flag']

# Correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(X.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("🔗 Correlation Heatmap")
plt.show()

# Mutual Information
mi_scores = mutual_info_classif(X.fillna(0), y)
mi_df = pd.DataFrame({'Feature': feature_cols, 'MI_Score': mi_scores})
mi_df.sort_values(by='MI_Score', ascending=False, inplace=True)

# Plot MI scores
plt.figure(figsize=(8, 5))
sns.barplot(data=mi_df, y='Feature', x='MI_Score', palette='Blues_r')
plt.title("📈 Mutual Information Scores")
plt.xlabel("Score (0–1)")
plt.ylabel("Feature")
plt.show()
```

---

### 📊 Sample Results:

| Feature                     | MI Score |
| --------------------------- | -------- |
| Engagement_Score_Imputed    | 0.127    |
| At_Risk                     | 0.092    |
| Tenure_Capped               | 0.066    |
| Salary_per_Month_of_Service | 0.049    |
| Salary_Log                  | 0.031    |
| Age                         | 0.019    |
| Salary_Capped               | 0.011    |

> 🔍 High MI means the variable carries useful signal about `Resigned_Flag`.

---

### ✅ Interpretation:

- **Keep**: Engagement, At_Risk, Tenure, Salary_log

- **Drop or combine**: Highly correlated ones (Salary_Capped vs Salary_Log)

- **Optional**: Age, Salary per month (include for explainability)

---

## 📊 3. Feature Selection Using WoE and IV

---

### 🧭 Introduction

**Weight of Evidence (WoE)** transforms categorical or binned numeric variables into numeric values that reflect how well they **differentiate the target classes** (Resigned = Yes vs No).  
**Information Value (IV)** summarizes this separation into a single score.

| IV Range   | Interpretation    |
| ---------- | ----------------- |
| < 0.02     | Not predictive    |
| 0.02 – 0.1 | Weak predictor    |
| 0.1 – 0.3  | Medium            |
| 0.3 – 0.5  | Strong            |
| > 0.5      | Suspiciously good |

---

### 💻 Code Block 2: Using `optbinning` for IV Calculation

```python
from optbinning import OptimalBinning

# Define variables to bin
iv_features = ['Engagement_Score_Imputed', 'Tenure_Capped', 'Salary_Log']
target = df['Resigned_Flag']

# Loop over variables to get IV
for feature in iv_features:
    X = df[feature]
    optb = OptimalBinning(name=feature, dtype="numerical", target_dtype="binary")
    optb.fit(X, target)
    iv = optb.information_value_
    print(f"📌 {feature}: IV = {iv:.3f}")
```

---

### 📊 Sample IV Output:

| Feature                  | IV Score | Interpretation   |
| ------------------------ | -------- | ---------------- |
| Engagement_Score_Imputed | 0.345    | Strong predictor |
| Tenure_Capped            | 0.218    | Medium strength  |
| Salary_Log               | 0.098    | Weak/moderate    |

> 🧠 These values give you **quantitative evidence** for feature usefulness — especially for interpretable models like logistic regression.

---

## 🧠 4. Results Summary and Final Feature Decisions

| Feature                  | Correlation        | MI Score | IV Score | Final Verdict                          |
| ------------------------ | ------------------ | -------- | -------- | -------------------------------------- |
| Engagement_Score_Imputed | Moderate           | 0.127    | 0.345    | ✅ Strong keep                          |
| At_Risk (engineered)     | –                  | 0.092    | –        | ✅ Keep                                 |
| Tenure_Capped            | Low                | 0.066    | 0.218    | ✅ Keep                                 |
| Salary_Log               | High (with Salary) | 0.031    | 0.098    | ✅ Keep                                 |
| Salary_Capped            | Redundant          | 0.011    | –        | ❌ Drop                                 |
| Salary_per_Month         | Medium corr        | 0.049    | –        | Optional                               |
| Age                      | Weak               | 0.019    | –        | ❌ Drop or keep only for interpretation |

---

### ✨ Utility Recap:

| Method      | Best For                               |
| ----------- | -------------------------------------- |
| Correlation | Removing redundant variables           |
| Mutual Info | Highlighting important predictors      |
| WoE + IV    | Model explainability + binning insight |

---

### ✅ Final Feature Set (Recommended for Modeling)

```python
selected_features = [
    'Engagement_Score_Imputed',
    'At_Risk',
    'Tenure_Capped',
    'Salary_Log'
]
```

---


