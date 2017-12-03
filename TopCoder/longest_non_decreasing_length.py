import random

# Incomplete
def longest_non_decreasing_sequence_length(A):
	longest = [-1 for i in A]
	longest[0] = 1
	
	for i in range(1, len(A)):
		#for j in range(len(list_of_coins)):
		if A[i] >= A[i-1]:
			longest[i] = longest[i-1] + 1
		else:
			longest[i] = 1
		print longest
	return max(longest)	

sequence = random.sample(range(-5, 7), 7)
print sequence
print longest_non_decreasing_sequence_length([5, 3, 4, 8, 6, 7]	)