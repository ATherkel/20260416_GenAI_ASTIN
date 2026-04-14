def pareto_pdf(x, alpha, beta):
    if x <= 0:
        raise ValueError("x must be positive")
    return (
        alpha * beta**alpha / (beta + x) ** (alpha + 1)
    )
