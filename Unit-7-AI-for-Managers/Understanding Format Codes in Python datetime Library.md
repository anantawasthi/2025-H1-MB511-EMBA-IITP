# 📘 Understanding Format Codes in Python's `datetime` Library

---

## 🔹 Chapter Overview

The `datetime` module in Python provides robust tools to work with dates and times. A crucial part of this functionality is **formatting** and **parsing** date and time strings using `strftime()` and `strptime()` methods. These methods rely on **format codes**, special placeholders that represent components like year, month, day, hour, minute, etc.

Understanding these format codes helps in converting `datetime` objects to human-readable strings and vice versa, making them useful in logging, file naming, data transformation, and user interfaces.

---

## 🔹 `strftime()` vs `strptime()`

The `strftime()` and `strptime()` functions are essential for working with date and time formatting and parsing in Python:

- `strftime()` stands for **String Format Time**: It takes a `datetime` object and converts it into a string representation, using format codes to specify the layout.

- `strptime()` stands for **String Parse Time**: It takes a string representing a date/time and converts it into a `datetime` object, using the same format codes to interpret the string structure.

These functions are widely used in:

- Creating readable timestamps for logging and filenames

- Parsing input from users or files into `datetime` objects

- Reformatting dates between systems or locales

| Method       | Description                                                 |
| ------------ | ----------------------------------------------------------- |
| `strftime()` | Converts a `datetime` object to a string using format codes |
| `strptime()` | Parses a string into a `datetime` object using format codes |

### Example

```python
from datetime import datetime

now = datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")  # Formatting
parsed = datetime.strptime("2025-03-30 14:35:00", "%Y-%m-%d %H:%M:%S")  # Parsing
```

---

## 🔹 Commonly Used Format Codes

### 📅 Date Components

| Code | Meaning                                       | Example  |
| ---- | --------------------------------------------- | -------- |
| `%Y` | 4-digit year                                  | `2025`   |
| `%y` | 2-digit year                                  | `25`     |
| `%m` | Month (01 to 12)                              | `03`     |
| `%B` | Full month name                               | `March`  |
| `%b` | Abbreviated month name                        | `Mar`    |
| `%d` | Day of the month (01 to 31)                   | `30`     |
| `%A` | Full weekday name                             | `Sunday` |
| `%a` | Abbreviated weekday name                      | `Sun`    |
| `%j` | Day of the year (001 to 366)                  | `089`    |
| `%U` | Week number of the year (Sunday as first day) | `13`     |
| `%W` | Week number (Monday as first day)             | `13`     |

### 🕓 Time Components

| Code | Meaning                        | Example        |
| ---- | ------------------------------ | -------------- |
| `%H` | Hour (00 to 23)                | `14`           |
| `%I` | Hour (01 to 12)                | `02`           |
| `%p` | AM or PM                       | `PM`           |
| `%M` | Minute (00 to 59)              | `35`           |
| `%S` | Second (00 to 59)              | `00`           |
| `%f` | Microsecond (000000 to 999999) | `123456`       |
| `%Z` | Time zone name                 | `UTC` (if set) |
| `%z` | UTC offset                     | `+0530`        |

### 🗓️ Combined Codes

| Code | Meaning             | Example                        |
| ---- | ------------------- | ------------------------------ |
| `%c` | Local date and time | `Sun Mar 30 14:35:00 2025`     |
| `%x` | Local date          | `03/30/25` (depends on locale) |
| `%X` | Local time          | `14:35:00` (depends on locale) |

---

## 🔹 Practical Examples

### 📁 Timestamped Filename

```python
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"report_{timestamp}.csv"
print(filename)  # Example: report_20250330_143500.csv
```

### 📋 User-Friendly Date Format

```python
from datetime import datetime

print(datetime.now().strftime("%A, %B %d, %Y"))  # Example: Sunday, March 30, 2025
```

### 🔍 Parsing a Date String

```python
from datetime import datetime

date_str = "30-03-2025"
parsed_date = datetime.strptime(date_str, "%d-%m-%Y")
print(parsed_date)  # Output: 2025-03-30 00:00:00
```

---

## 🔹 Best Practices

- Always match the format string in `strptime()` to the input string exactly.

- Use ISO formats (`%Y-%m-%d %H:%M:%S`) for standardization and compatibility.

- Combine `strftime()` with file operations for versioned outputs.

- Use `%A` and `%B` when presenting to users for better readability.

- Use `%Y%m%d_%H%M%S` for compact and sortable timestamp formats.

---

## 🔹 Example: All Format Codes Together

```python
"""
Demonstrate formatting with all major datetime format codes.
Useful as a consolidated reference or for testing output layouts.
"""
from datetime import datetime

now = datetime.now()

print("Year (4-digit):", now.strftime("%Y"))
print("Year (2-digit):", now.strftime("%y"))
print("Month (number):", now.strftime("%m"))
print("Month (full):", now.strftime("%B"))
print("Month (abbr):", now.strftime("%b"))
print("Day (number):", now.strftime("%d"))
print("Weekday (full):", now.strftime("%A"))
print("Weekday (abbr):", now.strftime("%a"))
print("Day of year:", now.strftime("%j"))
print("Week number (Sunday):", now.strftime("%U"))
print("Week number (Monday):", now.strftime("%W"))

print("Hour (24h):", now.strftime("%H"))
print("Hour (12h):", now.strftime("%I"))
print("AM/PM:", now.strftime("%p"))
print("Minute:", now.strftime("%M"))
print("Second:", now.strftime("%S"))
print("Microsecond:", now.strftime("%f"))

print("Time zone name:", now.strftime("%Z"))
print("UTC offset:", now.strftime("%z"))

print("Locale datetime (%c):", now.strftime("%c"))
print("Locale date (%x):", now.strftime("%x"))
print("Locale time (%X):", now.strftime("%X"))
```

---


