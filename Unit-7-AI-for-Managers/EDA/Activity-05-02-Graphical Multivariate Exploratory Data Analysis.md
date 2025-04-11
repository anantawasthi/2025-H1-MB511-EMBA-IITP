Perfect! Let’s continue with **Activity 5.2: Graphical Multivariate Analysis** — where we’ll **visualize the interaction between 3 or more variables**. These plots are great for presentations and storytelling, especially when you want to highlight **intersections and layered insights** (e.g., how engagement and tenure together affect attrition by department).

---

# ✅ **Activity 5.2: Graphical Multivariate Exploratory Data Analysis**

---

### 🧭 1. Activity Introduction

When two variables don’t tell the full story, we bring in a third (or more) to:

- Reveal interactions

- Uncover compound risk segments

- Visually explore clusters or decision patterns

In this activity, we’ll use:

- **Facet plots** (small multiples)

- **Grouped bar charts**

- **Hue & style in scatter plots**

- **Stacked categorical visualizations**

---

### 💻 2. Python Code — Multivariate Plots

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Set aesthetics
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 5)

# 1. Facet plot: Engagement vs Tenure, separated by Resigned
g = sns.FacetGrid(df, col='Resigned', height=5, aspect=1)
g.map_dataframe(sns.scatterplot, x='Tenure_Months', y='Engagement_Score', hue='Department', alpha=0.7)
g.add_legend()
g.fig.suptitle("🎯 Engagement vs Tenure by Resigned Status", fontsize=14, y=1.05)
plt.show()

# 2. Grouped bar plot: Resigned % by Engagement Level and Tenure Group
pivot_data = pd.crosstab(index=[df['Engagement_Level'], df['Tenure_Group']], 
                         columns=df['Resigned'], normalize='index') * 100
pivot_data = pivot_data.reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=pivot_data, x='Engagement_Level', y='Yes', hue='Tenure_Group')
plt.title("📉 Attrition Rate by Engagement and Tenure Segments")
plt.ylabel("Resigned (%)")
plt.xlabel("Engagement Level")
plt.ylim(0, 100)
plt.legend(title='Tenure Group')
plt.show()

# 3. Multicolor scatter plot: Salary vs Age colored by Resigned
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df, x='Age', y='Salary', hue='Resigned', style='Department', alpha=0.6)
plt.title("💰 Salary vs Age by Resigned Status and Department")
plt.show()
```

---

### 📊 3. Results (What You’ll See)

#### ✅ Facet Plot: Tenure vs Engagement by Resigned

- Left: Resigned employees — clustered in low engagement, low tenure

- Right: Retained employees — more spread, higher engagement, broader tenure range

- Coloring by Department shows Sales clusters toward risk

#### ✅ Grouped Bar: Resigned % by Engagement + Tenure

- Clear spike in attrition when **Engagement = Low** and **Tenure < 2 years**

- Low attrition among **High Engagement + 5+ years**

#### ✅ Scatter: Salary vs Age by Department + Resigned

- Some outliers in Sales and IT at younger ages with high salaries

- Retained employees are more densely distributed in middle age/salary zone

---

### 🧠 4. Results Discussion

| Visual          | Key Takeaway                                                                             |
| --------------- | ---------------------------------------------------------------------------------------- |
| **Facet Plot**  | Engagement is a strong visual separator — disengaged = higher churn, especially in Sales |
| **Grouped Bar** | Dual risk zones emerge clearly — short-tenure + low-engagement = 🔥                      |
| **Scatter**     | Age + salary vary by department — use for compensation and retention segmentation        |

---

✅ These visuals are ideal for:

- Leadership presentations

- Segmented HR interventions

- Building dynamic dashboards in Excel or Power BI

Ready to close Activity 5 with: **Activity 5.3 – Statistical Multivariate Relationships**?

We'll explore:

- Interaction testing

- Correlation matrices

- Multi-group ANOVA (if needed)

Shall we proceed?
