def pareto_cdf(x: float, alpha: float, beta: float) -> float:
    if alpha <= 0 or beta <= 0:
        raise ValueError("alpha and beta must be positive")
    if x < 0:
        raise ValueError("x must be non-negative")
    return 1 - (beta / (beta + x)) ** alpha
