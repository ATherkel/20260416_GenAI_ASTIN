import pytest
from hypothesis import given, settings, assume
from hypothesis.strategies import floats

from src.s06_needs_testing import pareto_cdf

# Reusable strategies for valid parameter ranges
valid_alpha = floats(min_value=0.1, max_value=50, allow_nan=False, allow_infinity=False)
valid_beta = floats(min_value=0.1, max_value=1e6, allow_nan=False, allow_infinity=False)
valid_x = floats(min_value=0.0, max_value=1e8, allow_nan=False, allow_infinity=False)
valid_p = floats(min_value=1e-6, max_value=1 - 1e-6, allow_nan=False, allow_infinity=False)


def pareto_quantile(p: float, alpha: float, beta: float) -> float:
    """Inverse CDF: x such that F(x) = p."""
    return beta * ((1 - p) ** (-1 / alpha) - 1)


def pareto_pdf(x: float, alpha: float, beta: float) -> float:
    """Analytical PDF: derivative of the CDF."""
    return alpha / beta * (beta / (beta + x)) ** (alpha + 1)


class TestParetoCdfProperties:
    @given(p=valid_p, alpha=valid_alpha, beta=valid_beta)
    @settings(max_examples=500)
    def test_cdf_of_quantile_roundtrips(self, p, alpha, beta):
        x = pareto_quantile(p, alpha, beta)
        assume(x >= 0 and x < 1e15)
        assert pareto_cdf(x, alpha, beta) == pytest.approx(p, rel=1e-6)

    @given(x=valid_x, alpha=valid_alpha, beta=valid_beta)
    @settings(max_examples=500)
    def test_pdf_is_non_negative(self, x, alpha, beta):
        assert pareto_pdf(x, alpha, beta) >= 0

    @given(x=valid_x, alpha=valid_alpha, beta=valid_beta)
    @settings(max_examples=500)
    def test_cdf_between_zero_and_one(self, x, alpha, beta):
        result = pareto_cdf(x, alpha, beta)
        assert 0.0 <= result <= 1.0

    @given(alpha=valid_alpha, beta=valid_beta)
    @settings(max_examples=200)
    def test_cdf_is_zero_at_origin(self, alpha, beta):
        assert pareto_cdf(0, alpha, beta) == pytest.approx(0.0)
