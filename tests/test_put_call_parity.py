import math
import pytest

from black_scholes.pricing import call_price, put_price


@pytest.mark.parametrize(
    "S,K,r,sigma,T",
    [
        (100, 100, 0.05, 0.20, 1),
        (120, 100, 0.04, 0.30, 0.5),
        (80, 100, 0.03, 0.25, 2),
        (100, 110, -0.01, 0.40, 1),
    ]
)
def test_put_call_parity(S, K, r, sigma, T):

    call = call_price(S, K, r, sigma, T)
    put = put_price(S, K, r, sigma, T)

    lhs = call - put
    rhs = S - K * math.exp(-r * T)

    assert lhs == pytest.approx(rhs, abs=1e-9)