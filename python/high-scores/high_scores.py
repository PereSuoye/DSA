def latest(scores):
    """Return last score."""
    return scores[-1]


def personal_best(scores):
    """Return the highest score."""
    return max(scores)


def personal_top_three(scores):
    """Return the three highest scores."""
    scores = sorted(scores, reverse=True)
    return scores[:3]
