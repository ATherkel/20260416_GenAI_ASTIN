import pytest
from src.s05_buggy import pareto_pdf


class TestParetoPdf:
    def test_known_value(self):
        # alpha=2, beta=1: pdf(x) = 2*1^2 / (1+x)^3
        # at x=1: 2 / 8 = 0.25
        assert pareto_pdf(1, alpha=2, beta=1) == pytest.approx(0.25)

    def test_positive_for_positive_x(self):
        assert pareto_pdf(10, alpha=3, beta=2) > 0

    def test_decreasing(self):
        vals = [pareto_pdf(x, alpha=3, beta=2) for x in [0.1, 1, 10, 100]]
        assert vals == sorted(vals, reverse=True)

    def test_x_zero_raises(self):
        with pytest.raises(ValueError, match="x must be positive"):
            pareto_pdf(0, alpha=2, beta=1)

    def test_x_negative_raises(self):
        with pytest.raises(ValueError, match="x must be positive"):
            pareto_pdf(-1, alpha=2, beta=1)

    def test_integrates_to_one(self):
        from scipy import integrate

        alpha, beta = 3, 2
        result, _ = integrate.quad(pareto_pdf, 0, float("inf"), args=(alpha, beta))
        assert result == pytest.approx(1.0, abs=1e-6)
