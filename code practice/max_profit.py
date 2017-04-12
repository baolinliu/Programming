stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
            
def get_max_profit(stock_prices_yesterday):
    
    difference = None
    for price_1 in stock_prices_yesterday:
        for price_2 in stock_prices_yesterday:
            current = price_1-price_2
            if current > difference:
                difference = current
    return difference 


get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)