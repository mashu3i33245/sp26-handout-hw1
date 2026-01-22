"""
Functions to calculate housing priority score based given user answers.
"""


def points_for_class_year(year: int) -> int:
    """Given an integer year, return points based on scoring system."""
    if year == 1:
        return 40
    elif year == 2:
        return 30
    elif year == 3:
        return 20
    else:
        return 10


def points_for_graduation(is_graduating: bool) -> int:
    """Return points based on graduation status."""
    if is_graduating:
        return 20
    return 0


def points_for_credits(num_credits: int) -> int:
    """Compute points based on credits earned."""
    return num_credits


def points_for_additional_questions(responses: dict[str, bool]) -> int:
    """Given the dict from ask_additional_questions(), assign points."""
    points = 0
    if responses.get('old23', False):
        points += 5
    if responses.get('honors', False):
        points += 5
    return points


def calculate_total_score(
    year: int,
    is_graduating: bool,
    num_credits: int,
    additional_responses: dict[str, bool],
) -> int:
    """Calculate the total priority score based on all inputs."""
    total = (
        points_for_class_year(year)
        + points_for_graduation(is_graduating)
        + points_for_credits(num_credits)
        + points_for_additional_questions(additional_responses)
    )
    return total
