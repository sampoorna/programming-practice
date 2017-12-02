import random

def get_max_profit(prices):

	min_price = prices[0]
	max_price = prices[1]
	max_profit = max_price - min_price
	
	for p in range(1, len(prices)):
		if prices[p] >= max_price:
			#print "If 1"
			max_price = prices[p]
			min_price = min(min_price, prices[p-1])
		
		elif prices[p] - prices[p-1] > max_profit:
			#print "If 2"
			max_price = prices[p]
			min_price = prices[p-1]
		#print min_price, max_price
		max_profit = max(max_price - min_price, max_profit)
	print max_price, min_price
	return max_profit

stock_prices_yesterday = random.sample(range(1, 7), 4) #[18, 11, 4, 10, 17, 9, 7] #
print stock_prices_yesterday
print get_max_profit(stock_prices_yesterday)