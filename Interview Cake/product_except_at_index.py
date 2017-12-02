import random

def get_products_of_all_ints_except_at_index(ints):
	products = [0 for i in ints]
	reverse_products = [0 for i in ints]
	result = [0 for i in ints]
	prod = ints[0]
	
	for i in range(len(ints)):
		if i == 0:
			#products[i] = ints[i]
			reverse_products[-i-1] = ints[-i-1]
		else:
			#products[i] = products[i-1] * ints[i]
			reverse_products[-1-i] = reverse_products[-i] * ints[-i-1]
	
	result[0] = reverse_products[1]
	#result[len(ints)-1] = ints[-1]
	
	for i in range(1, len(ints)-1):
		result[i] = prod * reverse_products[i+1]
		prod = prod * ints[i]
	result[-1] = prod
	#print products
	#print reverse_products
	return result
	
print get_products_of_all_ints_except_at_index([1, 2, 6, 5, 9])