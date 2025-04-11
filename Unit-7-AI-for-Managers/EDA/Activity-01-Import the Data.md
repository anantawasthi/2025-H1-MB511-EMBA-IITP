

# ✅ **Activity 1: Import the Data**

---

### 🧭 1. Activity Introduction

Before we can explore the data, we must first **import it** into Python. This step ensures we can:

- Access the file

- Convert it into a **DataFrame** for analysis

- Prepare for cleaning, visualizations, and insights

The dataset we’re using is:

> `HR_Attrition_Dataset_1000.xlsx`  
> A synthetic HR dataset with 1,000 employee records across multiple departments.

---

### 💻 2. Python Code (Beginner-Friendly Script Format)

```python
# Step 1: Import the pandas library
import pandas as pd  # pandas is used for working with data tables in Python

# Step 2: Define the file path to your dataset
file_path = "HR_Attrition_Dataset_1000.xlsx"  # Update this path if the file is located elsewhere

# Step 3: Read the Excel file and store it in a DataFrame
df = pd.read_excel(file_path)

# Step 4: Display a success message
print("✅ Dataset has been successfully imported.")
```

---

### 🧾 3. Results

Once the code runs correctly, you’ll see:

```
✅ Dataset has been successfully imported.
```

And you’ll now have a DataFrame named `df` that holds all your data. You can test this by running:

```python
df.head()  # Displays the first 5 rows of the dataset
```

---

### 🧠 4. Results Discussion

This step confirms that:

- The file is available and readable

- Python recognizes the dataset as a **DataFrame**, which we can manipulate and analyze

- We’re ready to begin structural checks and early exploration


