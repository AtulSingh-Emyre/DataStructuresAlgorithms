
def stock_buy_and_sell(stock_prices):
    # unlimited buy and sell
    total = 0
    previous_price = stock_prices[0]
    for i in range(1,len(stock_prices)):
        if previous_price < stock_prices[i]:
            total += stock_prices[i] - previous_price
            previous_price = stock_prices[i]
    return total
