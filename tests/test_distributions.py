import pytest

from black_scholes.distributions import normal_pdf, normal_cdf


def test_normal_pdf_at_zero():
    assert normal_pdf(0) == pytest.approx(0.39894228)


def test_normal_pdf_symmetry():
    assert normal_pdf(1) == pytest.approx(normal_pdf(-1))


def test_normal_cdf_at_zero():
    assert normal_cdf(0) == pytest.approx(0.5)


def test_normal_cdf_at_one():
    assert normal_cdf(1) == pytest.approx(0.8413447)


def test_normal_cdf_symmetry():
    assert normal_cdf(-1) == pytest.approx(1 - normal_cdf(1))


def test_normal_cdf_at_196():
    assert normal_cdf(1.96) == pytest.approx(0.9750021)