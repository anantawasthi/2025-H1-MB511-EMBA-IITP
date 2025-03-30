# 📘 Python Standard Libraries: `os`, `shutil`, and `datetime`

---

#### These examples focus on individual libraries—`os`, `shutil`, and `datetime`—with expanded docstrings and explanatory comments. They are suitable for classroom walkthroughs and beginner-level exercises. Each code snippet also includes **line-by-line documentation using comments** to aid understanding.

---

## `os` Library Examples

#### ✅ Example 1.1: Get Current Working Directory

```python
"""
Example 1.1: Retrieve the current working directory.
This is useful when your script depends on local file paths or when you're unsure where the script is running.
"""
import os

# Get the current directory in which this script is executing
cwd = os.getcwd()

# Display the directory path to the user
print("Current working directory:", cwd)
```

---

#### ✅ Example 1.2: List Files and Folders in a Directory

```python
"""
Example 1.2: List the contents of a directory.
This helps in understanding what files or subfolders are present, especially useful before processing files.
"""
import os

# Use '.' to refer to the current directory
contents = os.listdir(".")

# Print the list of files and folders
print("Contents of current directory:", contents)
```

---

#### ✅ Example 1.3: Check if a File or Folder Exists

```python
"""
Example 1.3: Use os.path.exists() to verify if a file or folder exists.
Avoids errors from trying to access or create existing paths.
"""
import os

# Check if a folder named 'data' exists in the current directory
if os.path.exists("data"):
    print("The 'data' folder exists.")
else:
    print("The 'data' folder does not exist.")
```

---

#### ✅ Example 1.4: Create and Delete Directories

```python
"""
Example 1.4: Dynamically create and delete nested directories.
This supports project structuring and cleanup operations.
"""
import os

# Create nested directories, use exist_ok=True to avoid error if it already exists
os.makedirs("new_folder/test", exist_ok=True)
print("Folder 'new_folder/test' created.")

# Remove the nested directory structure in reverse
os.removedirs("new_folder/test")
print("Folder 'new_folder/test' deleted.")
```

---

#### ✅ Example 1.5: Rename Files or Folders

```python
"""
Example 1.5: Rename an existing file or folder.
Important for reorganization or versioning of files.
"""
import os

# Rename a file named 'old.txt' to 'new.txt'
os.rename("old.txt", "new.txt")
print("File renamed from 'old.txt' to 'new.txt'")
```

---

## `shutil` Library Examples

#### ✅ Example 2.1: Copy a File

```python
"""
Example 2.1: Copy a file to another directory.
Used in backup or file duplication workflows.
"""
import shutil

# Copy 'report.docx' into the 'backup' directory
shutil.copy("report.docx", "backup/report.docx")
print("File copied to backup folder.")
```

---

#### ✅ Example 2.2: Copy File with Metadata

```python
"""
Example 2.2: Copy a file while preserving its metadata (e.g., timestamps).
Useful when copying files for compliance or audit.
"""
import shutil

# Copy and preserve file metadata such as creation and modification times
shutil.copy2("report.docx", "backup/report_with_meta.docx")
print("File copied with metadata preserved.")
```

---

#### ✅ Example 2.3: Move a File

```python
"""
Example 2.3: Move a file from one location to another.
Helps in organizing processed or archived files.
"""
import shutil

# Move the file to the archive folder
shutil.move("report.docx", "archive/report.docx")
print("File moved to archive folder.")
```

---

#### ✅ Example 2.4: Remove a Directory Tree

```python
"""
Example 2.4: Delete a directory and all its contents.
Should be used cautiously as this action is irreversible.
"""
import shutil

# Completely remove the 'old_reports' folder along with its files/subfolders
shutil.rmtree("old_reports")
print("Deleted the 'old_reports' folder and all its contents.")
```

---

#### ✅ Example 2.5: Create and Extract ZIP Archive

```python
"""
Example 2.5: Archive a folder into ZIP format and extract it.
Useful for data backup, sharing, or compression before upload.
"""
import shutil

# Create a ZIP file from 'reports' folder
shutil.make_archive("reports_2025_March", "zip", "reports")

# Extract the ZIP archive into 'restored_reports'
shutil.unpack_archive("reports_2025_March.zip", "restored_reports")
print("Archive created and extracted.")
```

---

## `datetime` Library Examples

#### ✅ Example 3.1: Get Today’s Date and Current Time

```python
"""
Example 3.1: Print today's date and current time.
Useful for time-stamping logs, events, or records.
"""
from datetime import date, datetime

# Get today's date
print("Today's Date:", date.today())

# Get full timestamp including time
print("Current DateTime:", datetime.now())
```

---

#### ✅ Example 3.2: Format Date and Time as a String

```python
"""
Example 3.2: Convert datetime to a human-readable or file-safe format.
This is often used in filenames and report headers.
"""
from datetime import datetime

# Capture current timestamp
now = datetime.now()

# Format the datetime object to a string
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted DateTime:", formatted)
```

---

#### ✅ Example 3.3: Parse a Date String into datetime Object

```python
"""
Example 3.3: Convert a date string to a datetime object.
Allows operations like comparison or time arithmetic.
"""
from datetime import datetime

# Define a date in string format
date_str = "2025-03-30"

# Parse string to datetime object
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
print("Parsed Date:", parsed_date)
```

---

#### ✅ Example 3.4: Add or Subtract Days Using timedelta

```python
"""
Example 3.4: Use timedelta to add or subtract days.
Useful for deadline calculation or schedule planning.
"""
from datetime import datetime, timedelta

# Get today's date and time
today = datetime.now()

# Subtract one day for 'yesterday'
yesterday = today - timedelta(days=1)

# Add 7 days to get the date for next week
next_week = today + timedelta(days=7)

# Output both modified dates
print("Yesterday:", yesterday)
print("Next Week:", next_week)
```

---

#### ✅ Example 3.5: Generate Timestamp for Unique Filenames

```python
"""
Example 3.5: Create a unique filename using the current timestamp.
Useful for logging, backup files, or daily reports.
"""
from datetime import datetime

# Create a timestamp in YYYYMMDD_HHMMSS format
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Generate a unique filename
filename = f"log_{timestamp}.txt"
print("Generated filename:", filename)
```

# 📘 Python Standard Libraries Use Cases: Combining `os`, `shutil`, and `datetime`

---

## 🔹 Real-World Use Cases

This section demonstrates how to combine the power of `os`, `shutil`, and `datetime` libraries to automate tasks such as creating folders, copying files, and timestamping backups. These use cases mirror real-world reporting, logging, and archiving workflows often seen in data operations, HR departments, and compliance teams.

---

### ✅ Use Case 1: Automated Report Folder Setup

```python
"""
Use Case 1: Automatically create a folder for the current month and year,
copy a report template into the folder, and name it with a timestamp.
"""
import os
import shutil
from datetime import datetime

# Step 1: Get current month and year
month = datetime.now().strftime("%B")
year = datetime.now().year

# Step 2: Define folder structure (e.g., reports/2025/March)
folder_path = os.path.join("reports", str(year), month)
os.makedirs(folder_path, exist_ok=True)
print("Created folder:", folder_path)

# Step 3: Copy a report template into the new folder with a timestamped name
template_file = "report_template.docx"
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
new_report_name = f"Monthly_Report_{timestamp}.docx"
destination = os.path.join(folder_path, new_report_name)
shutil.copy(template_file, destination)
print("Template copied to:", destination)
```

---

### ✅ Use Case 2: Daily Compliance Log Creation and Weekly Backup

```python
"""
Use Case 2: Generate a compliance log daily and back up logs weekly into a ZIP file.
"""
import os
import shutil
from datetime import datetime, timedelta

# Step 1: Create today's log
log_folder = "compliance_logs"
os.makedirs(log_folder, exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")
log_filename = f"log_{today}.txt"
log_path = os.path.join(log_folder, log_filename)

with open(log_path, 'w') as log_file:
    log_file.write(f"Compliance check for {today}\nStatus: OK\n")
print("Log file created:", log_path)

# Step 2: On Sundays, archive the week's logs (simulated here with manual call)
if datetime.now().weekday() == 6:  # 6 = Sunday
    archive_name = f"weekly_backup_{datetime.now().strftime('%Y%m%d')}"
    shutil.make_archive(archive_name, 'zip', log_folder)
    print("Weekly archive created:", archive_name + ".zip")
```

---

### ✅ Use Case 3: Cleanup of Old Backups

```python
"""
Use Case 3: Delete ZIP files older than 30 days from the backup directory
for disk space management and data retention policies.
"""
import os
import time

backup_dir = "backups"
os.makedirs(backup_dir, exist_ok=True)

# Define time threshold (30 days in seconds)
cutoff_time = time.time() - (30 * 86400)

# Loop through files and delete outdated ZIPs
for file in os.listdir(backup_dir):
    if file.endswith(".zip"):
        file_path = os.path.join(backup_dir, file)
        file_creation_time = os.path.getctime(file_path)
        if file_creation_time < cutoff_time:
            os.remove(file_path)
            print("Deleted old backup:", file)
```


