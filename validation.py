from scipy.stats import norm

from black_scholes.pricing import call_price, put_price

from black_scholes.greeks import call_delta, put_delta, gamma, call_theta, put_theta,vega

S = 100
K = 100
r = 0.05
sigma = 0.20
T = 1
h = 0.0001

call = call_price(S, K, r, sigma, T)
put = put_price(S, K, r, sigma, T)

print("Our Black-Scholes Engine")
print("------------------------")
print("Call:", call)
print("Put:", put)
print("SciPy benchmark: N(0.35) =", norm.cdf(0.35))
print("SciPy benchmark: N(0.15) =", norm.cdf(0.15))

numerical_vega = (
    call_price(S, K, r, sigma + h, T)
    - call_price(S, K, r, sigma - h, T)
) / (2 * h)

analytical_vega = vega(S, K, r, sigma, T) * 100

print("Numerical Vega:", numerical_vega)
print("Analytical Vega:", analytical_vega)