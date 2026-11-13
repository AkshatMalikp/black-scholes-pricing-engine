
from black_scholes.pricing import call_price, put_price


def implied_volatility(
    market_price,
    S,
    K,
    r,
    T,
    option_type,
    tolerance=1e-8,
    max_iterations=1000
):

    if market_price <= 0:
        raise ValueError("Market price must be positive.")
    if S <= 0 or K <= 0 or T <= 0:
        raise ValueError("S, K, and T must be positive.")
    if option_type not in ['call', 'put']:
        raise ValueError("Option type must be 'call' or 'put'.")
    if tolerance <= 0 or max_iterations <= 0:
        raise ValueError("Tolerance and max_iterations must be positive.")


    call_price_func = call_price if option_type == 'call' else put_price


    lower_vol = 1e-6
    higher_vol = 5.0

    lower_price = call_price_func(S, K, r, lower_vol, T)-market_price
    higher_price = call_price_func(S, K, r, higher_vol, T)-market_price

    if lower_price * higher_price > 0:
        raise ValueError("The market price is out of bounds for the given parameters.")


    for iteration in range(max_iterations):
        mid_vol = (lower_vol + higher_vol) / 2
        mid_price = call_price_func(S, K, r, mid_vol, T)-market_price

        if abs(mid_price) < tolerance:
            return mid_vol

        if lower_price * mid_price < 0:
            higher_vol = mid_vol
            higher_price = mid_price
        else:
            lower_vol = mid_vol
            lower_price = mid_price


    raise RuntimeError("Failed to converge to a solution within the maximum number of iterations.")        