from structure import analyze_structure
from scoring import compute_score
from report import render_report

def inspect_file(path: str):

    structure = analyze_structure(path)
    score = compute_score(structure)

    result = {
        "structure": structure,
        "score": score,
    }

    render_report(result)
    return result
