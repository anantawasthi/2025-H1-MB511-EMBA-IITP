# HR Attrition Case Study - Phase 1: EDA Activities

# ----------------------------------------------


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis, shapiro, pearsonr, ttest_ind, chi2_contingency
import missingno as msno
from sklearn.feature_selection import mutual_info_classif
from optbinning import OptimalBinning

sns.set(style='whitegrid')



# ----------------------------------------------

# Activity 1: Import the Dataset

# ----------------------------------------------


file_path = 'HR_Attrition_Dataset_1000.xlsx'
df = pd.read_excel(file_path)
print('✅ Dataset successfully imported.')


# ----------------------------------------------

# Activity 2: Examine the Structure

# ----------------------------------------------


print(df.shape)
print(df.columns.tolist())
print(df.head())
print(df.info())
print(df.describe())


# ----------------------------------------------

# Activity 3.1: Descriptive Univariate EDA

# ----------------------------------------------


numeric_cols = ['Age', 'Tenure_Months', 'Salary', 'Engagement_Score']
categorical_cols = ['Department', 'Gender', 'Resigned']
print(df[numeric_cols].describe().T)
for col in numeric_cols:
    print(f"{col} → Range: {df[col].max() - df[col].min()}, IQR: {df[col].quantile(0.75) - df[col].quantile(0.25)}")
for col in categorical_cols:
    print(df[col].value_counts())
    print(df[col].value_counts(normalize=True) * 100)


# ----------------------------------------------

# Activity 3.2: Graphical Univariate EDA

# ----------------------------------------------


for col in numeric_cols:
    plt.figure(figsize=(14, 5))
    plt.subplot(1, 2, 1)
    sns.histplot(df[col], kde=True, bins=30)
    plt.title(f'Distribution of {col}')
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.tight_layout()
    plt.show()
for col in categorical_cols:
    sns.countplot(data=df, x=col)
    plt.title(f'Count Plot of {col}')
    plt.xticks(rotation=30)
    plt.show()


# ----------------------------------------------

# Activity 3.3: Statistical Univariate Properties

# ----------------------------------------------


for col in numeric_cols:
    values = df[col].dropna()
    print(f'{col} → Skewness: {skew(values):.2f}, Kurtosis: {kurtosis(values):.2f}')
    _, p = shapiro(values[:500])
    print(f'Shapiro-Wilk Test p-value: {p:.4f}')


# ----------------------------------------------

# Activity 4.1: Descriptive Bi-variate EDA

# ----------------------------------------------


print(df.groupby('Department')[['Salary', 'Tenure_Months', 'Engagement_Score']].mean())
print(pd.crosstab(df['Gender'], df['Resigned'], normalize='index') * 100)
print(df[['Age', 'Tenure_Months', 'Salary', 'Engagement_Score']].corr())


# ----------------------------------------------

# Activity 4.2: Graphical Bi-variate EDA

# ----------------------------------------------


sns.boxplot(data=df, x='Department', y='Salary')
plt.title('Salary by Department')
plt.show()
sns.boxplot(data=df, x='Resigned', y='Engagement_Score')
plt.title('Engagement by Resigned')
plt.show()


# ----------------------------------------------

# Activity 4.3: Statistical Bi-variate Tests

# ----------------------------------------------


print(pearsonr(df['Salary'], df['Tenure_Months']))
print(ttest_ind(df[df['Resigned'] == 'Yes']['Engagement_Score'].dropna(), df[df['Resigned'] == 'No']['Engagement_Score'].dropna()))
print(chi2_contingency(pd.crosstab(df['Department'], df['Resigned'])))


# ----------------------------------------------

# Activity 5.1: Descriptive Multivariate Analysis

# ----------------------------------------------


df['Engagement_Level'] = pd.cut(df['Engagement_Score'], bins=[0, 4, 7, 10], labels=['Low', 'Medium', 'High'])
df['Tenure_Group'] = pd.cut(df['Tenure_Months'], bins=[0, 24, 60, 120], labels=['<2 yrs', '2–5 yrs', '5+ yrs'])
print(pd.crosstab([df['Tenure_Group'], df['Engagement_Level']], df['Resigned'], normalize='index') * 100)


# ----------------------------------------------

# Activity 6: Missing Value Detection and Imputation

# ----------------------------------------------


msno.matrix(df)
plt.show()
df['Engagement_Score_Imputed'] = df.groupby('Department')['Engagement_Score'].transform(lambda x: x.fillna(x.median()))
df['Engagement_Missing_Flag'] = df['Engagement_Score'].isna().astype(int)


# ----------------------------------------------

# Activity 7: Outlier Detection and Treatment

# ----------------------------------------------


df['Salary_Capped'] = df['Salary'].clip(lower=df['Salary'].quantile(0.01), upper=df['Salary'].quantile(0.99))
df['Tenure_Capped'] = df['Tenure_Months'].clip(lower=df['Tenure_Months'].quantile(0.01), upper=df['Tenure_Months'].quantile(0.99))


# ----------------------------------------------

# Activity 8: Data Transformation and Feature Engineering

# ----------------------------------------------


df['Salary_Log'] = np.log1p(df['Salary_Capped'])
df['Salary_per_Month_of_Service'] = (df['Salary'] / df['Tenure_Months'].replace(0, np.nan)).fillna(0)
df['At_Risk'] = np.where((df['Engagement_Score_Imputed'] < 5) & (df['Tenure_Capped'] < 24), 1, 0)


# ----------------------------------------------

# Activity 9: Feature Selection with Mutual Information and IV

# ----------------------------------------------


selected_features = ['Engagement_Score_Imputed', 'At_Risk', 'Tenure_Capped', 'Salary_Log']
X = df[selected_features]
y = df['Resigned'].map({'Yes': 1, 'No': 0})
mi_scores = mutual_info_classif(X.fillna(0), y)
for i, feature in enumerate(selected_features):
    print(f'MI Score for {feature}: {mi_scores[i]:.3f}')
for feature in selected_features:
    optb = OptimalBinning(name=feature, dtype='numerical', target_dtype='binary')
    optb.fit(df[feature], y)
    print(f'{feature} → IV: {optb.information_value_:.3f}')


