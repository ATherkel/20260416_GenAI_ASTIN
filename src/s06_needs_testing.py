def pareto_pdf(x, alpha, beta):
    if alpha <= 0 or beta <= 0:
        raise ValueError("alpha and beta must be positive")
    if x < 0:
        raise ValueError("x must be non-negative")
    return alpha * beta**alpha / (beta + x) ** (alpha + 1)


def pareto_cdf(x, alpha, beta):
    if alpha <= 0 or beta <= 0:
        raise ValueError("alpha and beta must be positive")
    if x < 0:
        raise ValueError("x must be non-negative")
    return 1 - (beta / (beta + x)) ** alpha


def pareto_quantile(p, alpha, beta):
    if alpha <= 0 or beta <= 0:
        raise ValueError("alpha and beta must be positive")
    if not (0 <= p < 1):
        raise ValueError("p must be in [0, 1)")
    return beta * ((1 - p) ** (-1 / alpha) - 1)


def pareto_mean(alpha, beta):
    if alpha <= 0 or beta <= 0:
        raise ValueError("alpha and beta must be positive")
    if alpha <= 1:
        raise ValueError("mean is undefined for alpha <= 1")
    return beta / (alpha - 1)
