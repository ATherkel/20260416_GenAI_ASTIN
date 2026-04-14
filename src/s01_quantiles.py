"""Quantile functions for heavy-tailed distributions."""


def pareto_quantile(p: float, alpha: float, beta: float) -> float:
    """Compute the quantile of a Pareto distribution.

    Args:
        p: Probability level in [0, 1).
        alpha: Shape parameter (tail index).
        beta: Scale parameter.

    Returns:
        The quantile value corresponding to probability p.
    """
    return beta * ((1 - p) ** (-1 / alpha) - 1)
