# Log File Analyzer

## 1. Project Title

**Log File Analyzer**

## 2. Project Description

Log File Analyzer is a Python-based application that reads a text log file, analyzes the log entries, and generates a summary report.

The application identifies different log levels such as INFO, WARNING, and ERROR. It counts each log type, displays all ERROR logs separately, and identifies the most frequently occurring log type.

## 3. Objectives

The main objectives of this project are:

* To read log data from a text file.
* To count INFO, WARNING, and ERROR logs.
* To display ERROR logs separately.
* To find the most frequent log type.
* To generate a clear summary report.
* To handle invalid log entries gracefully.
* To handle missing files and permission errors.

## 4. Features

* Text file log analysis
* INFO log counting
* WARNING log counting
* ERROR log counting
* Separate ERROR log display
* Most frequent log type detection
* Invalid log format validation
* Empty line handling
* File not found handling
* Permission error handling
* UTF-8 encoding error handling
* Structured summary report

## 5. Technologies Used

* **Programming Language:** Python
* **File Handling:** Python File I/O
* **Data Processing:** Counter
* **Data Structure:** Dataclass
* **Path Handling:** pathlib
* **Exception Handling:** try-except

## 6. Log Format

The application expects log entries in the following format:

```text
YYYY-MM-DD HH:MM:SS LEVEL - MESSAGE
```

Example:

```text
2026-06-06 08:00:01 INFO - Server initialized.
2026-06-06 08:05:12 WARNING - High memory usage detected.
2026-06-06 08:10:45 ERROR - Database connection timeout.
```

## 7. Output

The application generates a summary report containing:

* Total Logs
* Total INFO Logs
* Total WARNING Logs
* Total ERROR Logs
* Invalid Log Entries
* Most Frequent Log Type

It also displays all ERROR logs separately.

## 8. Validation and Exception Handling

The application handles the following cases:

### Missing File

If the specified log file does not exist, an appropriate error message is displayed.

### Permission Error

If the application does not have permission to read the file, a permission error is displayed.

### Invalid Log Entry

Invalid log entries are detected and reported without stopping the complete analysis.

### Empty Lines

Empty lines are ignored during log processing.

## 9. Sample Result

```text
==================================================
              LOG SUMMARY REPORT
==================================================
Total Logs                    : 6
Total INFO Logs               : 3
Total WARNING Logs            : 1
Total ERROR Logs              : 2
Invalid Log Entries           : 0
Most Frequent Log Type        : INFO
==================================================

--- ERROR LOGS ---
1. 2026-06-06 08:10:45 ERROR - Database connection timeout.
2. 2026-06-06 08:20:11 ERROR - Null pointer exception in module X.
--------------------------------------------------
```

## 10. Conclusion

The Log File Analyzer provides a simple and reliable way to analyze application log files. It summarizes important log information, identifies frequent log types, displays ERROR entries separately, and handles common file and data validation errors gracefully.

```


