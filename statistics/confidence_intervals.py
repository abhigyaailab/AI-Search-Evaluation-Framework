from typing import List, Tuple

def calculate_standard_error(
scores: List[float]
) -> float:
"""Calculate standard error."""
pass

def calculate_confidence_interval(
scores: List[float],
confidence_level: float = 0.95
) -> Tuple[float, float]:
"""Calculate confidence interval."""
pass

def bootstrap_confidence_interval(
bootstrap_scores: List[float],
confidence_level: float = 0.95
) -> Tuple[float, float]:
"""Compute CI using bootstrap percentiles."""
pass
