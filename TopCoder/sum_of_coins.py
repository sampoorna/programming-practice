def sum_of_coins(list_of_coins, sum):
	min_solution = [100000 for i in range(sum+1)]
	min_solution[0] = 0
	
	for i in range(sum+1):
		for j in range(len(list_of_coins)):
			if list_of_coins[j] <= i and min_solution[i-list_of_coins[j]] + 1 < min_solution[i]:
				min_solution[i] = min_solution[i-list_of_coins[j]] + 1
		print min_solution
	return min_solution[-1]	

#list_of_coins = random.sample(range(-5, 7), 7)
#print list_of_coins
print sum_of_coins([1, 3, 5], 11)