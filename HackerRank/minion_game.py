# Problem definition: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    # your code goes here
	vowels = 'AEIOU'
	stuart_score = 0
	kevin_score = 0
	stuart_words = []
	kevin_words = []
	
	for ind in range(len(string)):
		if string[ind] in vowels:
			kevin_score += len(string) - ind
		else:
			stuart_score += len(string) - ind
			
	if kevin_score > stuart_score:
		print "Kevin", kevin_score
	elif kevin_score < stuart_score:
		print "Stuart", stuart_score
	else:
		print "Draw"
	return

if __name__ == '__main__':
    s = raw_input()
    minion_game(s)