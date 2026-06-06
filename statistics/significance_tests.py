from typing import List, Dict, Any

def paired_t_test(
system_a_scores: List[float],
system_b_scores: List[float]
) -> Dict[str, Any]:
"""Perform paired t-test."""
pass

def wilcoxon_test(
system_a_scores: List[float],
system_b_scores: List[float]
) -> Dict[str, Any]:
"""Perform Wilcoxon signed-rank test."""
def bootstrap_significance_test(
system_a_scores: List[float],
system_b_scores: List[float],
n_iterations: int = 1000
) -> Dict[str, Any]:
"""Bootstrap-based significance test."""
pass

def permutation_test(
system_a_scores: List[float],
system_b_scores: List[float],
n_iterations: int = 1000
) -> Dict[str, Any]:
"""Permutation test."""
pass
