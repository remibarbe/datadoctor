from datadoctor.structure import analyze_structure
from datadoctor.scoring import compute_score
from datadoctor.report import render_report

def inspect_file(path: str):

    structure = analyze_structure(path)
    score = compute_score(structure)

    result = {
        "structure": structure,
        "score": score,
    }

    render_report(result)
    return result
