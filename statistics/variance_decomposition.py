from typing import Dict, List, Any

def compute_total_variance(
scores: List[float]
) -> float:
"""Compute total variance."""
pass

def compute_within_group_variance(
grouped_scores: Dict[str, List[float]]
) -> Dict[str, float]:
"""Compute variance within each group."""
pass

def compute_between_group_variance(
grouped_scores: Dict[str, List[float]]
) -> float:
"""Compute variance between groups."""
pass

def compute_variance_contribution(
total_variance: float,
factor_variance: float
) -> float:
"""Compute variance contribution percentage."""
pass

def decompose_variance(
evaluation_results: List[Dict[str, Any]]
) -> Dict[str, float]:
"""Run variance decomposition analysis."""
pass
