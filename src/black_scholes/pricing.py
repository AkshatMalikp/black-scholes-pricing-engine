
import math

from black_scholes.parameters import calculate_d1, calculate_d2
from black_scholes.distributions import normal_cdf


def call_price(S, K, r, sigma, T):
    """
    Calculate European call option price
    using the Black-Scholes model.
    """
    d1=calculate_d1(S, K, r, sigma, T)
    d2=calculate_d2(d1, sigma, T)

    N_d1=normal_cdf(d1)
    N_d2=normal_cdf(d2)

    a= S*N_d1
    b= K*math.exp(-r*T)*N_d2

    C_t=a-b
    return C_t


def put_price(S, K, r, sigma, T):

   d1=calculate_d1(S, K, r, sigma, T)
   d2=calculate_d2(d1, sigma, T)
   N_neg_d1=normal_cdf(-d1)
   N_neg_d2=normal_cdf(-d2)
   a= K*math.exp(-r*T)*N_neg_d2
   b= S*N_neg_d1
   P_t=a-b
   return P_t
