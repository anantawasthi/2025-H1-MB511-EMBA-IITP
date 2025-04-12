

# 🎯 Feature Engineering of Categorical Data

## 🔹 Step 1: Generate Sample Dataset

We'll create a small, synthetic dataset with customer details that includes various types of categorical variables (nominal, ordinal, binary, high-cardinality). This dataset will help us demonstrate all transformation techniques.

---

### 📄 Dataset Preview:

| CustomerID | Gender | MaritalStatus | Education   | City   | ProductType | SubscriptionType | Churn |
| ---------- | ------ | ------------- | ----------- | ------ | ----------- | ---------------- | ----- |
| C001       | Male   | Married       | Graduate    | Delhi  | Internet    | Monthly          | 1     |
| C002       | Female | Single        | High School | Mumbai | Phone       | Yearly           | 0     |
| ...        | ...    | ...           | ...         | ...    | ...         | ...              | ...   |

Includes:

- **Nominal variables** (`City`, `Gender`, `ProductType`)

- **Ordinal variable** (`Education`, `SubscriptionType`)

- **Target variable** (`Churn`) for encoding methods like target mean

---

### 🧪 Python Code: Create the Dataset

```python
"""
Step 1: Create a synthetic dataset with various categorical columns.
This dataset simulates a small telecom-like customer list for demo purposes.
"""

import pandas as pd

# Synthetic dataset with categorical variables
data = {
    'CustomerID': [f'C{str(i).zfill(3)}' for i in range(1, 21)],
    'Gender': ['Male', 'Female'] * 10,
    'MaritalStatus': ['Married', 'Single', 'Divorced', 'Widowed', 'Married'] * 4,
    'Education': ['High School', 'Graduate', 'Postgraduate', 'PhD', 'Graduate'] * 4,
    'City': ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Bangalore'] * 4,
    'ProductType': ['Internet', 'Phone', 'Combo', 'Phone', 'Internet'] * 4,
    'SubscriptionType': ['Monthly', 'Quarterly', 'Yearly', 'Monthly', 'Quarterly'] * 4,
    'Churn': [1, 0, 1, 0, 0] * 4  # Target variable
}

df = pd.DataFrame(data)

# Preview the dataset
print("Sample Dataset:")
print(df.head(10))
```

---

## **Label Encoding**

### 📖 Concept Introduction

**Label Encoding** converts each unique category in a column into a **numeric code** (e.g., "Male" → 1, "Female" → 0). It’s fast and memory-efficient, but **introduces ordinal relationships** which may be misleading for nominal data.

✅ **Use When**:

- The variable has only two categories (binary),

- You're using **tree-based models** (e.g., Random Forest, XGBoost),

- You’re encoding **ordinal variables intentionally**.

🚫 **Avoid When**:

- You’re applying linear models on **nominal** categories.

---

### 🧪 Python Code: Apply Label Encoding

```python
"""
Step 2: Apply Label Encoding
We’ll label encode the binary 'Gender' column and the ordinal 'SubscriptionType' column.
"""

from sklearn.preprocessing import LabelEncoder

# Copy original dataset to preserve structure
df_label_encoded = df.copy()

# Label encode 'Gender' (binary nominal)
le_gender = LabelEncoder()
df_label_encoded['Gender_LE'] = le_gender.fit_transform(df_label_encoded['Gender'])

# Display encoding map
print("Gender Encoding Map:", dict(zip(le_gender.classes_, le_gender.transform(le_gender.classes_))))

# Label encode 'SubscriptionType' with defined order (ordinal)
subscription_order = ['Monthly', 'Quarterly', 'Yearly']
df_label_encoded['SubscriptionType_LE'] = df_label_encoded['SubscriptionType'].apply(
    lambda x: subscription_order.index(x)
)

# Preview result
df_label_encoded[['Gender', 'Gender_LE', 'SubscriptionType', 'SubscriptionType_LE']].head()
```

---

### 📊 Output Interpretation

| Gender | Gender_LE | SubscriptionType | SubscriptionType_LE |
| ------ | --------- | ---------------- | ------------------- |
| Male   | 1         | Monthly          | 0                   |
| Female | 0         | Quarterly        | 1                   |
| Male   | 1         | Yearly           | 2                   |

- `Gender`: Nominal → encoded with LabelEncoder (`0 = Female`, `1 = Male`)

- `SubscriptionType`: Ordinal → manually encoded to reflect plan hierarchy

---

### **One-Hot Encoding**

---

### 📖 Concept Introduction

**One-Hot Encoding** converts each category of a feature into a **separate binary column** (0 or 1). It avoids implying any order and works great for **nominal variables**.

✅ **Use When**:

- Categories are **non-ordinal** (e.g., city, product type),

- You’re using models sensitive to numeric distances (e.g., linear regression, logistic regression).

🚫 **Watch Out**:

- High-cardinality columns → explosion in number of features,

- Can increase **memory usage** and **model complexity**.

---

### 🧪 Python Code: Apply One-Hot Encoding

```python
"""
Step 3: Apply One-Hot Encoding
We'll one-hot encode the 'City' and 'ProductType' columns (nominal features).
"""

# One-hot encode using pandas get_dummies
df_onehot = pd.get_dummies(df_label_encoded, columns=['City', 'ProductType'], prefix=['City', 'Product'])

# Preview resulting columns
print("New columns after One-Hot Encoding:", [col for col in df_onehot.columns if 'City_' in col or 'Product_' in col])

# Display a sample
df_onehot[['City_Delhi', 'City_Mumbai', 'City_Chennai', 'Product_Internet', 'Product_Combo', 'Product_Phone']].head()
```

---

### 📊 Output Interpretation

| City_Delhi | City_Mumbai | City_Chennai | Product_Internet | Product_Combo | Product_Phone |
| ---------- | ----------- | ------------ | ---------------- | ------------- | ------------- |
| 1          | 0           | 0            | 1                | 0             | 0             |
| 0          | 1           | 0            | 0                | 0             | 1             |

- Each category has its **own column**.

- A `1` indicates the category was present for that row.

- Original columns `City` and `ProductType` are now encoded and removed.

---

### **Ordinal Encoding**

---

### 📖 Concept Introduction

**Ordinal Encoding** is used when the categories in a feature have a **natural order** or ranking. For example:

- Education: High School < Graduate < Postgraduate < PhD

- Satisfaction: Low < Medium < High

Unlike label encoding (which is arbitrary for nominal features), **ordinal encoding preserves ranking** relationships.

✅ **Use When**:

- The categories follow a logical order,

- You want to preserve **distance or progression** in meaning.

🚫 **Avoid When**:

- The variable has **no intrinsic order** (e.g., colors, brands).

---

### 🧪 Python Code: Ordinal Encoding for Education

```python
"""
Step 4: Ordinal Encoding
Manually map the education levels to ordered numeric values:
- High School → 0
- Graduate → 1
- Postgraduate → 2
- PhD → 3
"""

# Define ordered list of education levels
education_order = ['High School', 'Graduate', 'Postgraduate', 'PhD']
edu_map = {level: idx for idx, level in enumerate(education_order)}

# Apply mapping to create encoded column
df_onehot['Education_Ordinal'] = df_onehot['Education'].map(edu_map)

# Preview encoded values
df_onehot[['Education', 'Education_Ordinal']].drop_duplicates().sort_values(by='Education_Ordinal')
```

---

### 📊 Output Interpretation

| Education    | Education_Ordinal |
| ------------ | ----------------- |
| High School  | 0                 |
| Graduate     | 1                 |
| Postgraduate | 2                 |
| PhD          | 3                 |

- This encoding **respects the semantic hierarchy** of education levels.

- Now models can understand: PhD > Graduate in terms of value.

---

### **Frequency / Count Encoding**

---

### 📖 Concept Introduction

**Frequency Encoding** (also called Count Encoding) replaces each category with the **number of times it appears** in the dataset. It’s simple, preserves category granularity, and avoids column explosion.

✅ **Use When**:

- You want to reduce high-cardinality features without losing all information,

- You're working with **tree-based models** that can benefit from frequency patterns.

🚫 **Be Cautious**:

- Not great for models sensitive to numerical scale (e.g., logistic regression),

- May **blur distinctions** between categories with similar frequencies.

---

### 🧪 Python Code: Frequency Encoding for MaritalStatus

```python
"""
Step 5: Frequency Encoding
We’ll encode 'MaritalStatus' by replacing each category with its count in the dataset.
"""

# Get value counts and map to the column
marital_counts = df_onehot['MaritalStatus'].value_counts()
df_onehot['MaritalStatus_FE'] = df_onehot['MaritalStatus'].map(marital_counts)

# Show mapping
print("Marital Status → Frequency Map:")
print(marital_counts)

# Preview result
df_onehot[['MaritalStatus', 'MaritalStatus_FE']].drop_duplicates().sort_values(by='MaritalStatus_FE', ascending=False)
```

---

### 📊 Output Interpretation

| MaritalStatus | MaritalStatus_FE |
| ------------- | ---------------- |
| Married       | 8                |
| Single        | 4                |
| Divorced      | 4                |
| Widowed       | 4                |

- Now each row reflects **how common the marital status is**.

- The encoded value indicates **frequency of occurrence**, not category ID.

---

### **Target Mean Encoding (a.k.a. Mean Response Encoding)**

---

### 📖 Concept Introduction

**Target Mean Encoding** replaces a category with the **average value of the target variable (e.g., churn)** for that category.  
For instance, if 60% of customers from "Delhi" churned, then "Delhi" gets encoded as `0.6`.

✅ **Use When**:

- The categorical variable has a strong relationship with the target,

- You're building **tree-based models**, **Bayesian-boosted models**, or **gradient boosting** models.

🚫 **Watch Out**:

- **Target leakage**: encoding must be done only using **training data**,

- Can cause overfitting if not regularized.

---

### 🧪 Python Code: Target Mean Encoding for `City`

```python
"""
Step 6: Target Mean Encoding
We calculate the average churn rate for each city, then map it back to the rows.
NOTE: This is a simplified version (no data split or cross-validation yet).
"""

# Calculate mean churn for each city
city_churn_mean = df_onehot.groupby('City')['Churn'].mean()

# Map average churn rate to original City column
df_onehot['City_TargetMean'] = df_onehot['City'].map(city_churn_mean)

# Show encoding map
print("City → Churn Rate Map:")
print(city_churn_mean)

# Preview output
df_onehot[['City', 'Churn', 'City_TargetMean']].head(10)
```

---

### 📊 Output Interpretation

| City    | Churn | City_TargetMean |
| ------- | ----- | --------------- |
| Delhi   | 1     | 0.75            |
| Mumbai  | 0     | 0.50            |
| Chennai | 1     | 0.50            |

- For each city, we now have a column that represents its **average churn behavior**.

- Models can leverage this to make **behavior-driven predictions**.

⚠️ **Note**: In production ML pipelines, this should be applied using **cross-validation folds or only training data** to avoid leakage.

---

### Grouping Rare Categories

---

### 📖 Concept Introduction

In some columns—especially **high-cardinality** ones—you’ll find categories that occur only once or twice. These "rare labels" can:

- Add **noise** to the model,

- Cause **overfitting** (model memorizes them),

- Lead to **poor generalization**.

**Rare Category Grouping** consolidates these infrequent values into a single label, like `"Other"` or `"Rare"`.

✅ **Use When**:

- A categorical column has **many unique values**,

- You're encoding for **models sensitive to category sparsity**.

---

### 🧪 Python Code: Group Rare Categories in `City`

```python
"""
Step 7: Group Rare Categories
We'll group cities that occur less than a threshold (say < 5%) of total rows into 'Other'.
"""

# Step 1: Calculate frequency (%)
city_freq = df_onehot['City'].value_counts(normalize=True)

# Step 2: Define threshold for rare (e.g., < 5%)
rare_threshold = 0.05

# Step 3: Create mapping
rare_cities = city_freq[city_freq < rare_threshold].index
df_onehot['City_Grouped'] = df_onehot['City'].apply(lambda x: 'Other' if x in rare_cities else x)

# Show before vs after
df_onehot[['City', 'City_Grouped']].drop_duplicates().sort_values(by='City')
```

---

### 📊 Output Interpretation

| City   | City_Grouped |
| ------ | ------------ |
| Delhi  | Delhi        |
| Mumbai | Mumbai       |
| Bhopal | Other        |

- Rare city names like `"Bhopal"` or `"Nagpur"` (if added) would be grouped into `"Other"`.

- Helps models by **reducing noise** and **generalizing better**.

💡 You can apply this technique to **MaritalStatus**, **ProductType**, or any high-cardinality feature.

---

✅ 🎉 **Recap – What We Learned **

| Technique              | Used On           | Purpose                          |
| ---------------------- | ----------------- | -------------------------------- |
| Label Encoding         | `Gender`          | Binary conversion                |
| Ordinal Encoding       | `Education`       | Preserve ranking                 |
| One-Hot Encoding       | `City`, `Product` | Safe for nominal categories      |
| Frequency Encoding     | `MaritalStatus`   | Reduce category volume           |
| Target Mean Encoding   | `City`            | Capture behavioral trends        |
| Rare Category Grouping | `City`            | Generalize low-frequency classes |

---

Excellent! Let’s move into **Part 2: Feature Engineering for Continuous Data** with the same structured approach.

---

# 📘 Feature Engineering of Continuous Data

## 🔹 Create Synthetic Dataset

This dataset simulates customer financial and usage data for a telecom or SaaS business. We'll include:

- Skewed values,

- Outliers,

- Ratios,

- Columns for group-based aggregations.

---

### 📄 Columns to Include:

| CustomerID | MonthlyCharges | TotalCharges | Tenure | DataUsage(GB) | NumLogins | Age | Department |
| ---------- | -------------- | ------------ | ------ | ------------- | --------- | --- | ---------- |

---

### 🧪 Python Code: Generate Synthetic Data

```python
"""
Step 1: Create a synthetic dataset with continuous features.
We'll include some numeric columns and one group variable (Department) for aggregate stats.
"""

import numpy as np
import pandas as pd

np.random.seed(42)

n = 25  # Sample size

df_cont = pd.DataFrame({
    'CustomerID': [f'C{str(i).zfill(3)}' for i in range(1, n+1)],
    'MonthlyCharges': np.random.normal(70, 20, n).round(2),         # Normal distribution
    'TotalCharges': np.random.normal(1500, 400, n).round(2),        # Skewed due to tenure
    'Tenure': np.random.randint(1, 72, n),                          # Months
    'DataUsage(GB)': np.random.exponential(5, n).round(2),         # Right-skewed
    'NumLogins': np.random.poisson(8, n),                          # Count data
    'Age': np.random.randint(21, 60, n),                           # Age of account holder
    'Department': np.random.choice(['Sales', 'Tech', 'Support'], n) # For grouped stats
})

# Recalculate TotalCharges to reflect MonthlyCharges * Tenure + random noise
df_cont['TotalCharges'] = (df_cont['MonthlyCharges'] * df_cont['Tenure'] + np.random.normal(0, 200, n)).round(2)

# Preview
df_cont.head()
```

---

✅ Dataset is ready with features perfect for:

- Log/sqrt transformations,

- Standardization,

- Binning,

- Ratio creation,

- Interaction terms,

- Grouped rolling aggregates.

---

### **Log & Power Transformations**

---

### 📖 Concept Introduction

Many continuous features (like income, usage, or charges) have **right-skewed distributions**, meaning a small number of high values pull the mean upward.  
**Logarithmic and square root transformations** compress large values and stabilize variance, helping models:

- Detect **patterns in smaller ranges**,

- Handle **heteroscedasticity** (unequal variance),

- Improve **normality** assumptions in linear models.

✅ **Use When**:

- Data is **positive-only** and **right-skewed**,

- You need to improve **model convergence or accuracy**.

🚫 **Avoid When**:

- The feature contains **zero or negative values** (handle with shifting),

- The interpretation becomes unclear (e.g., log-transformed age).

---

### 🧪 Python Code: Log and Sqrt Transformations

```python
"""
Step 2: Apply log and square-root transformations to skewed features like:
- 'DataUsage(GB)' → Right-skewed
- 'TotalCharges' → Large range
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Make a copy to preserve original
df_transformed = df_cont.copy()

# Log and Sqrt Transformations
df_transformed['DataUsage_log'] = np.log1p(df_transformed['DataUsage(GB)'])  # log1p handles zero safely
df_transformed['TotalCharges_sqrt'] = np.sqrt(df_transformed['TotalCharges'].clip(lower=0))  # prevent negative sqrt

# Plot original vs transformed
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.histplot(df_transformed['DataUsage(GB)'], bins=10, kde=True, ax=axes[0], color='skyblue')
axes[0].set_title('Original: Data Usage (GB)')

sns.histplot(df_transformed['DataUsage_log'], bins=10, kde=True, ax=axes[1], color='orange')
axes[1].set_title('Log-Transformed: Data Usage')
plt.tight_layout()
plt.show()
```

---

### 📊 Output Interpretation

- The original `DataUsage(GB)` may show a **long tail** (many small values + a few large ones).

- `DataUsage_log` compresses high values and spreads out the lower values.

- `TotalCharges_sqrt` normalizes variance for large monetary values.

These transformed features often improve:

- **Model stability** in regression,

- **Interpretability** in tree-based splits,

- **Gradient performance** in boosting models.

---

### Binning (Discretization)

---

### 📖 Concept Introduction

**Binning** converts continuous features into **discrete intervals or categories**. It’s useful when:

- You want to group values into **human-interpretable segments**,

- Need to **reduce sensitivity** to small variations,

- Want to **highlight nonlinear effects** in behavior.

### 🧠 Common Types of Binning:

| Method         | Description                                | Use Case                  |
| -------------- | ------------------------------------------ | ------------------------- |
| Equal-width    | Divides range into equal intervals         | Data with uniform spread  |
| Quantile-based | Divides data so each bin has equal samples | Skewed or uneven data     |
| Custom binning | Based on domain knowledge                  | Business-aligned grouping |

---

### 🧪 Python Code: Equal-width, Quantile, and Custom Binning

```python
"""
Step 3: Demonstrate three types of binning on 'Tenure':
- Equal-width binning (simple range split)
- Quantile-based binning (equal size buckets)
- Custom binning (business logic: New, Mid, Mature, Loyal)
"""

# Equal-width binning: divide Tenure into 4 equal intervals
df_transformed['Tenure_EqualWidth'] = pd.cut(df_transformed['Tenure'], bins=4)

# Quantile binning: divide into quartiles
df_transformed['Tenure_Quantile'] = pd.qcut(df_transformed['Tenure'], q=4)

# Custom binning
bins = [0, 12, 36, 60, np.inf]
labels = ['New', 'Mid', 'Mature', 'Loyal']
df_transformed['Tenure_Custom'] = pd.cut(df_transformed['Tenure'], bins=bins, labels=labels)

# View side-by-side
df_transformed[['Tenure', 'Tenure_EqualWidth', 'Tenure_Quantile', 'Tenure_Custom']].head()
```

---

### 📊 Output Commentary

| Tenure | EqualWidth     | Quantile      | Custom |
| ------ | -------------- | ------------- | ------ |
| 5      | (0.929, 18.25] | (0.999, 19.0] | New    |
| 34     | (18.25, 35.5]  | (31.0, 48.0]  | Mid    |

- EqualWidth gives **uniform numerical range** buckets.

- Quantile keeps **bucket sizes equal** (useful for skewed data).

- Custom gives **business-driven behavioral labels**.

---

### **Standardization & Normalization**

---

### 📖 Concept Introduction

These methods bring numerical features to a **common scale**:

- Prevent one feature from dominating due to magnitude.

- Help in **gradient descent convergence**.

- Required for models using **distances** (e.g., k-NN, clustering).

---

### 🧠 Two Main Techniques:

| Technique       | Formula                 | Output Range  |
| --------------- | ----------------------- | ------------- |
| Standardization | (x − mean) / std        | Centered at 0 |
| Normalization   | (x − min) / (max − min) | 0 to 1        |

---

### 🧪 Python Code: Apply to `MonthlyCharges` and `NumLogins`

```python
"""
Step 4: Scale numerical features using StandardScaler and MinMaxScaler.
We apply:
- Standardization to 'MonthlyCharges'
- Normalization to 'NumLogins'
"""

from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Initialize scalers
std_scaler = StandardScaler()
minmax_scaler = MinMaxScaler()

# Apply transformations
df_transformed['MonthlyCharges_std'] = std_scaler.fit_transform(df_transformed[['MonthlyCharges']])
df_transformed['NumLogins_norm'] = minmax_scaler.fit_transform(df_transformed[['NumLogins']])

# Preview scaled results
df_transformed[['MonthlyCharges', 'MonthlyCharges_std', 'NumLogins', 'NumLogins_norm']].head()
```

---

### 📊 Output Commentary

| MonthlyCharges | MonthlyCharges_std | NumLogins | NumLogins_norm |
| -------------- | ------------------ | --------- | -------------- |
| 75.6           | 0.32               | 9         | 0.47           |
| 60.2           | -0.54              | 13        | 0.80           |

- `MonthlyCharges_std`: Now centered around 0 with unit variance.

- `NumLogins_norm`: Scaled between 0 and 1 for uniform comparison.

---

### Ratio Features

---

### 📖 Concept Introduction

**Ratio Features** combine existing variables to capture efficiency, usage, or proportion. They're especially powerful in customer analytics, fraud detection, and credit scoring.

✅ Use ratio features to:

- Normalize large numbers (e.g., Charges per Login),

- Highlight **value vs. activity** (e.g., Spend per Age),

- Identify **resource efficiency**.

---

### 🧪 Python Code: Create Ratio Features

```python
"""
Step 5: Create ratio-based features.
- Charges per login: captures revenue efficiency
- Data usage per month: normalizes data consumption
- Spend efficiency: value for age & activity
"""

# Prevent divide-by-zero by adding 1 where needed
df_transformed['Charges_per_Login'] = (df_transformed['TotalCharges'] / (df_transformed['NumLogins'] + 1)).round(2)
df_transformed['DataUsage_per_Month'] = (df_transformed['DataUsage(GB)'] / (df_transformed['Tenure'] + 1)).round(2)
df_transformed['Spend_Efficiency'] = (df_transformed['TotalCharges'] / ((df_transformed['Age'] + 1) * (df_transformed['NumLogins'] + 1))).round(2)

# Preview the new features
df_transformed[['TotalCharges', 'NumLogins', 'Charges_per_Login',
                'DataUsage(GB)', 'Tenure', 'DataUsage_per_Month',
                'Age', 'Spend_Efficiency']].head()
```

---

### 📊 Output Commentary

| Charges_per_Login | DataUsage_per_Month | Spend_Efficiency |
| ----------------- | ------------------- | ---------------- |
| 180.0             | 0.42                | 4.31             |

- These give the model **contextual behavior**, not just absolute numbers.

- Particularly useful for identifying **low-usage high-spenders (churn risk)** or **efficient users (premium targets)**.

---

## 🔹 Step 6: Interaction & Polynomial Features

---

### 📖 Concept Introduction

**Interaction Features** capture combined effects of two variables.  
**Polynomial Features** are powers of existing features—useful for modeling curves or trends.

✅ Use these when:

- You suspect **nonlinear relationships**,

- You want to give **linear models more expressive power**,

- You want to explore **combinatorial behavior**.

---

### 🧪 Python Code: Create Interaction & Polynomial Features

```python
"""
Step 6: Create interaction and polynomial features.
- MonthlyCharges × Tenure = inferred TotalCharges
- Age × Logins = engagement indicator
- Square of MonthlyCharges = nonlinear spend pattern
"""

# Interaction terms
df_transformed['ChargeTenure_Interaction'] = (df_transformed['MonthlyCharges'] * df_transformed['Tenure']).round(2)
df_transformed['AgeLogin_Interaction'] = (df_transformed['Age'] * df_transformed['NumLogins']).round(2)

# Polynomial transformation
df_transformed['MonthlyCharges_Sq'] = (df_transformed['MonthlyCharges'] ** 2).round(2)

# Preview new features
df_transformed[['MonthlyCharges', 'Tenure', 'ChargeTenure_Interaction',
                'Age', 'NumLogins', 'AgeLogin_Interaction',
                'MonthlyCharges_Sq']].head()
```

---

### 📊 Output Commentary

| ChargeTenure_Interaction | AgeLogin_Interaction | MonthlyCharges_Sq |
| ------------------------ | -------------------- | ----------------- |
| 3850.2                   | 427                  | 5625.0            |

- Helps the model **understand combined effects**, such as:
  
  - Does *high spend × low tenure* indicate dissatisfaction?
  
  - Does *older age × high login count* reflect loyalty?

---

### Group-Based Aggregates (Rolling / Group-Level Statistics)

---

### 📖 Concept Introduction

In many datasets, **individuals belong to groups** (e.g., customers to departments, users to regions).  
By computing **group-level aggregates**—like average spend per department—we can:

- Capture **contextual signals**,

- Benchmark users **relative to their group**,

- Reveal **inter-group variation** and outliers.

✅ **Use Cases**:

- Department-level average charges,

- Regional fraud rates,

- Peer comparison for churn/loyalty segmentation.

---

### 🧪 Python Code: Create Group-Based Features

```python
"""
Step 7: Group-level aggregate features.
We'll create:
- Department_avg_MonthlyCharges
- Department_avg_DataUsage
Then compare individual values to their department mean.
"""

# Group by Department and compute mean values
dept_avg = df_transformed.groupby('Department')[['MonthlyCharges', 'DataUsage(GB)']].mean().round(2)
dept_avg.columns = ['Dept_Avg_MonthlyCharges', 'Dept_Avg_DataUsage']

# Merge back into the main DataFrame
df_transformed = df_transformed.merge(dept_avg, on='Department', how='left')

# Create features for individual vs group difference
df_transformed['MonthlyCharges_vs_Dept'] = (df_transformed['MonthlyCharges'] - df_transformed['Dept_Avg_MonthlyCharges']).round(2)
df_transformed['DataUsage_vs_Dept'] = (df_transformed['DataUsage(GB)'] - df_transformed['Dept_Avg_DataUsage']).round(2)

# Preview results
df_transformed[['Department', 'MonthlyCharges', 'Dept_Avg_MonthlyCharges', 'MonthlyCharges_vs_Dept',
                'DataUsage(GB)', 'Dept_Avg_DataUsage', 'DataUsage_vs_Dept']].head()
```

---

### 📊 Output Commentary

| Department | MonthlyCharges | Dept_Avg_MonthlyCharges | Diff |
| ---------- | -------------- | ----------------------- | ---- |
| Sales      | 75.5           | 68.2                    | +7.3 |
| Support    | 61.0           | 64.5                    | -3.5 |

- This highlights whether a user is **above or below the group average**.

- Helps identify:
  
  - **Over-consuming users**,
  
  - **Outliers for proactive retention**,
  
  - **Unusual patterns for fraud detection**.

---



### ✅ Recap – Techniques You’ve Mastered:

| Technique              | Purpose                                        |
| ---------------------- | ---------------------------------------------- |
| Log/Sqrt Transform     | Normalize skewed data                          |
| Binning                | Simplify numeric features into categories      |
| Scaling                | Bring features to similar ranges               |
| Ratio Features         | Highlight proportional behavior                |
| Interaction Terms      | Combine variables to capture nonlinear effects |
| Group-Based Aggregates | Benchmark users against their cohorts          |

---

# Feature Engineering of Time-Based Data

---



### Datetime Decomposition

---

### 📖 Concept Introduction

Datetime features are **rich with behavioral signals**. By decomposing a timestamp into components, we can extract:

- **Seasonality** (e.g., month, quarter),

- **Temporal behavior** (e.g., weekday vs weekend),

- **Patterns across time of day** (e.g., login hour).

✅ Use cases:

- Time-aware modeling,

- Retail seasonality,

- Staffing shifts (e.g., weekday patterns).

---

### 🧪 Python Code: Decompose SignupDate

```python
"""
Step 1: Decompose the 'SignupDate' column into individual time parts:
- Year, Month, Day, Weekday, Week Number, Quarter
"""

# Ensure 'SignupDate' is in datetime format
df_time['SignupDate'] = pd.to_datetime(df_time['SignupDate'])

# Extract components
df_time['Signup_Year'] = df_time['SignupDate'].dt.year
df_time['Signup_Month'] = df_time['SignupDate'].dt.month
df_time['Signup_Day'] = df_time['SignupDate'].dt.day
df_time['Signup_Weekday'] = df_time['SignupDate'].dt.day_name()
df_time['Signup_Week'] = df_time['SignupDate'].dt.isocalendar().week
df_time['Signup_Quarter'] = df_time['SignupDate'].dt.quarter

# Preview
df_time[['SignupDate', 'Signup_Year', 'Signup_Month', 'Signup_Weekday', 'Signup_Quarter']].head()
```

---

### 📊 Output Commentary

| SignupDate | Month | Weekday   | Quarter |
| ---------- | ----- | --------- | ------- |
| 2023-02-11 | 2     | Saturday  | 1       |
| 2023-08-30 | 8     | Wednesday | 3       |

- These components are used for:
  
  - **Time-based trends** (Q1 vs Q4),
  
  - **Campaign timing** (weekend vs weekday),
  
  - **Modeling temporal seasonality**.

 ---

## Flags and Cyclical Encoding

---

### 📖 Concept Introduction

Some datetime features are **cyclical** in nature:

- Days of the week (Monday ≈ Sunday),

- Months (December is close to January).

To retain these patterns, we use **cyclical encodings** using **sine and cosine** functions.

Also, **flags** like `IsWeekend` are helpful for behavioral segmentation.

---

### 🧪 Python Code: Create Flags & Cyclic Encodings

```python
"""
Step 2: Create:
- IsWeekend flag based on day of week,
- Sine and cosine encodings for month (to model cyclicity).
"""

# IsWeekend flag (Saturday/Sunday)
df_time['IsWeekend'] = df_time['Signup_Weekday'].isin(['Saturday', 'Sunday']).astype(int)

# Normalize month to [0, 2π] range
df_time['Month_sin'] = np.sin(2 * np.pi * df_time['Signup_Month'] / 12)
df_time['Month_cos'] = np.cos(2 * np.pi * df_time['Signup_Month'] / 12)

# Preview
df_time[['Signup_Month', 'IsWeekend', 'Month_sin', 'Month_cos']].head()
```

---

### 📊 Output Commentary

- `IsWeekend`: Useful for time-based cohorting.

- `Month_sin`, `Month_cos`: Ensure that **December and January are adjacent**, unlike simple numeric encoding.

---



## Time Since Event (Recency)

---

### 📖 Concept Introduction

**Recency features** capture how much time has passed since a key event, such as:

- Last login,

- Last transaction,

- Last renewal.

These are powerful indicators of:

- **Engagement drop-offs**,

- **Likely churn**,

- **Customer health**.

---

### 🧪 Python Code: Time Since Last Login

```python
"""
Step 3: Calculate recency from 'LastLogin' to today's date.
This helps us understand how recently a customer was active.
"""

# Define reference date (e.g., today)
today = pd.Timestamp("2024-04-01")

# Ensure datetime type
df_time['LastLogin'] = pd.to_datetime(df_time['LastLogin'])

# Calculate recency in days
df_time['Days_Since_Login'] = (today - df_time['LastLogin']).dt.days

# Preview
df_time[['CustomerID', 'LastLogin', 'Days_Since_Login']].head()
```

---

### 📊 Output Commentary

| CustomerID | LastLogin  | Days_Since_Login |
| ---------- | ---------- | ---------------- |
| C001       | 2023-11-15 | 138              |
| C002       | 2024-01-05 | 87               |

- Larger values → customer has **been inactive longer**,

- Common churn signal: high recency = disengagement.

---

## Time Until Event (Forward Window)

---

### 📖 Concept Introduction

**Time until an event** estimates the number of days **left before a future milestone**, like:

- Subscription renewal,

- Policy expiration,

- Scheduled upgrade.

This is used in:

- **Retention alerts**,

- **Reminder emails**,

- **Renewal forecasting models**.

---

### 🧪 Python Code: Days Until Renewal

```python
"""
Step 4: Calculate how many days are left until subscription renewal.
"""

# Ensure datetime type
df_time['RenewalDate'] = pd.to_datetime(df_time['RenewalDate'])

# Calculate future time delta
df_time['Days_Until_Renewal'] = (df_time['RenewalDate'] - today).dt.days

# Preview
df_time[['CustomerID', 'RenewalDate', 'Days_Until_Renewal']].head()
```

---

### 📊 Output Commentary

| RenewalDate | Days_Until_Renewal |
| ----------- | ------------------ |
| 2024-06-01  | 61                 |
| 2024-12-15  | 258                |

- Small values indicate **imminent deadlines**, useful for **intervention** or **campaign triggers**.

- Negative values = **expired customers** (can also be a flag!).

---

Perfect! Let’s now wrap up **Part 3: Time-Based Feature Engineering** with two more advanced (yet very useful) concepts:



---

## Time-Based Cohorts

---

### 📖 Concept Introduction

**Cohorting** involves grouping users based on **time of their first interaction**—like their signup date. This helps:

- Analyze retention patterns,

- Run lifecycle-based analysis,

- Compare engagement across cohorts (e.g., Jan vs Mar signups).

---

### 🧪 Python Code: Create Signup Cohorts (by Month)

```python
"""
Step 5: Time-Based Cohorts
We’ll group customers into monthly signup cohorts.
This allows us to compare users who joined in the same period.
"""

# Create cohort label from SignupDate
df_time['Signup_Cohort'] = df_time['SignupDate'].dt.to_period('M').astype(str)

# Preview cohorts
df_time[['CustomerID', 'SignupDate', 'Signup_Cohort']].head()
```

---

### 📊 Output Commentary

| SignupDate | Signup_Cohort |
| ---------- | ------------- |
| 2023-02-11 | 2023-02       |
| 2023-05-23 | 2023-05       |

- Use this for **retention charts**, **cohort-wise modeling**, or **trend comparison**.

- Often used in product analytics or campaign targeting.

---

## Time-Based Rolling Features (requires time-series data)

---

### 📖 Concept Introduction

**Rolling or time-windowed features** summarize behavior over **recent periods** (e.g., last 7 days):

- Rolling login counts,

- Moving average spend,

- Usage volatility.

Since our synthetic dataset doesn’t have detailed time-stamped logs, we’ll simulate it briefly.

---

### 🧪 Simulated Example: Rolling Login Frequency

```python
"""
Step 6: Simulated example of rolling features using LoginFrequency.
We'll group by cohort and calculate the average login frequency per cohort.
"""

# Example: Average login frequency per Signup Cohort
cohort_stats = df_time.groupby('Signup_Cohort')['LoginFrequency'].mean().round(2)
df_time = df_time.merge(cohort_stats.rename('Cohort_Avg_Logins'), on='Signup_Cohort', how='left')

# Preview
df_time[['CustomerID', 'Signup_Cohort', 'LoginFrequency', 'Cohort_Avg_Logins']].head()
```

---

### 📊 Output Commentary

| CustomerID | Cohort  | LoginFrequency | Avg in Cohort |
| ---------- | ------- | -------------- | ------------- |
| C005       | 2023-03 | 4              | 6.2           |
| C006       | 2023-03 | 8              | 6.2           |

- This approach helps identify:
  
  - Users with **above or below-average behavior**,
  
  - **Emerging patterns** in usage over time.

---

🎯 **End of Part 3: Time-Based Feature Engineering**

---

### ✅ Recap – What You Learned:

| Technique              | Insight Captured                          |
| ---------------------- | ----------------------------------------- |
| Datetime Decomposition | Seasonality, weekday, month, quarter      |
| IsWeekend + Cyclic     | Cyclic patterns like time-of-week effects |
| Time Since Login       | Recency → churn risk                      |
| Time Until Renewal     | Imminent action window                    |
| Cohorts                | Lifecycle-stage-based segmentation        |
| Rolling Features       | Moving patterns for forecasting           |

---


