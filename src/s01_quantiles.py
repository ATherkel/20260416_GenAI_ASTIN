def pareto_quantile(p, alpha, beta):
    return beta * ((1 - p) ** (-1 / alpha) - 1)
