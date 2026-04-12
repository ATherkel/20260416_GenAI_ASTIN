err_msg_positive = "alpha and beta must be positive"
err_msg_non_negative = "x must be non-negative"

def pareto_pdf(x: float, alpha: float, beta: float) -> float:
    if alpha <= 0 or beta <= 0:
        raise ValueError(err_msg_positive)
    if x < 0:
        raise ValueError(err_msg_non_negative)
    return alpha * beta**alpha / (beta + x) ** (alpha + 1)


def pareto_cdf(x: float, alpha: float, beta: float) -> float:
    if alpha <= 0 or beta <= 0:
        raise ValueError(err_msg_positive)
    if x < 0:
        raise ValueError(err_msg_non_negative)
    return 1 - (beta / (beta + x)) ** alpha


def pareto_quantile(p: float, alpha: float, beta: float) -> float:
    if alpha <= 0 or beta <= 0:
        raise ValueError(err_msg_positive)
    if not (0 <= p < 1):
        raise ValueError("p must be in [0, 1)")
    return beta * ((1 - p) ** (-1 / alpha) - 1)


def pareto_mean(alpha: float, beta: float) -> float:
    if alpha <= 0 or beta <= 0:
        raise ValueError(err_msg_positive)
    if alpha <= 1:
        raise ValueError("mean is undefined for alpha <= 1")
    return beta / (alpha - 1)
