import pytest

from src.s06_needs_testing import pareto_cdf


def pareto_pdf(x: float, alpha: float, beta: float) -> float:
    return alpha / beta * (beta / (beta + x)) ** (alpha + 1)


def test_pareto_pdf_100k(benchmark):
    def run():
        for i in range(100_000):
            pareto_pdf(float(i), alpha=2.0, beta=100.0)

    benchmark(run)
