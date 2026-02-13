#!/usr/bin/env python3

import typer
from inspector import inspect_file

app = typer.Typer()

@app.command()
def inspect(
    file: str,
    strict: bool = typer.Option(False, "--strict")
):
    result = inspect_file(file)

    if strict:
        if result["score"] < 80 or result["structure"]["drift_ratio"] > 0.01:
            raise typer.Exit(code=1)

    raise typer.Exit(code=0)

if __name__ == "__main__":
    app()
