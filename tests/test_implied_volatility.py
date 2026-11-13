
import pytest

from black_scholes.pricing import call_price, put_price
from black_scholes.implied_volatility import implied_volatility


def test_call_implied_volatility():
    # Generate a market price using known volatility of 20%.
    market_price = call_price(100, 100, 0.05, 0.20, 1)

    result = implied_volatility(
        market_price, 100, 100, 0.05, 1, "call"
    )

    assert result == pytest.approx(0.20, abs=1e-6)


def test_put_implied_volatility():
    market_price = put_price(100, 100, 0.05, 0.20, 1)

    result = implied_volatility(
        market_price, 100, 100, 0.05, 1, "put"
    )

    assert result == pytest.approx(0.20, abs=1e-6)


def test_invalid_option_type():
    with pytest.raises(ValueError):
        implied_volatility(10, 100, 100, 0.05, 1, "invalid")


def test_market_price_below_call_lower_bound():
    with pytest.raises(ValueError):
        implied_volatility(0.01, 100, 100, 0.05, 1, "call")


def test_market_price_above_call_upper_bound():
    with pytest.raises(ValueError):
        implied_volatility(101, 100, 100, 0.05, 1, "call")


def test_market_price_below_put_lower_bound():
    with pytest.raises(ValueError):
        implied_volatility(1, 80, 100, 0.05, 1, "put")


def test_market_price_above_put_upper_bound():
    with pytest.raises(ValueError):
        implied_volatility(100, 100,100, 0.05, 1, "put")
