import csv
from collections import Counter

def detect_type(values):
    is_int = True
    is_float = True

    for v in values:
        if v == "":
            continue
        if not v.isdigit():
            is_int = False
        try:
            float(v)
        except ValueError:
            is_float = False

    if is_int:
        return "int"
    if is_float:
        return "float"
    return "text"


def profile_csv(file_path):
    with open(file_path, newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        return []

    num_cols = len(rows[0])
    columns = [[] for _ in range(num_cols)]

    for row in rows:
        for i in range(num_cols):
            if i < len(row):
                columns[i].append(row[i])
            else:
                columns[i].append("")

    report = []

    for i, col in enumerate(columns):
        non_empty = [v for v in col if v != ""]
        col_type = detect_type(non_empty)

        profile = {
            "column": i,
            "type": col_type,
            "unique_values": len(set(non_empty)),
            "empty_values": col.count(""),
            "total_rows": len(col)
        }

        if col_type in ["int", "float"] and non_empty:
            numeric_values = list(map(float, non_empty))
            profile["min"] = min(numeric_values)
            profile["max"] = max(numeric_values)

        report.append(profile)

    return report
