# Enter your code here. Read input from STDIN. Print output to STDOUT

def test(sideLengths):
	last_cube = 2**32
	front_pointer = 0
	end_pointer = -1
	for i in sideLengths:
		if sideLengths[front_pointer] >= sideLengths[end_pointer] and sideLengths[front_pointer] <= last_cube:
			last_cube = sideLengths[front_pointer]
			front_pointer += 1
		elif sideLengths[front_pointer] <= sideLengths[end_pointer] and sideLengths[end_pointer] <= last_cube:
			last_cube = sideLengths[end_pointer]
			end_pointer += -1
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
		