## 📥 Common Data Sources (Import with Pandas)

| Format / Source          | Function Used                           | Notes                                              |
| ------------------------ | --------------------------------------- | -------------------------------------------------- |
| **CSV File**             | `pd.read_csv()`                         | Most common; can handle large plain-text datasets  |
| **Excel File**           | `pd.read_excel()`                       | Supports `.xls` and `.xlsx`; can select sheet      |
| **JSON**                 | `pd.read_json()`                        | For structured data in JSON format                 |
| **SQL Database**         | `pd.read_sql()` / `read_sql_query()`    | Needs a connection engine (e.g., via SQLAlchemy)   |
| **Parquet**              | `pd.read_parquet()`                     | Efficient columnar storage; often used in big data |
| **HTML Tables**          | `pd.read_html()`                        | Parses HTML tables from web pages                  |
| **Clipboard**            | `pd.read_clipboard()`                   | Reads tabular data copied to clipboard             |
| **Google Sheets**        | Indirect (via `gspread` or `pygsheets`) | Requires API setup                                 |
| **Pickle Format**        | `pd.read_pickle()`                      | Fastest format for internal Pandas storage         |
| **Feather / ORC / Avro** | `pd.read_feather()`, etc.               | Often used in data engineering workflows           |

---

## 📤 Common Data Destinations (Export from Pandas)

| Format / Destination     | Function Used           | Notes                                             |
| ------------------------ | ----------------------- | ------------------------------------------------- |
| **CSV File**             | `df.to_csv()`           | Saves tabular data into plain-text files          |
| **Excel File**           | `df.to_excel()`         | Exports data into an Excel workbook               |
| **JSON**                 | `df.to_json()`          | Saves data in a JSON-compatible structure         |
| **SQL Table**            | `df.to_sql()`           | Sends data to a database table via SQLAlchemy     |
| **Parquet**              | `df.to_parquet()`       | Saves data in a compressed, efficient format      |
| **Clipboard**            | `df.to_clipboard()`     | Copies data to system clipboard for quick pasting |
| **Pickle File**          | `df.to_pickle()`        | Saves DataFrame for fast reloads                  |
| **Feather / ORC / Avro** | `df.to_feather()`, etc. | For optimized analytics pipelines                 |


