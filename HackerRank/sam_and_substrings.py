# Problem definition: https://www.hackerrank.com/challenges/sam-and-substrings/problem

def substring_sum2(n):
    size = len(n)
    result = 0
    mod = (10**9 + 7)
    f = 1
    
    for k in range(size-1, -1, -1):
        result += ((k+1) * int(n[k]) * f) % mod
        #print result, f, (k+1), int(n[k])
        f = (f*10 + 1) % mod
        
    return result % mod

def substring_sum(n):
    m = [[0 for i in n] for j in n]
    mod = (10**9 + 7)
    result = 0
    for i in range(len(n)):
        for j in range(i, len(n)):
            if i == j:
                m[i][j] = int(n[i])
            else:
                m[i][j] = (int(n[i:j+1])  + m[i][j-1] ) % mod
        result += (m[i][j]) % mod
    #print m
    return result % mod

n = raw_input()
print substring_sum2(n)