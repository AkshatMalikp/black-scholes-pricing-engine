
def call_payoff(stock_price, strike_price):
    C_t=max(stock_price - strike_price, 0)
    return C_t


def put_payoff(stock_price, strike_price):
    C_t=max(strike_price - stock_price, 0)
    return C_t

def long_call_profit(stock_price, strike_price, premium):
    return call_payoff(stock_price, strike_price) - premium


def short_call_profit(stock_price, strike_price, premium):
    return premium - call_payoff(stock_price, strike_price)
 


def long_put_profit(stock_price, strike_price, premium):
    return put_payoff(stock_price, strike_price) - premium



def short_put_profit(stock_price, strike_price, premium):
    return premium - put_payoff(stock_price, strike_price)



