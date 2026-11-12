
from black_scholes.payoffs import call_payoff, put_payoff, long_call_profit, short_call_profit, long_put_profit, short_put_profit


def test_call_in_the_money():
    assert call_payoff(120, 100) == 20


def test_call_out_of_the_money():
    assert call_payoff(80, 100) == 0


def test_call_at_the_money():
    assert call_payoff(100, 100) == 0


def test_put_in_the_money():
    assert put_payoff(80, 100) == 20


def test_put_out_of_the_money():
    assert put_payoff(120, 100) == 0


def test_put_at_the_money():
    assert put_payoff(100, 100) == 0


def test_long_call_profit():
    assert long_call_profit(115, 100, 5) == 10


def test_short_call_profit():
    assert short_call_profit(115, 100, 5) == -10


def test_long_put_profit():
    assert long_put_profit(115, 100, 5) == -5


def test_short_put_profit():
    assert short_put_profit(115, 100, 5) == 5
