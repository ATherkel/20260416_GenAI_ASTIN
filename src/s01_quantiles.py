"""Quantile functions for heavy-tailed distributions."""


def pareto_quantile(p: float, alpha: float, beta: float) -> float:
    """Compute the quantile of a Pareto distribution.

    Args:
        p: Probability level in [0, 1).
        alpha: Shape parameter (tail index).
        beta: Scale parameter.

    Returns:
        The quantile value corresponding to probability p.

    Raises:
        ValueError: If p is not in [0, 1), alpha <= 0, or beta <= 0.
    """
    if not (0 <= p < 1):
        raise ValueError(f"p must be in [0, 1), got {p}")
    if alpha <= 0:
        raise ValueError(f"alpha must be positive, got {alpha}")
    if beta <= 0:
        raise ValueError(f"beta must be positive, got {beta}")
    return beta * ((1 - p) ** (-1 / alpha) - 1)
