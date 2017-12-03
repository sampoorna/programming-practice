# Enter your code here. Read input from STDIN. Print output to STDOUT

def test(sideLengths):
	last_cube = 2**32
	while len(sideLengths)>0:
		if sideLengths[0] >= sideLengths[-1] and sideLengths[0] <= last_cube:
			last_cube = sideLengths[0]
			sideLengths = sideLengths[1:]
		elif sideLengths[0] <= sideLengths[-1] and sideLengths[-1] <= last_cube:
			last_cube = sideLengths[-1]
			sideLengths = sideLengths[:-1]
		else:
			print "No"
			return
		#print sideLengths
	
	print "Yes"
	return

T = input()
for i in range(T):
	n = input()
	sideLengthsString = raw_input()
	sideLengths = [int(i) for i in sideLengthsString.split(" ")]
	#print sideLengths
	
	test(sideLengths)
		