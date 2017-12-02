import random

def highest_product_of_3 (list_of_ints):
	highest_2 = [list_of_ints[0], list_of_ints[1]]
	lowest_2 = [list_of_ints[0], list_of_ints[1]]
	current_prod = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
	highest = 0
	lowest = 0
	
	for i in list_of_ints[2:]:		
					
		highest_2[highest_2.index(min(highest_2))] = max(i, min(highest_2))
		lowest_2[lowest_2.index(max(lowest_2))] = min(i, min(lowest_2))
		highest = max(highest, i)
		lowest = min(lowest, i)
		
		if highest_2[0]*highest_2[1]*lowest > current_prod:
			current_prod = highest_2[0]*highest_2[1]*lowest
		elif lowest_2[0]*lowest_2[1]*highest > current_prod:
			current_prod = lowest_2[0]*lowest_2[1]*highest
		print highest_2, lowest_2, highest, lowest
	return current_prod
	
list_of_ints = random.sample(range(-5, 7), 7)
print list_of_ints
print highest_product_of_3([-10,-10, 1, 3, 2])