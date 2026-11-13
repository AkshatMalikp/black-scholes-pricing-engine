import pytest

from black_scholes.greeks import call_delta, put_delta,gamma,call_theta,put_theta,vega,call_rho,put_rho,calculate_all_greeks


def test_call_delta():
    assert call_delta(100, 100, 0.05, 0.20, 1) == pytest.approx(0.63683065)


def test_put_delta():
    assert put_delta(100, 100, 0.05, 0.20, 1) == pytest.approx(-0.36316935)


def test_delta_parity():
    call = call_delta(100, 100, 0.05, 0.20, 1)
    put = put_delta(100, 100, 0.05, 0.20, 1)

    assert call - put == pytest.approx(1)

def test_gamma():
    result = gamma(100, 100, 0.05, 0.20, 1)
    assert result == pytest.approx(0.018762, abs=0.00001)


def test_gamma_is_positive():
    assert gamma(100, 100, 0.05, 0.20, 1) > 0    


def test_call_theta():
    result = call_theta(100, 100, 0.05, 0.20, 1)
    assert result == pytest.approx(-0.0175726782)


def test_put_theta():
    result = put_theta(100, 100, 0.05, 0.20, 1)
    assert result == pytest.approx(-0.0045421381)


def test_call_theta_negative():
    assert call_theta(100, 100, 0.05, 0.20, 1) < 0   

def test_vega():
    result = vega(100, 100, 0.05, 0.20, 1)
    assert result == pytest.approx(0.375240, abs=0.00001)


def test_vega_positive():
    assert vega(100, 100, 0.05, 0.20, 1) > 0

def test_call_rho():
    result = call_rho(100, 100, 0.05, 0.20, 1)
    assert result == pytest.approx(0.5323, abs=0.0001)


def test_put_rho():
    result = put_rho(100, 100, 0.05, 0.20, 1)
    assert result == pytest.approx(-0.4189, abs=0.0001)    

S = 100
K = 100
R = 0.05
SIGMA = 0.20
T = 1


def test_calculate_all_call_greeks():
    result = calculate_all_greeks(
        S, K, R, SIGMA, T, "call"
    )

    assert result["delta"] == pytest.approx(0.63683065, abs=1e-6)
    assert result["gamma"] == pytest.approx(0.01876202, abs=1e-6)
    assert result["theta"] == pytest.approx(-0.01757268, abs=1e-6)
    assert result["vega"] == pytest.approx(0.37524035, abs=1e-6)
    assert result["rho"] == pytest.approx(0.53232482, abs=1e-6)


def test_calculate_all_put_greeks():
    result = calculate_all_greeks(
        S, K, R, SIGMA, T, "put"
    )

    assert result["delta"] == pytest.approx(-0.36316935, abs=1e-6)
    assert result["gamma"] == pytest.approx(0.01876202, abs=1e-6)
    assert result["theta"] == pytest.approx(-0.00454214, abs=1e-6)
    assert result["vega"] == pytest.approx(0.37524035, abs=1e-6)
    assert result["rho"] == pytest.approx(-0.41890482, abs=1e-6)


def test_invalid_option_type():
    with pytest.raises(ValueError):
        calculate_all_greeks(
            S, K, R, SIGMA, T, "invalid"
        )


def test_result_contains_all_five_greeks():
    result = calculate_all_greeks(
        S, K, R, SIGMA, T, "call"
    )

    assert set(result.keys()) == {
        "delta", "gamma", "theta", "vega", "rho"
    }
