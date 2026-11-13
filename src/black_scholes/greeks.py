
from black_scholes.parameters import calculate_d1,calculate_d2
from black_scholes.distributions import normal_cdf
import math

def call_delta(S, K, r, sigma, T):
    d1 = calculate_d1(S, K, r, sigma, T)
    N_d1 = normal_cdf(d1)
    return N_d1


def put_delta(S, K, r, sigma, T):
    d1 = calculate_d1(S, K, r, sigma, T)
    N_d1 = normal_cdf(d1)
    return N_d1 - 1

def gamma(S, K, r, sigma, T):

    d1 = calculate_d1(S, K, r, sigma, T)


    # Calculate normal PDF of d1
    N_prime_d1 = (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * d1 ** 2)

    gamma_value = N_prime_d1 / (S * sigma * math.sqrt(T))
    return gamma_value



def call_theta(S, K, r, sigma, T):

    d1 = calculate_d1(S, K, r, sigma, T)
    d2 = d1 - sigma * math.sqrt(T)
    N_prime_d1 = (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * d1 ** 2)

    N_d2 = normal_cdf(d2)

    call_theta = (-S * N_prime_d1 * sigma / (2 * math.sqrt(T))) - (r * K * math.exp(-r * T) * N_d2)
    call_theta_daily = call_theta / 365

    return call_theta_daily

def put_theta(S, K, r, sigma, T):

    # Calculate d1 and d2

    d1=calculate_d1(S, K, r, sigma, T)
    d2=d1-sigma*math.sqrt(T)

    N_prime_d1 = (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * d1 ** 2)
    N_neg_d2 = normal_cdf(-d2)

    put_theta = (-S * N_prime_d1 * sigma / (2 * math.sqrt(T))) + (r * K * math.exp(-r * T) * N_neg_d2)
    put_theta_daily = put_theta / 365
    return put_theta_daily


def vega(S, K, r, sigma, T):

    # Calculate d1
    d1 = calculate_d1(S, K, r, sigma, T)
    normal_pdf_d1 = (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * d1 ** 2)

    vega_value = S * normal_pdf_d1 * math.sqrt(T)

    return vega_value / 100  


def call_rho(S, K, r, sigma, T):

    # Calculate d1 and d2
    d1=calculate_d1(S, K, r, sigma, T)
    d2=calculate_d2(d1, sigma, T)

    N_d2 = normal_cdf(d2)

    rho_value = K * T * math.exp(-r * T) * N_d2
    return rho_value / 100  



def put_rho(S, K, r, sigma, T):

    # Calculate d1 and d2
    d1=calculate_d1(S, K, r, sigma, T)
    d2=calculate_d2(d1, sigma, T)

    N_neg_d2 = normal_cdf(-d2)

    rho_value = -K * T * math.exp(-r * T) * N_neg_d2
    return rho_value / 100

def calculate_all_greeks(S, K, r, sigma, T, option_type):

    if option_type not in ['call', 'put']:
        raise ValueError("Invalid option type. Must be 'call' or 'put'.")
    
    if option_type == 'call':
        delta = call_delta(S, K, r, sigma, T)
        theta = call_theta(S, K, r, sigma, T)
        rho = call_rho(S, K, r, sigma, T)
    elif option_type == 'put':
        delta = put_delta(S, K, r, sigma, T)
        theta = put_theta(S, K, r, sigma, T)
        rho = put_rho(S, K, r, sigma, T)
    else:
        raise ValueError("Invalid option type. Must be 'call' or 'put'.")

    gamma_value = gamma(S, K, r, sigma, T)
    vega_value = vega(S, K, r, sigma, T)

    return {
        'delta': delta,
        'gamma': gamma_value,
        'theta': theta,
        'vega': vega_value,
        'rho': rho
    }
 