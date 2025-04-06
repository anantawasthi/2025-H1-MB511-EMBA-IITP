

## 🔹 Chart 1: Bar Chart

**Use Case**: Compare the number of employees across departments.



```python
# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the synthetic HR dataset (assumed file name)
df = pd.read_excel('Synthetic_HR_Dataset.xlsx', sheet_name='Employee_Master')

# --- Initial Exploration ---

# Show first 5 rows of data
print(df.head())

# Check the unique values in Department column
print("Departments:", df['Department'].unique())

# Count number of employees per department
department_counts = df['Department'].value_counts()
print("Employee count by Department:\n", department_counts)

# --- Bar Chart ---

"""
Bar Chart:
This chart is used to display the count of employees across different departments.
It helps managers quickly see which departments are large or small.
"""

# Plotting the bar chart
plt.figure(figsize=(8, 5))  # Set the chart size
department_counts.plot(kind='bar')  # Create bar chart from value counts

# Add title and axis labels
plt.title('Employee Count by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')

# Show the chart
plt.tight_layout()
plt.show()
```

---

### 🧠 Explanation:

- **Why this chart**: A bar chart is ideal for comparing sizes of categories—in this case, departments.

- **Interpretation**: Taller bars = more employees. You can identify staffing gaps or resource-heavy areas.

- **Limitations**: Doesn’t show proportions directly (a pie chart would help there).

- **Alternatives**: Pie chart, horizontal bar chart.

---

## 🔹 Chart 2: **Pie Chart** – *Proportion of Gender in the Workforce*

```python
# --- Initial Exploration for Gender Distribution ---

# Check unique gender values
print("Unique Genders:", df['Gender'].unique())

# Count of employees by gender
gender_counts = df['Gender'].value_counts()
print("Employee count by Gender:\n", gender_counts)

# --- Pie Chart ---

"""
Pie Chart:
This chart shows the proportion of employees by gender.
Useful for diversity reporting or gender equity assessments.
"""

# Plotting pie chart
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)

# Add title
plt.title('Gender Distribution in Workforce')

# Display the chart
plt.show()
```

### ✅ Interpretation:

- Gives a clear idea of **proportional representation**

- Great for **diversity insights**

- Less effective with **too many categories**

---

## 🔹 Chart 3: **Histogram** – *Distribution of Employee Ages*

```python
# --- Initial Exploration for Age Column ---

# Check for nulls and summary
print("Missing Age values:", df['Age'].isnull().sum())
print("Age Summary:\n", df['Age'].describe())

# --- Histogram ---

"""
Histogram:
This chart helps visualize the distribution of a numeric variable—in this case, employee ages.
Useful for understanding age demographics and planning generational policies.
"""

# Plotting histogram
plt.figure(figsize=(8, 5))
plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')

# Add labels and title
plt.title('Age Distribution of Employees')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Display the chart
plt.tight_layout()
plt.show()
```

### ✅ Interpretation:

- Shows **concentration** of age groups (e.g., younger vs. older workforce)

- Helps identify skewness or outliers

- Ideal for **continuous numeric variables**

---

## 🔹 Chart 4: **Box Plot** – *Salary Distribution by Department*

```python
import seaborn as sns

# --- Initial Exploration ---

# Check data types and basic info
print(df[['Department', 'MonthlySalary']].info())

# Check for outliers
print(df.groupby('Department')['MonthlySalary'].describe())

# --- Box Plot ---

"""
Box Plot:
Shows distribution, median, and outliers of salary by department.
Useful for identifying salary fairness or detecting outliers in compensation.
"""

# Plotting box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Department', y='MonthlySalary', data=df)

# Add title and labels
plt.title('Salary Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Monthly Salary')

# Rotate x-axis labels if needed
plt.xticks(rotation=45)

# Display the chart
plt.tight_layout()
plt.show()
```

### ✅ Interpretation:

- Reveals **median salary**, **interquartile range**, and **outliers**

- Departments with wider boxes = more salary variation

- Can expose **inequities or pay structure gaps**

---

## 🔹 Chart 5: **Line Chart** – *Monthly New Hires Trend*

```python
# --- Initial Exploration for Joining Dates ---

# Ensure 'DateOfJoining' is datetime
df['DateOfJoining'] = pd.to_datetime(df['DateOfJoining'])

# Extract year-month for aggregation
df['JoinMonth'] = df['DateOfJoining'].dt.to_period('M')

# Count number of employees joined per month
monthly_hires = df['JoinMonth'].value_counts().sort_index()
monthly_hires.index = monthly_hires.index.astype(str)  # Convert Period to string for plotting

print("Monthly Hiring Trend:\n", monthly_hires.head())

# --- Line Chart ---

"""
Line Chart:
Displays new hires over time. Useful for visualizing hiring trends, seasonal effects, or policy impact.
"""

# Plotting line chart
plt.figure(figsize=(12, 6))
plt.plot(monthly_hires.index, monthly_hires.values, marker='o')

# Formatting
plt.title('Monthly New Hires Trend')
plt.xlabel('Month')
plt.ylabel('Number of New Joinees')
plt.xticks(rotation=45)

# Display the chart
plt.tight_layout()
plt.show()
```

### ✅ Interpretation:

- Tracks **recruitment trends** over time

- Helps identify **seasonality** or the impact of hiring drives

- Can be extended to track **attrition or training completions**

---



## 🔹 Chart 6: **Stacked Bar Chart** – *Gender Distribution Across Departments*

```python
# --- Initial Exploration ---

# Create a cross-tabulation of Department vs Gender
dept_gender_counts = pd.crosstab(df['Department'], df['Gender'])

print("Department-wise Gender Count:\n", dept_gender_counts.head())

# --- Stacked Bar Chart ---

"""
Stacked Bar Chart:
Displays category breakdowns within a group. Here, we’re showing gender distribution within departments.
Helpful for understanding diversity within teams or departments.
"""

# Plotting the stacked bar chart
dept_gender_counts.plot(kind='bar', stacked=True, figsize=(10, 6))

# Chart formatting
plt.title('Gender Distribution Across Departments')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.legend(title='Gender')

# Display the chart
plt.tight_layout()
plt.show()
```

### ✅ Interpretation:

- Easily identifies **departmental gender balance**

- Stacked bars show **total headcount and internal breakdown**

- Can become cluttered if too many sub-categories

---

## 🔹 Chart 7: **Grouped Bar Chart** – *Average Salary by Gender Across Departments*

```python
# --- Initial Exploration ---

# Group by Department and Gender, then calculate mean salary
avg_salary = df.groupby(['Department', 'Gender'])['MonthlySalary'].mean().unstack()

print("Average Salary by Gender and Department:\n", avg_salary.head())

# --- Grouped Bar Chart ---

"""
Grouped Bar Chart:
Used to compare subcategories side-by-side. Here, we’re comparing average salaries by gender within each department.
Good for detecting pay disparities or role imbalance.
"""

# Plotting grouped bar chart
avg_salary.plot(kind='bar', figsize=(10, 6))

# Chart formatting
plt.title('Average Monthly Salary by Gender Across Departments')
plt.xlabel('Department')
plt.ylabel('Average Monthly Salary')
plt.xticks(rotation=45)
plt.legend(title='Gender')

# Display the chart
plt.tight_layout()
plt.show()
```

### ✅ Interpretation:

- Makes it easy to spot **inter-gender pay differences**

- Side-by-side bars are great for quick comparisons

- Can lead to clutter with many sub-groups

---

## 🔹 Chart 8: **Heatmap** – *Correlation Between Numeric Features*

```python
# --- Initial Exploration ---

# Selecting only numeric columns
numeric_cols = df.select_dtypes(include='number')

# Compute correlation matrix
correlation_matrix = numeric_cols.corr()

print("Correlation Matrix:\n", correlation_matrix)

# --- Heatmap ---

import seaborn as sns

"""
Heatmap:
Displays correlation strengths between numerical variables. Helps detect linear relationships and multicollinearity.
"""

# Plotting heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')

# Chart formatting
plt.title('Correlation Heatmap of Numeric Features')

# Display the chart
plt.tight_layout()
plt.show()
```

### ✅ Interpretation:

- Useful for feature selection in modeling

- Bright/dark color = strong correlation

- Doesn't imply causation, only correlation

---

## 🔹 Chart 9: **Scatter Plot** – *Age vs. Monthly Salary*

```python
# --- Initial Exploration ---

# Check for nulls
print(df[['Age', 'MonthlySalary']].isnull().sum())

# --- Scatter Plot ---

"""
Scatter Plot:
Shows the relationship between two continuous variables. Here, we explore how age relates to salary.
Useful for identifying trends, clusters, or outliers.
"""

# Plotting scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df['Age'], df['MonthlySalary'], alpha=0.6)

# Chart formatting
plt.title('Age vs. Monthly Salary')
plt.xlabel('Age')
plt.ylabel('Monthly Salary')

# Display the chart
plt.tight_layout()
plt.show()
```

### ✅ Interpretation:

- Can show **linear or non-linear patterns**

- Reveals **clusters, gaps, or outliers**

- Hard to interpret with dense overlaps or many variables

---

## 🔹 Chart 10: **Violin Plot** – *Age Distribution by Gender*

```python
# --- Initial Exploration ---

# Check age distribution by gender
print(df.groupby('Gender')['Age'].describe())

# --- Violin Plot ---

"""
Violin Plot:
A combination of box plot and KDE (smoothed histogram). It shows the distribution and density of the data.
Great for comparing distributions across categories.
"""

# Plotting violin plot
plt.figure(figsize=(8, 5))
sns.violinplot(x='Gender', y='Age', data=df)

# Chart formatting
plt.title('Age Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Age')

# Display the chart
plt.tight_layout()
plt.show()
```

### ✅ Interpretation:

- More informative than box plot alone

- Useful to spot **multi-modal** (bimodal/mixed) distributions

- Can be less intuitive for beginners

---



## 🔹 Chart 11: **Donut Chart** – *Employment Type Distribution*

```python
# --- Initial Exploration ---

# Check unique Employment Types
print("Employment Types:", df['EmploymentType'].unique())

# Count of employment types
employment_type_counts = df['EmploymentType'].value_counts()
print("Counts by Employment Type:\n", employment_type_counts)

# --- Donut Chart ---

"""
Donut Chart:
A variation of the pie chart, useful for showing category proportions with better center spacing.
Looks modern and is easy to annotate.
"""

# Plotting donut chart
plt.figure(figsize=(6, 6))
plt.pie(employment_type_counts, labels=employment_type_counts.index, autopct='%1.1f%%', startangle=90, wedgeprops={'width': 0.4})

# Add title
plt.title('Employment Type Distribution')

# Display chart
plt.tight_layout()
plt.show()
```

### ✅ Interpretation:

- Functionally same as pie chart, but visually more appealing

- Adds center space for labels or annotations

- Good for high-level category distribution

---

## 🔹 Chart 12: **Area Chart** – *Cumulative New Hires Over Time*

```python
# --- Initial Exploration ---

# Count of new hires by month (reuse JoinMonth)
monthly_hires_sorted = df.groupby('JoinMonth').size().sort_index()

# Convert to cumulative total
cumulative_hires = monthly_hires_sorted.cumsum()
print("Cumulative Hires:\n", cumulative_hires)

# --- Area Chart ---

"""
Area Chart:
Highlights the accumulation of a metric over time. Here, we show cumulative hires month by month.
Great for showing trends in workforce growth.
"""

# Plotting area chart
plt.figure(figsize=(10, 5))
plt.fill_between(cumulative_hires.index.astype(str), cumulative_hires.values, color='skyblue', alpha=0.6)

# Chart formatting
plt.title('Cumulative Hiring Over Time')
plt.xlabel('Month')
plt.ylabel('Total Hires')
plt.xticks(rotation=45)

# Display chart
plt.tight_layout()
plt.show()
```

### ✅ Interpretation:

- Great for **trend analysis and time series growth**

- Emphasizes **cumulative totals**

- Might obscure fine monthly variations (unlike line charts)

---

## 🔹 Chart 13: **Horizontal Bar Chart** – *Average Training Hours by Department*

```python
# --- Initial Exploration ---

# Calculate average training hours per department
avg_training = df.groupby('Department')['TrainingHours'].mean().sort_values()

print("Average Training Hours by Department:\n", avg_training)

# --- Horizontal Bar Chart ---

"""
Horizontal Bar Chart:
Useful when category names are long or there are many categories.
Here, we compare training investment across departments.
"""

# Plotting horizontal bar chart
plt.figure(figsize=(10, 6))
avg_training.plot(kind='barh', color='teal')

# Chart formatting
plt.title('Average Training Hours by Department')
plt.xlabel('Training Hours')
plt.ylabel('Department')

# Display chart
plt.tight_layout()
plt.show()
```

### ✅ Interpretation:

- Better readability than vertical bars when labels are long

- Good for **ranked comparisons**

- Can be enhanced with labels or color coding

---

## 🔹 Chart 14: **KDE Plot** – *Distribution of Tenure*

```python
# --- Initial Exploration ---

# Check distribution and summary of tenure
print("Tenure Summary:\n", df['Tenure'].describe())

# --- KDE Plot ---

"""
KDE (Kernel Density Estimate) Plot:
Smoothed version of a histogram. Helps understand the shape of a distribution without binning.
Ideal for detecting modality and spread.
"""

# Plotting KDE
plt.figure(figsize=(8, 5))
sns.kdeplot(df['Tenure'], shade=True)

# Chart formatting
plt.title('Distribution of Employee Tenure')
plt.xlabel('Years in Company')
plt.ylabel('Density')

# Display chart
plt.tight_layout()
plt.show()
```

### ✅ Interpretation:

- Shows **smoothed shape** of tenure distribution

- Better than histograms for small datasets

- Doesn’t show actual frequency values

---

## 🔹 Chart 15: **Bubble Chart** – *Experience vs. Salary with Training Hours as Bubble Size*

```python
# --- Initial Exploration ---

# Select relevant columns and drop nulls
bubble_data = df[['TotalExperience', 'MonthlySalary', 'TrainingHours']].dropna()

# --- Bubble Chart ---

"""
Bubble Chart:
A scatter plot with bubble sizes representing a third variable.
Here, bubble size = training hours. Useful to explore multi-dimensional relationships.
"""

# Plotting bubble chart
plt.figure(figsize=(10, 6))
plt.scatter(
    bubble_data['TotalExperience'], 
    bubble_data['MonthlySalary'], 
    s=bubble_data['TrainingHours'] * 5,  # Scale size for visibility
    alpha=0.5, edgecolor='k'
)

# Chart formatting
plt.title('Experience vs Salary (Bubble = Training Hours)')
plt.xlabel('Total Experience (Years)')
plt.ylabel('Monthly Salary')

# Display chart
plt.tight_layout()
plt.show()
```

### ✅ Interpretation:

- Reveals **tri-variate relationships**

- Size dimension adds **insightful depth** (e.g., training impact)

- Can be visually dense or hard to interpret without scaling

---

## 🔹 Chart 16: **Pair Plot** – *Multi-variable Relationship Exploration*

```python
# --- Initial Exploration ---

# Select numeric features for correlation exploration
pair_data = df[['Age', 'MonthlySalary', 'Tenure', 'TotalExperience']].dropna()

# --- Pair Plot ---

"""
Pair Plot:
Creates scatter plots between every pair of numerical variables and histograms on the diagonal.
Useful for getting an overall sense of correlations and variable interactions.
"""

# Plotting pair plot
sns.pairplot(pair_data)

# Display chart
plt.show()
```

### ✅ Interpretation:

- Helps identify **correlations, clusters, and outliers**

- Great exploratory tool for **modeling prep**

- Gets overwhelming with too many variables

---

## 🔹 Chart 17: **Treemap** – *Headcount Contribution by Department and Job Role*

```python
import squarify  # For Treemap

# --- Initial Exploration ---

# Combine Department and JobRole
df['Dept_Role'] = df['Department'] + " - " + df['JobRole']
role_counts = df['Dept_Role'].value_counts().head(15)  # Limit to top 15 for clarity

print("Top 15 Dept-Role Combinations:\n", role_counts)

# --- Treemap ---

"""
Treemap:
Uses nested rectangles to show hierarchical data and part-to-whole relationships.
Here, we visualize employee headcount by department and role.
"""

# Plotting treemap
plt.figure(figsize=(12, 6))
squarify.plot(sizes=role_counts.values, label=role_counts.index, alpha=0.8)

# Chart formatting
plt.title('Headcount by Department-Role Combination')
plt.axis('off')

# Display chart
plt.tight_layout()
plt.show()
```

### ✅ Interpretation:

- Emphasizes **contributions and hierarchy**

- Good when category values differ significantly

- Labels can get cramped with too many items

---

## 🔹 Chart 18: **Count Plot** – *Job Satisfaction Distribution*

```python
# --- Initial Exploration ---

# Check unique values
print("Unique Satisfaction Scores:", df['JobSatisfaction'].unique())

# --- Count Plot ---

"""
Count Plot:
Bar chart for categorical values directly from data. Here, it shows frequency of satisfaction levels.
Often used in survey or ordinal scale analysis.
"""

# Plotting count plot
plt.figure(figsize=(7, 5))
sns.countplot(x='JobSatisfaction', data=df)

# Chart formatting
plt.title('Job Satisfaction Ratings')
plt.xlabel('Satisfaction Level (1–5)')
plt.ylabel('Number of Employees')

# Display chart
plt.tight_layout()
plt.show()
```

### ✅ Interpretation:

- Clear view of **mode and distribution**

- Very useful for **ordinal and survey scales**

- Doesn’t show proportions (unless normalized)

---

## 🔹 Chart 19: **Swarm Plot** – *Monthly Salary Spread by Gender*

```python
# --- Initial Exploration ---

# View overall spread
print(df.groupby('Gender')['MonthlySalary'].describe())

# --- Swarm Plot ---

"""
Swarm Plot:
Displays all individual data points with minimal overlap.
Helps visualize clusters, outliers, and distribution more granularly than box plots.
"""

# Plotting swarm plot
plt.figure(figsize=(8, 5))
sns.swarmplot(x='Gender', y='MonthlySalary', data=df)

# Chart formatting
plt.title('Monthly Salary Spread by Gender')
plt.xlabel('Gender')
plt.ylabel('Monthly Salary')

# Display chart
plt.tight_layout()
plt.show()
```

### ✅ Interpretation:

- Useful for **seeing individual data points**

- Complements box/violin plots with more detail

- Can become cluttered for large datasets

---

## 🔹 Chart 20: **Facet Grid** – *Age vs Salary by Department and Gender*

```python
# --- Initial Exploration ---

# Select a smaller subset to avoid clutter (optional)
subset = df[df['Department'].isin(df['Department'].unique()[:4])]  # First 4 depts

# --- Facet Grid ---

"""
Facet Grid:
Small multiples of scatter plots for subgroups. Here, we examine age vs salary across departments and genders.
Helps compare patterns across categories.
"""

# Plotting facet grid
g = sns.FacetGrid(subset, col='Department', row='Gender', height=4)
g.map_dataframe(sns.scatterplot, x='Age', y='MonthlySalary')

# Add titles
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle('Age vs Salary by Department and Gender')

# Display chart
plt.show()
```

### ✅ Interpretation:

- Great for **comparative subgroup analysis**

- Helps detect **group-specific patterns**

- May require filtering for clarity

---

### ✅ ✅ Summary of Charts Covered

| Chart Type              | Use Case Example                     |
| ----------------------- | ------------------------------------ |
| Bar, Pie, Donut         | Distribution by category             |
| Histogram, KDE          | Numeric distribution                 |
| Line, Area              | Trend over time                      |
| Scatter, Bubble         | Relationships between variables      |
| Box, Violin, Swarm      | Spread and outliers                  |
| Heatmap, Pair Plot      | Correlation analysis                 |
| Count, Stacked, Grouped | Frequency and composition            |
| Treemap, Facet Grid     | Hierarchy and multi-view exploration |

---


