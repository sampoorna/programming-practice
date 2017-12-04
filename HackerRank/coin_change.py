# Problem definition: https://www.hackerrank.com/challenges/coin-change/problem

def get_coin_change(list_of_coins, n):
    m = [[0 for i in range(n+1)] for j in list_of_coins]
    
    for i in range(len(list_of_coins)):
        coin = list_of_coins[i]
        for j in range(n+1):
            if j % coin == 0 and i == 0:
                m[i][j] = 1
            elif j% coin != 0 and i == 0:
                m[i][j] = 0
            elif j < coin and i > 0: # Second row onwards
                m[i][j] = m[i-1][j]
            elif j >= coin and i > 0:
                m[i][j] = m[i][j-coin] + m[i-1][j]
	
    #print m, i, j
    return m[i][j]

#list_of_coins = random.sample(range(-5, 7), 7)
#print list_of_coins
n, m = map(int, raw_input().split())
c = raw_input().split(" ")
coins = sorted([int(i) for i in c])
print get_coin_change(coins, n)