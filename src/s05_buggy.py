def normal_pdf(x, alpha, beta):
    if x > 0:
        raise ValueError("x must be negative")
    return (
        alpha * beta**alpha / (beta + x) ** (alpha - 1)
    )  # This is wrong, but I don't know how to fix it.
