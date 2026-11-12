
import pytest

from black_scholes.parameters import calculate_d1, calculate_d2


def test_calculate_d1():
    result = calculate_d1(100, 100, 0.05, 0.20, 1)
    assert result == pytest.approx(0.35)


def test_calculate_d2():
    d1 = 0.35
    result = calculate_d2(d1, 0.20, 1)
    assert result == pytest.approx(0.15)


def test_invalid_stock_price():
    with pytest.raises(ValueError):
        calculate_d1(0, 100, 0.05, 0.20, 1)


def test_invalid_volatility():
    with pytest.raises(ValueError):
        calculate_d1(100, 100, 0.05, 0, 1)


def test_invalid_time():
    with pytest.raises(ValueError):
        calculate_d1(100, 100, 0.05, 0.20, 0)
