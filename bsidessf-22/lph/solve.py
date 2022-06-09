# letters on the dial, in order; note that JKQVXZ are excluded as they do not appear on the dial
alphabet = 'ABCDEFGHILMNOPRSTUWY'

# number of short clicks in each set of clicks in the recording
clicks = [5, 5, 17, 14, 13, 7, 14, 13, 21, 13]

# initial direction to turn is right.  Set to False for left
right = True

# iterate through different starting positions on the dial
for value in range(0, len(alphabet)):  
	for c in clicks:
		if right:
			# increase position by that many clicks, plus one for the big click at the end
			value += c + 1
		else:
			# decrease position by that many clicks, plus one for the big click at the end
			value -= c + 1
		
		# reverse turning direction after each letter
		right = not right

		# print the character at that position on the dial; the mod (%) makes it so the position "wraps around" if value is negative or larger than 20
		print(alphabet[value % (len(alphabet))], end='')

	# start a new line
	print()
