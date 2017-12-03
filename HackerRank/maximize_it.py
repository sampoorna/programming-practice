# Enter your code here. Read input from STDIN. Print output to STDOUT

def f(X):
	return X**2

def S(X_list, M):
	S = 0
	
	for x in X_list:
		S += f(x)
		
	return S%M
	

def maximize_it(K, M, N):
	
	for i in K:
		N[i] = [(j*j) % M for j in N[i][1:]]
	# Incomplete

T = input()
for i in range(T):
	
	K, M = input()
	N = []
	
	for i in range(K):
		NString = raw_input()
		N.append([int(i) for i in NString.split(" ")])
	#print sideLengths
	
	maximize_it(K, M, N)
		