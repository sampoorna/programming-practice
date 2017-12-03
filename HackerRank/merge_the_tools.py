def merge_the_tools(string, k):
    # your code goes here
	result = ''
	
	for s in range(len(string)):
		if string[s] not in result:
			result += string[s]
		if (s+1)%k == 0:
			print result
			result = ''
	
	print result	
	return
	
if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)