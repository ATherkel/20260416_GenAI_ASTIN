from scipy import integrate


def pareto_pdf(x, alpha, beta):
    if x <= 0:
        raise ValueError("x must be positive")
    return (
        alpha * beta**alpha / (beta + x) ** (alpha + 1)
    )


if __name__ == "__main__":
    alpha, beta = 3, 2
    result, error = integrate.quad(pareto_pdf, 0, float("inf"), args=(alpha, beta))
    print(f"Integral of pareto_pdf(x, {alpha}, {beta}) over (0, inf): {result:.6f}")
    assert abs(result - 1) < 1e-6, f"PDF does not integrate to 1: {result}"
