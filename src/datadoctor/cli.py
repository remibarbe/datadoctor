#!/usr/bin/env python3

import typer
import json

from datadoctor.inspector import inspect_file
from datadoctor.profiler import profile_csv

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

app = typer.Typer()
console = Console()


@app.command()
def main(
    file: str = typer.Argument(..., help="CSV file to inspect"),
    strict: bool = typer.Option(False, "--strict", help="Exit with code 1 if CSV is unhealthy"),
    json_output: bool = typer.Option(False, "--json", help="Output report as JSON")
):
    result = inspect_file(file)
    profiles = profile_csv(file)

    structure = result.get("structure", {})
    score = result.get("score", 0)
    drift_ratio = structure.get("drift_ratio", 0.0)

    full_report = {
        "structure": structure,
        "score": score,
        "columns": profiles
    }

    # JSON MODE
    if json_output:
        print(json.dumps(full_report, indent=2))
        if strict and (score < 80 or drift_ratio > 0.01):
            raise typer.Exit(code=1)
        raise typer.Exit(code=0)

    # RICH DISPLAY
    total_rows = structure.get("total_rows", 0)
    expected_columns = structure.get("expected_columns", 0)
    misaligned_rows = structure.get("misaligned_rows", 0)
    empty_rows = structure.get("empty_rows", 0)

    if score >= 80:
        score_color = "green"
    elif score >= 50:
        score_color = "yellow"
    else:
        score_color = "red"

    structural_text = Text()
    structural_text.append(f"Rows: {total_rows}\n")
    structural_text.append(f"Expected columns: {expected_columns}\n")
    structural_text.append(f"Misaligned rows: {misaligned_rows}\n")
    structural_text.append(f"Empty rows: {empty_rows}\n")
    structural_text.append(f"Drift ratio: {drift_ratio*100:.2f}%\n\n")
    structural_text.append(f"Data Health Score: {score}/100", style=score_color)

    console.print(Panel(structural_text, title="📊 DataDoctor — Structural Analysis"))

    table = Table(title="📁 Column Profiling")
    table.add_column("Column")
    table.add_column("Type")
    table.add_column("Unique Values")
    table.add_column("Empty Values")
    table.add_column("Total Rows")

    for p in profiles:
        table.add_row(
            str(p.get("column")),
            str(p.get("type")),
            str(p.get("unique_values")),
            str(p.get("empty_values")),
            str(p.get("total_rows")),
        )

    console.print(table)

    if strict and (score < 80 or drift_ratio > 0.01):
        raise typer.Exit(code=1)

    raise typer.Exit(code=0)


if __name__ == "__main__":
    app()
