def analyze_structure(path: str):

    total_rows = 0
    misaligned_rows = 0
    empty_rows = 0

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        header = f.readline()

        if not header:
            return {
                "total_rows": 0,
                "expected_columns": 0,
                "misaligned_rows": 0,
                "empty_rows": 0,
                "drift_ratio": 0,
            }

        expected_columns = len(header.rstrip("\n").split(","))

        for line in f:
            total_rows += 1

            stripped = line.rstrip("\n")

            if not stripped:
                empty_rows += 1
                continue

            columns = len(stripped.split(","))

            if columns != expected_columns:
                misaligned_rows += 1

    drift_ratio = misaligned_rows / total_rows if total_rows else 0

    return {
        "total_rows": total_rows,
        "expected_columns": expected_columns,
        "misaligned_rows": misaligned_rows,
        "empty_rows": empty_rows,
        "drift_ratio": drift_ratio,
    }
