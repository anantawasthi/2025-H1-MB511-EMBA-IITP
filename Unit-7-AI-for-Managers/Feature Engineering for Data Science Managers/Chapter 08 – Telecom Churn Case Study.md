We'll walk through this **feature engineering case study** step-by-step using the structured template:

> **1. Problem Statement**  
> **2. Approach**  
> **3. Python Code (with docstring, inline comments, and explanation)**  
> **4. Output**  
> **5. Output Discussion**  
> **6. Business-Specific Discussion**

Let’s begin with **Step 1: Problem Statement**.

---

# ✅ Step 1: Problem Statement

**Context**:  
Telecommunication service providers operate in highly competitive markets, where acquiring new customers is costly and losing existing customers (churn) can lead to revenue loss and reputational damage.

**Business Problem**:  
Identify which customers are likely to leave the telecom service, understand **what factors influence churn**, and help design **targeted retention strategies**.

**Data Science Problem**:  
Build a churn prediction-ready dataset using structured **feature engineering**:

- Convert raw customer data into meaningful features,

- Prepare these features for modeling,

- Ensure interpretability and business relevance of engineered features.

**Key Goal**:  
Enable a classification model to **accurately and reliably predict customer churn** while ensuring that the inputs (features) reflect real-world logic, strategic insight, and operational feasibility.

---



# ✅ Step 2: Approach

To engineer features that are both statistically meaningful and business-relevant, we adopt a structured, phase-wise methodology. This ensures not only **technical rigor** but also **managerial alignment** with decision-making contexts like pricing, service bundling, contract duration, and engagement metrics.

---

## 🧭 **Feature Engineering Workflow**

| Phase                     | Activity                                                        | Purpose                                    |
| ------------------------- | --------------------------------------------------------------- | ------------------------------------------ |
| **1. Data Understanding** | Load dataset, inspect schema, check nulls and types             | Ensure readiness for feature creation      |
| **2. Data Cleaning**      | Fix missing values, drop irrelevant columns                     | Prepare a clean canvas for engineering     |
| **3. Feature Creation**   | Engineer categorical, continuous, and time-based features       | Transform raw data into high-signal inputs |
| **4. Feature Encoding**   | Convert categorical features into numerical representations     | Make features model-compatible             |
| **5. Feature Selection**  | Retain the most informative, interpretable, and stable features | Reduce noise, redundancy, and overfitting  |
| **6. Data Splitting**     | Split into training and testing sets with stratification        | Simulate real-world performance            |

---

## 📊 Types of Features to be Engineered

| Feature Type    | Techniques Applied                                                     |
| --------------- | ---------------------------------------------------------------------- |
| **Categorical** | Grouping, simplification, encoding (e.g., Contract Type, Payment Mode) |
| **Continuous**  | Ratio features (e.g., average monthly spend), binning, derived metrics |
| **Time-Based**  | Tenure group creation, recency-based insights                          |

---

## 🎯 Modeling Readiness Goals

- Ensure **each feature has a rationale** linked to customer behavior or business logic.

- Prioritize **features that are interpretable** to customer support, marketing, and operations teams.

- Avoid features that may cause **bias**, **data leakage**, or are **unavailable in production**.

---

# ✅ Step 3: Python Code

## 📦 Part A: Importing Libraries and Initial Setup

```python
# 📦 PART A: IMPORT LIBRARIES AND SETUP

"""
This block imports the required Python libraries for:
- Data loading and transformation (pandas, numpy),
- Visualization (matplotlib, seaborn),
- Feature selection and preprocessing (sklearn),
- Data splitting for modeling.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import mutual_info_classif
from sklearn.model_selection import train_test_split

# Visual and display settings
pd.set_option('display.max_columns', None)
sns.set(style='whitegrid')
```

---

## 📂 Part B: Load Dataset and Preview

```python
# 📂 PART B: LOAD DATASET

"""
Load the Telco Customer Churn dataset.
Check its shape and preview the first few rows.
"""

# Load the dataset (ensure this file is in your working directory)
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Preview data structure
print("Dataset Shape:", df.shape)
df.head()
```

---

## 🧹 Part C: Data Cleaning

```python
# 🧹 PART C: CLEANING DATA

"""
1. Drop non-informative fields (e.g., customerID).
2. Convert 'TotalCharges' to numeric (some are empty strings).
3. Handle missing values by imputing with the median.
"""

# Remove ID column
df.drop("customerID", axis=1, inplace=True)

# Convert TotalCharges to float, coercing errors to NaN
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce')

# Impute missing TotalCharges with the median
df["TotalCharges"].fillna(df["TotalCharges"].median(), inplace=True)
```

---

# ✅ Step 3: Python Code

## ⚙️ **Part D: Feature Creation**

Here, we engineer new variables using business logic and domain understanding. This includes handling **categorical**, **continuous**, and **tenure/time-related** fields.

---

### 🏷️ D1: Tenure Grouping

```python
# 🏷️ PART D1: TENURE GROUPING

"""
Group customers into tenure brackets to create behavioral segments:
- 0–12 months
- 13–24 months
- 25–48 months
- 49–60 months
- 61–72 months

This helps us capture 'new', 'moderate', and 'long-term' customers.
"""

df["tenure_group"] = pd.cut(
    df["tenure"],
    bins=[0, 12, 24, 48, 60, 72],
    labels=["0-12", "13-24", "25-48", "49-60", "61-72"]
)
```

---

### 💸 D2: Average Monthly Spend

```python
# 💸 PART D2: AVERAGE MONTHLY SPEND

"""
Create a derived feature: average monthly spend.
This normalizes 'TotalCharges' against tenure and provides insight into billing pressure.
"""

df["avg_monthly_spend"] = df["TotalCharges"] / (df["tenure"] + 1)  # +1 avoids division by zero
```

---

### 🧾 D3: Count of Services Used

```python
# 🧾 PART D3: COUNT OF SERVICES USED

"""
This feature counts how many value-added services the customer subscribes to.
Higher usage often correlates with loyalty (or billing dissatisfaction).
"""

service_cols = [
    "PhoneService", "MultipleLines", "InternetService",
    "OnlineSecurity", "OnlineBackup", "DeviceProtection",
    "TechSupport", "StreamingTV", "StreamingMovies"
]

# Count number of 'Yes' service indicators per customer
df["services_count"] = df[service_cols].apply(lambda row: (row == "Yes").sum(), axis=1)
```

---

### 💳 D4: Simplify Payment Method

```python
# 💳 PART D4: SIMPLIFY PAYMENT METHOD

"""
Group payment methods into broader categories:
- 'Auto': Credit card or bank transfer (automatic)
- 'Online': Electronic check
- 'Offline': Mailed check

This allows us to correlate payment convenience with churn.
"""

df["payment_simplified"] = df["PaymentMethod"].replace({
    "Electronic check": "Online",
    "Mailed check": "Offline",
    "Bank transfer (automatic)": "Auto",
    "Credit card (automatic)": "Auto"
})
```

---

We’ve now engineered **four high-value features**:

- `tenure_group`

- `avg_monthly_spend`

- `services_count`

- `payment_simplified`

Each one reflects a **behavioral or economic logic**, making them valuable for predictive modeling and business interpretation.



Awesome! Let’s proceed to:

---



## 🔢 **Part E: Encoding Categorical Features**

Since machine learning models generally require numeric input, we must encode all categorical variables. We’ll use `LabelEncoder` for simplicity here, given that the dataset is relatively small and we want to retain interpretability.

---

### 🔠 E1: Label Encoding All Categorical Features

```python
# 🔠 PART E1: ENCODING CATEGORICAL FEATURES

"""
This block encodes categorical columns using LabelEncoder.
- This is suitable for tree-based models or as a baseline.
- A dictionary is maintained to map original labels for interpretation.

Best practice: Retain encoded mappings for model explainability or inverse transformation.
"""

from sklearn.preprocessing import LabelEncoder

# Identify object-type columns (categorical)
categorical_cols = df.select_dtypes(include="object").columns

# Dictionary to store mappings for each encoded column
label_encoders = {}
encoded_value_maps = {}

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le
    encoded_value_maps[col] = dict(zip(le.classes_, le.transform(le.classes_)))
```

---

### 🔍 E2: Preview Encoded Feature Mappings (Optional)

```python
# 🔍 PART E2: DISPLAY ENCODED VALUE MAPPINGS

"""
This preview shows how some categorical values were transformed.
Useful for reviewing encoding logic.
"""

for col in ["gender", "Contract", "payment_simplified"]:
    print(f"Encoding map for {col}: {encoded_value_maps[col]}")
```

---

Now all features in the dataset are:

- **Numerically represented**,

- **Free of nulls**, and

- Include **several new engineered features** that capture customer tenure, spend, and behavior.



## 📊 **Part F: Feature Selection using Mutual Information**

Now that all features are numerically encoded, we want to identify **which ones provide the most information about customer churn**. We'll use **Mutual Information (MI)**, a model-free, information-theoretic metric that measures how much knowing one variable reduces uncertainty about another.

---

### 🔍 F1: Mutual Information Score Calculation

```python
# 🔍 PART F1: CALCULATE MUTUAL INFORMATION (MI) SCORES

"""
Use mutual_info_classif to calculate the importance of each feature with respect to the target (Churn).
MI works well with both categorical and continuous variables.
"""

# Separate target and features
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Compute MI scores
mi_scores = pd.Series(mutual_info_classif(X, y, discrete_features='auto'), index=X.columns)

# Sort descending for visibility
mi_scores = mi_scores.sort_values(ascending=False)

# Display top 10 features
print("Top 10 Important Features by Mutual Information:\n")
print(mi_scores.head(10))
```

---

### 📈 F2: Visualize Feature Importance (Optional but insightful)

```python
# 📈 PART F2: BARPLOT OF FEATURE IMPORTANCE

"""
Plot the top 10 features based on mutual information.
This gives a visual sense of which variables most strongly relate to churn.
"""

plt.figure(figsize=(10, 6))
sns.barplot(x=mi_scores.head(10), y=mi_scores.head(10).index, palette='viridis')
plt.title("Top 10 Features by Mutual Information with Churn", fontsize=14)
plt.xlabel("Mutual Information Score")
plt.ylabel("Feature")
plt.tight_layout()
plt.show()
```

---

## ✂️ **Part G: Data Splitting for Model Training and Testing**

Once we've engineered and selected our features, we prepare for modeling by **splitting the dataset** into training and test sets. We'll use **stratified sampling** to preserve the original churn class distribution—critical in imbalanced classification tasks.

---

### 🔄 G1: Split the Dataset

```python
# 🔄 PART G1: TRAIN-TEST SPLIT

"""
Split the dataset into:
- 80% for training,
- 20% for testing.
Use stratification to ensure churn class balance across both sets.
"""

from sklearn.model_selection import train_test_split

X = df.drop("Churn", axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# Display resulting split sizes
print(f"Training set size: {X_train.shape[0]} samples")
print(f"Test set size: {X_test.shape[0]} samples")
```

---

### 📊 G2: Verify Class Balance After Split (Optional but recommended)

```python
# 📊 PART G2: CLASS BALANCE CHECK

"""
Ensure the churn class distribution remains consistent post-split.
This is important to avoid misleading evaluation metrics later.
"""

print("\nChurn Distribution in Training Set:")
print(y_train.value_counts(normalize=True).rename_axis("Churn").to_frame("Proportion"))

print("\nChurn Distribution in Test Set:")
print(y_test.value_counts(normalize=True).rename_axis("Churn").to_frame("Proportion"))
```

---


