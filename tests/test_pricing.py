
import pytest
import math
from black_scholes.pricing import call_price, put_price


def test_call_price():
    result = call_price(100, 100, 0.05, 0.20, 1)
    assert result == pytest.approx(10.4506, abs=0.0001)


def test_put_price():
    result = put_price(100, 100, 0.05, 0.20, 1)
    assert result == pytest.approx(5.5735, abs=0.0001)


def test_call_positive():
    assert call_price(100, 100, 0.05, 0.20, 1) > 0


def test_put_positive():
    assert put_price(100, 100, 0.05, 0.20, 1) > 0


def test_invalid_stock_price():
    with pytest.raises(ValueError):
        call_price(0, 100, 0.05, 0.20, 1)
def test_put_call_parity():
    S, K, r, sigma, T = 100, 100, 0.05, 0.20, 1

    call = call_price(S, K, r, sigma, T)
    put = put_price(S, K, r, sigma, T)

    assert call - put == pytest.approx(
        S - K * math.exp(-r * T)
    )