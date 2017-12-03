# Problem definition: https://www.hackerrank.com/challenges/mark-and-toys/problem
import sys

def maximumToys(prices, k):
    prices = sorted(prices)
    count = 0
    spent = 0
    
    for i in prices:
        if spent + i < k:
            count += 1
            spent += i
            #print i,
    return count

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    prices = map(int, raw_input().strip().split(' '))
    result = maximumToys(prices, k)
    print result
