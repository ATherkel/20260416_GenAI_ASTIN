import pytest
from src.s06_needs_testing import pareto_cdf


class TestParetoCdfBasic:
    def test_zero_returns_zero(self):
        assert pareto_cdf(0, alpha=2, beta=100) == pytest.approx(0.0)

    def test_large_x_approaches_one(self):
        assert pareto_cdf(1e12, alpha=2, beta=100) == pytest.approx(1.0, abs=1e-6)

    def test_known_value(self):
        # x=100, alpha=2, beta=100 → 1 - (100/200)^2 = 0.75
        assert pareto_cdf(100, alpha=2, beta=100) == pytest.approx(0.75)

    def test_alpha_one(self):
        # x=100, alpha=1, beta=100 → 1 - 100/200 = 0.5
        assert pareto_cdf(100, alpha=1, beta=100) == pytest.approx(0.5)

    def test_result_between_zero_and_one(self):
        result = pareto_cdf(50, alpha=3, beta=200)
        assert 0.0 <= result <= 1.0

    def test_monotonically_increasing(self):
        vals = [pareto_cdf(x, alpha=2, beta=100) for x in [0, 10, 50, 100, 500, 1000]]
        assert vals == sorted(vals)


class TestParetoCdfParametrized:
    @pytest.mark.parametrize(
        "x, alpha, beta, expected",
        [
            (100, 1, 100, 0.5),
            (100, 2, 100, 0.75),
            (100, 3, 100, 0.875),
            (200, 2, 200, 0.75),
            (50, 1, 50, 0.5),
            (100, 0.5, 100, 1 - (0.5) ** 0.5),
            (500, 2, 1000, 1 - (1000 / 1500) ** 2),
            (0, 5, 50, 0.0),
        ],
    )
    def test_known_values(self, x, alpha, beta, expected):
        assert pareto_cdf(x, alpha, beta) == pytest.approx(expected)

    @pytest.mark.parametrize(
        "alpha, beta",
        [(1, 100), (2, 100), (3, 50), (0.5, 200), (5, 1000), (10, 10)],
    )
    def test_zero_gives_zero(self, alpha, beta):
        assert pareto_cdf(0, alpha, beta) == pytest.approx(0.0)

    @pytest.mark.parametrize(
        "alpha, beta",
        [(1, 100), (2, 100), (3, 50), (0.5, 200), (5, 1000), (10, 10)],
    )
    def test_large_x_approaches_one(self, alpha, beta):
        assert pareto_cdf(1e12, alpha, beta) == pytest.approx(1.0, abs=1e-4)

    @pytest.mark.parametrize(
        "alpha, beta",
        [(1, 100), (2, 100), (3, 50), (0.5, 200), (5, 1000), (10, 10)],
    )
    def test_monotonically_increasing(self, alpha, beta):
        vals = [pareto_cdf(x, alpha, beta) for x in [0, 10, 50, 100, 500]]
        assert vals == sorted(vals)


class TestParetoCdfEdgeCases:
    def test_alpha_negative_raises(self):
        with pytest.raises(ValueError, match="alpha and beta must be positive"):
            pareto_cdf(10, alpha=-1, beta=100)

    def test_alpha_zero_raises(self):
        with pytest.raises(ValueError, match="alpha and beta must be positive"):
            pareto_cdf(10, alpha=0, beta=100)

    def test_beta_negative_raises(self):
        with pytest.raises(ValueError, match="alpha and beta must be positive"):
            pareto_cdf(10, alpha=2, beta=-1)

    def test_beta_zero_raises(self):
        with pytest.raises(ValueError, match="alpha and beta must be positive"):
            pareto_cdf(10, alpha=2, beta=0)

    def test_x_negative_raises(self):
        with pytest.raises(ValueError, match="x must be non-negative"):
            pareto_cdf(-1, alpha=2, beta=100)
