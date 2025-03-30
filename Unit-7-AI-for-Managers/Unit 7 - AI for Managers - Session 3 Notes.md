# 📘 Python Standard Libraries: `os`, `shutil`, and `datetime`

---

## 🔹 Section 1: Introduction to Standard Libraries

### What are Standard Libraries?

Python's **standard library** is a robust suite of modules and packages included with every installation of Python. These libraries enable developers to perform a wide range of tasks such as string manipulation, file operations, system interactions, and data/time processing without the need for third-party installations. For managers and analysts, this means efficient development with fewer dependencies and improved stability.

### Why Learn `os`, `shutil`, and `datetime`?

Each of these libraries serves a distinct purpose in automating business processes:

- The `os` module allows interaction with the operating system, such as navigating file systems and managing directories.

- The `shutil` module extends the capabilities of `os` by enabling high-level file operations like copying, moving, and archiving.

- The `datetime` module provides functions for manipulating and formatting dates and times, essential for logging, report generation, and scheduling.

Understanding these libraries is fundamental for anyone building automated data pipelines, processing logs, or managing a structured data repository.

### Real-World Managerial Applications

| Scenario               | Use Case                                                                           | Relevant Library           |
| ---------------------- | ---------------------------------------------------------------------------------- | -------------------------- |
| Report Generation      | Automatically create monthly or quarterly report folders based on the current date | `os`, `datetime`           |
| Backup Automation      | Programmatically copy and zip project files for backup or archival purposes        | `shutil`                   |
| Performance Dashboards | Timestamp logs or output files with current date and time for audit tracking       | `datetime`                 |
| Compliance             | Automatically delete or move old files that exceed retention periods               | `os`, `shutil`, `datetime` |

---

## 🔹 Section 2: The `os` Library – Operating System Interface

### 2.1 Basics of the `os` Module

The `os` module is part of Python's standard utility modules and allows users to interact with the operating system in a portable way. It is especially useful for navigating directories, accessing environment variables, and performing file-based operations.

```python
import os

# Get the current working directory
print("Current Directory:", os.getcwd())

# List all files and folders in the current directory
print("Contents:", os.listdir())
```

These commands help in understanding the current workspace and its contents, which is useful when working with dynamically generated paths or verifying script execution environments.

### Key Functions

| Function               | Description                                                                     |
| ---------------------- | ------------------------------------------------------------------------------- |
| `os.getcwd()`          | Returns the current working directory, useful for debugging and setting context |
| `os.listdir(path)`     | Lists contents of a given directory to confirm file availability                |
| `os.path.exists(path)` | Checks if a file/folder exists before attempting operations to avoid errors     |
| `os.path.join()`       | Joins directory and file paths safely using OS-appropriate separators           |
| `os.path.isfile(path)` | Checks if a given path refers to a file (not a folder)                          |
| `os.path.isdir(path)`  | Checks if a given path refers to a directory (not a file)                       |

```python
# Safe way to join paths
project_dir = os.path.join("reports", "2025", "March")
print(project_dir)
```

---

### 2.2 Directory Management

These functions allow users to create, rename, and delete directories. Such tasks are crucial in automating the creation of new folders for client reports or departmental submissions.

```python
# Create a single directory
os.mkdir("new_folder")

# Create nested directories
os.makedirs("projects/2025/March")

# Rename a directory
os.rename("old_folder", "renamed_folder")

# Delete an empty directory
os.rmdir("new_folder")

# Delete nested directories
os.removedirs("projects/2025/March")
```

> 🔍 **Managerial Tip:** Automating directory creation and cleanup can reduce manual error and streamline regular reporting cycles.

---

### 2.3 Example Use Case

**Automating Monthly Report Folders**

This script uses `os` and `datetime` to dynamically generate a folder structure for storing reports by month and year. This is commonly required in corporate environments for organizing documentation.

```python
import os
import datetime

month_name = datetime.datetime.now().strftime("%B")
year = datetime.datetime.now().year

path = os.path.join("reports", str(year), month_name)
if not os.path.exists(path):
    os.makedirs(path)
```

---

## 🔹 Section 3: The `shutil` Library – High-Level File Operations

The `shutil` module builds upon the functionality of `os` by providing a higher-level interface for file operations such as copying entire directories, archiving, and moving folders.

### 3.1 Copying and Moving Files

```python
import shutil

# Copy a file (basic)
shutil.copy("data.txt", "backup/data.txt")

# Copy a file including metadata
shutil.copy2("data.txt", "backup/data_with_metadata.txt")

# Move file
shutil.move("data.txt", "archive/data.txt")

# Remove a directory tree
shutil.rmtree("old_reports")
```

> ⚠️ **Caution:** Always confirm before using `shutil.rmtree()` as it will irreversibly delete the entire directory tree.

### Managerial Relevance:

- Use copying to maintain file backups before updates.

- Move files after processing to avoid duplicate execution.

- Delete obsolete folders to maintain disk hygiene.

---

### 3.2 Archiving and Backup

```python
# Create a ZIP archive of the reports folder
shutil.make_archive("backup_2025_March", 'zip', "reports/2025/March")

# Extract the archive
shutil.unpack_archive("backup_2025_March.zip", "restored_reports")
```

> 📁 **Managerial Tip:** Automating the compression of folders at the end of each reporting cycle can simplify email transfers and ensure historical backup.

---

## 🔹 Section 4: The `datetime` Library – Time and Date Handling

The `datetime` module helps developers and analysts work with real-world temporal data. This includes generating timestamps for logs, formatting reports, calculating deadlines, and auditing changes.

### 4.1 Getting Current Date and Time

```python
import datetime

today = datetime.date.today()
now = datetime.datetime.now()

print("Today:", today)
print("Now:", now)
```

These values provide a snapshot of current system time, helpful for versioning, timestamping, and daily automated script runs.

### 4.2 Formatting and Parsing Dates

```python
# Convert datetime to string
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted:", formatted)

# Parse string to datetime
parsed = datetime.datetime.strptime("2025-03-30", "%Y-%m-%d")
print("Parsed:", parsed)
```

Using `strftime()` and `strptime()` ensures consistent formatting for filenames, logs, or user-friendly reporting.

### 4.3 Timedelta for Date Arithmetic

```python
# Time difference
from datetime import timedelta

future = now + timedelta(days=7)
past = now - timedelta(days=3)

print("Next Week:", future)
print("Three Days Ago:", past)
```

Date arithmetic is essential in workflows involving deadlines, data aging, or forecasting future events.

---

### Example: Timestamping Reports

```python
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"report_{timestamp}.csv"
print("Report name:", filename)
```

This allows automated generation of unique filenames that include timestamps to avoid overwriting files.

---

## 🔹 Section 5: Mini Project – Automated Report Folder Generator

### Objective:

To build a complete mini-automation system that:

- Generates a folder path based on the current date

- Ensures idempotency (does not duplicate folders if they already exist)

- Backs up the contents using compression

### Code:

```python
"""
📂 Automated Report Folder Generator
Creates a folder with current month/year, timestamps old reports, and backs them up.
"""

import os
import shutil
from datetime import datetime

# Step 1: Define folder path
month = datetime.now().strftime("%B")
year = datetime.now().year
folder_name = f"{month}_{year}"
report_path = os.path.join("reports", str(year), month)

# Step 2: Create folder if not exists
if not os.path.exists(report_path):
    os.makedirs(report_path)
    print("Report folder created:", report_path)
else:
    print("Folder already exists:", report_path)

# Step 3: Backup old reports
backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
shutil.make_archive(backup_name, 'zip', report_path)
print("Backup created:", backup_name + ".zip")
```

---

## 🔹 Section 6: Summary and Best Practices

| Topic      | Best Practices                                                                                                                 |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `os`       | Always use `os.path.join()` instead of string concatenation to build file paths, ensuring cross-platform compatibility         |
| `shutil`   | Use `shutil.copy2()` when preserving metadata is important; double-check before using `rmtree()` to avoid accidental deletions |
| `datetime` | Standardize time formats across logs and reports using `strftime()` and maintain readability with ISO formats when possible    |
| Automation | Integrate all three libraries in data pipelines to automate and structure report generation, file management, and archiving    |
| Debugging  | Use logging or conditional print statements for better visibility during development and debugging phases                      |

These practices ensure your automation scripts are robust, maintainable, and production-ready.



# 

---

## 🔹 Section 7: Code Exercises and Case Studies for Class Discussion

### 🧪 Exercise 1: Clean-up Old Backup Files

**Objective:** Write a Python script to automatically delete backup `.zip` files older than 30 days from a specified backup directory.

```python
"""
📁 Cleanup Script
Deletes `.zip` files older than 30 days from the backup directory.
"""

import os
import time
from datetime import datetime, timedelta

backup_dir = "backups"
now = time.time()
cutoff = now - (30 * 86400)  # 30 days in seconds

if os.path.exists(backup_dir):
    for filename in os.listdir(backup_dir):
        filepath = os.path.join(backup_dir, filename)
        if filepath.endswith(".zip") and os.path.isfile(filepath):
            file_creation = os.path.getctime(filepath)
            if file_creation < cutoff:
                os.remove(filepath)
                print(f"Deleted: {filename}")
else:
    print("Backup directory not found.")
```

---

### 🧪 Exercise 2: Auto-Generate Quarterly Reports Folder Structure

**Objective:** Create nested folders automatically for a full year’s quarters, e.g., `/2025/Q1`, `/2025/Q2`, etc.

```python
import os

year = 2025
quarters = ["Q1", "Q2", "Q3", "Q4"]

for q in quarters:
    folder_path = os.path.join("reports", str(year), q)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created: {folder_path}")
```

> 📌 **Class Prompt:** Modify this to create folders for multiple years from 2022 to 2025.

---

### 🧪 Exercise 3: Date-Based File Renaming for Reports

**Objective:** Rename all `.csv` files in a folder to include a timestamp suffix.

```python
import os
import datetime

folder = "monthly_data"
timestamp = datetime.datetime.now().strftime("%Y%m%d")

for filename in os.listdir(folder):
    if filename.endswith(".csv"):
        base, ext = os.path.splitext(filename)
        new_name = f"{base}_{timestamp}{ext}"
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
        print(f"Renamed: {filename} -> {new_name}")
```

---

### 🧪 Case Study 1: Automating Departmental Reporting

**Background:** The HR department creates monthly reports for each region. Manually managing the directory and archiving the reports is time-consuming.

**Goal:** Use `os`, `shutil`, and `datetime` to automate:

- Folder creation for each region

- Copying a report template into each folder

- Archiving previous month’s folders

**Code Template:**

```python
import os
import shutil
from datetime import datetime

regions = ["North", "South", "East", "West"]
base_dir = "HR_Reports"
template_file = "report_template.docx"

month = datetime.now().strftime("%B")
year = datetime.now().year

for region in regions:
    path = os.path.join(base_dir, region, str(year), month)
    os.makedirs(path, exist_ok=True)
    shutil.copy(template_file, os.path.join(path, f"{region}_report_{month}.docx"))
    print(f"Created and copied for {region}")

# Archive last month (optional advanced)
prev_month = (datetime.now().replace(day=1) - timedelta(days=1)).strftime("%B")
prev_path = os.path.join(base_dir, "North", str(year), prev_month)
if os.path.exists(prev_path):
    archive_name = f"{prev_path}_archive"
    shutil.make_archive(archive_name, 'zip', prev_path)
    print(f"Archived {prev_path} to {archive_name}.zip")
```

---

### 🧪 Case Study 2: Generating Compliance Logs

**Background:** Your compliance officer needs daily log files generated with timestamps and archived weekly.

**Solution Outline:**

- Use `datetime` to create a new `.log` file daily

- Write simulated log content

- At the end of the week, compress all `.log` files into a zip archive

**Implementation (for daily run):**

```python
import os
from datetime import datetime

log_dir = "compliance_logs"
os.makedirs(log_dir, exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")
log_file = os.path.join(log_dir, f"log_{today}.txt")

with open(log_file, "w") as f:
    f.write(f"Compliance check on {today}\n")
    f.write("All systems operating normally.\n")

print(f"Log created: {log_file}")
```

> 💡 **Weekly Archival Exercise:** Students can write a script to zip all `.txt` logs from the last 7 days into `weekly_compliance.zip`

---
