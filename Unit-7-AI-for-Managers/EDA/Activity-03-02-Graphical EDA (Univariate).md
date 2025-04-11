

# ✅ **Activity 3.2: Graphical EDA (Univariate)**

---

### 🧭 1. Activity Introduction

While descriptive statistics give a summary, **visualizations reveal the shape, symmetry, outliers, and modality** (e.g., uni-modal, bimodal) of the data.

This activity uses different charts to analyze:

- **Numerical variables** → with histograms, box plots, KDE plots

- **Categorical variables** → with bar plots

We’ll focus on:

- Detecting **skewness**

- Identifying **gaps and clusters**

- Spotting **outliers visually**

---

### 💻 2. Python Code: Visual EDA for Each Variable

```python
# Import necessary visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Set default aesthetics for plots
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 5)

# Define numeric and categorical columns
numeric_cols = ['Age', 'Tenure_Months', 'Salary', 'Engagement_Score']
categorical_cols = ['Department', 'Gender', 'Resigned']

# Visualize numerical variables using histogram + KDE + boxplot
for col in numeric_cols:
    plt.figure(figsize=(14, 5))

    # Histogram + KDE
    plt.subplot(1, 2, 1)
    sns.histplot(df[col], kde=True, bins=30, color='skyblue')
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")

    # Boxplot
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df[col], color='lightcoral')
    plt.title(f"Boxplot of {col}")
    plt.xlabel(col)

    plt.tight_layout()
    plt.show()

# Visualize categorical variables using count plots
for col in categorical_cols:
    plt.figure(figsize=(8, 4))
    sns.countplot(data=df, x=col, palette='Set2', order=df[col].value_counts().index)
    plt.title(f"Count Plot of {col}")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.xticks(rotation=30)
    plt.show()
```

---

### 📊 3. Results

#### ✅ What You’ll See:

- **Age**: Normal-like curve, centered around mid-30s

- **Tenure_Months**: Long tail — some stay >100 months

- **Salary**: Slight right skew — some high earners pull the tail

- **Engagement_Score**: Wide spread; some clusters between 4 and 7

#### ✅ Boxplots:

- Help highlight **outliers** in salary and tenure

- Give a clean visual of the **IQR (Interquartile Range)**

#### ✅ Categorical Count Plots:

- **Sales and IT** have higher counts → focus areas

- **Gender** is relatively balanced

- **Resigned** shows significant churn (bar for "Yes" visible, but lower)

---

### 🧠 4. Results Discussion

| Visual Insight                     | Interpretation                                                            |
| ---------------------------------- | ------------------------------------------------------------------------- |
| Salary histogram right-skewed      | Some employees earn disproportionately more → validate in outlier section |
| Tenure boxplot shows outliers      | Some very senior employees — possible retention anchors                   |
| Engagement spread is wide          | Suggests varying sentiment across workforce → cluster potential           |
| Sales dominates headcount          | Retention programs may need to target this group first                    |
| Resigned = Yes visible but smaller | Confirms attrition is ~28%, visually digestible                           |

> 🔍 **Key Takeaway**: Visual EDA adds **pattern recognition** that numbers alone miss. It brings to light the *shapes* of distributions and supports deeper storytelling.


