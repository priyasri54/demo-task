
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple


# ============================================================
# Data Model
# ============================================================

@dataclass
class LogReport:
    """
    Stores the complete log analysis report.
    """

    total_logs: int
    info_count: int
    warning_count: int
    error_count: int
    invalid_count: int
    most_frequent: str
    error_logs: List[str]


# ============================================================
# Log Line Parser
# ============================================================

def parse_log_line(
    line: str,
) -> Tuple[Optional[str], Optional[str]]:
    """
    Parses a single log line.

    Expected format:
        YYYY-MM-DD HH:MM:SS LEVEL - Message

    Example:
        2026-06-06 10:00:00 INFO - System started successfully
    """

    cleaned = line.strip()

    # Ignore empty lines
    if not cleaned:
        return None, None

    # Split the log into parts
    parts = cleaned.split(maxsplit=3)

    # Validate basic structure
    if len(parts) != 4:
        raise ValueError(
            "Invalid log format. Expected: "
            "TIMESTAMP LEVEL - MESSAGE"
        )

    date = parts[0]
    time = parts[1]
    level = parts[2].upper()
    separator = parts[3]

    # Validate date/time structure
    if len(date) != 10 or date[4] != "-" or date[7] != "-":
        raise ValueError(
            "Invalid date format."
        )

    if len(time) != 8 or time[2] != ":" or time[5] != ":":
        raise ValueError(
            "Invalid time format."
        )

    # Validate log level
    if level == "INFO":
        pass

    elif level == "WARNING":
        pass

    elif level == "ERROR":
        pass

    else:
        raise ValueError(
            f"Invalid log level: '{level}'"
        )

    # Validate separator/message
    if not separator.startswith("-"):
        raise ValueError(
            "Invalid log message format."
        )

    message = separator[1:].strip()

    if not message:
        raise ValueError(
            "Log message cannot be empty."
        )

    return level, cleaned


# ============================================================
# Analyze Log File
# ============================================================

def analyze_log_file(
    file_path: str | Path,
) -> Optional[LogReport]:
    """
    Reads and analyzes the specified log file.
    """

    path = Path(file_path)

    try:

        # ----------------------------------------------------
        # Check File Existence
        # ----------------------------------------------------

        if not path.exists():
            raise FileNotFoundError(
                f"The file '{path}' does not exist."
            )

        # ----------------------------------------------------
        # Check Whether Path Is a File
        # ----------------------------------------------------

        if not path.is_file():
            raise FileNotFoundError(
                f"'{path}' is not a valid file."
            )

        # ----------------------------------------------------
        # Counters
        # ----------------------------------------------------

        log_counts = Counter()

        error_logs: List[str] = []

        invalid_count = 0

        # ----------------------------------------------------
        # Read File
        # ----------------------------------------------------

        with path.open(
            "r",
            encoding="utf-8",
        ) as file:

            for line_number, line in enumerate(
                file,
                start=1,
            ):

                try:

                    level, parsed_line = parse_log_line(
                        line
                    )

                    # Ignore empty lines
                    if level is None:
                        continue

                    # Count log type
                    log_counts[level] += 1

                    # Store ERROR logs separately
                    if level == "ERROR":
                        error_logs.append(parsed_line)

                except ValueError as error:

                    invalid_count += 1

                    print(
                        f"[Warning] Line {line_number}: "
                        f"{error}"
                    )

        # ----------------------------------------------------
        # Calculate Total Valid Logs
        # ----------------------------------------------------

        total_logs = sum(log_counts.values())

        # ----------------------------------------------------
        # Handle File With No Valid Logs
        # ----------------------------------------------------

        if total_logs == 0:

            print(
                "[Notice] The log file contains "
                "no valid log entries."
            )

            return None

        # ----------------------------------------------------
        # Find Most Frequent Log Type
        # ----------------------------------------------------

        most_frequent = (
            log_counts.most_common(1)[0][0]
        )

        # ----------------------------------------------------
        # Create Report
        # ----------------------------------------------------

        return LogReport(
            total_logs=total_logs,
            info_count=log_counts["INFO"],
            warning_count=log_counts["WARNING"],
            error_count=log_counts["ERROR"],
            invalid_count=invalid_count,
            most_frequent=most_frequent,
            error_logs=error_logs,
        )

    # --------------------------------------------------------
    # File Not Found
    # --------------------------------------------------------

    except FileNotFoundError as error:

        print(f"[Error] {error}")

    # --------------------------------------------------------
    # Permission Error
    # --------------------------------------------------------

    except PermissionError:

        print(
            f"[Error] Permission denied: "
            f"Cannot read '{path}'."
        )

    # --------------------------------------------------------
    # Encoding Error
    # --------------------------------------------------------

    except UnicodeDecodeError:

        print(
            f"[Error] Unable to decode '{path}'. "
            f"Please make sure the file is UTF-8 encoded."
        )

    # --------------------------------------------------------
    # Unexpected Error
    # --------------------------------------------------------

    except OSError as error:

        print(
            f"[Error] Unable to read the file: {error}"
        )

    return None


# ============================================================
# Print Report
# ============================================================

def print_report(
    report: LogReport,
) -> None:
    """
    Displays the analysis report.
    """

    print()
    print("=" * 50)
    print("              LOG SUMMARY REPORT")
    print("=" * 50)

    print(
        f"{'Total Logs':<30}: "
        f"{report.total_logs}"
    )

    print(
        f"{'Total INFO Logs':<30}: "
        f"{report.info_count}"
    )

    print(
        f"{'Total WARNING Logs':<30}: "
        f"{report.warning_count}"
    )

    print(
        f"{'Total ERROR Logs':<30}: "
        f"{report.error_count}"
    )

    print(
        f"{'Invalid Log Entries':<30}: "
        f"{report.invalid_count}"
    )

    print(
        f"{'Most Frequent Log Type':<30}: "
        f"{report.most_frequent}"
    )

    print("=" * 50)

    # --------------------------------------------------------
    # Display ERROR Logs
    # --------------------------------------------------------

    print("\n--- ERROR LOGS ---")

    if report.error_logs:

        for index, error_log in enumerate(
            report.error_logs,
            start=1,
        ):
            print(
                f"{index}. {error_log}"
            )

    else:

        print("No ERROR logs found.")

    print("-" * 50)


# ============================================================
# Main Program
# ============================================================

def main() -> None:
    """
    Application entry point.
    """

    print("=" * 50)
    print("              LOG FILE ANALYZER")
    print("=" * 50)

    file_name = input(
        "Enter log file path: "
    ).strip()

    # --------------------------------------------------------
    # Validate User Input
    # --------------------------------------------------------

    if not file_name:

        print(
            "[Error] File path cannot be empty."
        )

        return

    # --------------------------------------------------------
    # Analyze File
    # --------------------------------------------------------

    print(
        f"\nAnalyzing log file: '{file_name}'..."
    )

    report = analyze_log_file(
        file_name
    )

    # --------------------------------------------------------
    # Display Report
    # --------------------------------------------------------

    if report is not None:

        print_report(report)


# ============================================================
# Program Entry Point
# ============================================================

if __name__ == "__main__":
    main()

