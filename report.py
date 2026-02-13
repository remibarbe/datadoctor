from rich.console import Console

console = Console()

def render_report(result):

    structure = result["structure"]

    console.rule("DataDoctor — Structural Analysis")

    console.print(f"Rows: {structure['total_rows']}")
    console.print(f"Expected columns: {structure['expected_columns']}")
    console.print(f"Misaligned rows: {structure['misaligned_rows']}")
    console.print(f"Empty rows: {structure['empty_rows']}")
    console.print(f"Drift ratio: {structure['drift_ratio']:.2%}")

    console.print()
    console.print(f"[bold]Data Health Score:[/bold] {result['score']}/100")
