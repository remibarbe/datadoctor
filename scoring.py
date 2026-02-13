def compute_score(structure):

    score = 100
    drift = structure["drift_ratio"]

    if drift > 0.01:
        score -= 40
    elif drift > 0:
        score -= 20

    return max(score, 0)
