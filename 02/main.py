# Read the input file
file = open("input.txt")
input = file.readlines()

# Part 1
doubleCounter = 0
tribbleCounter = 0
for id in input:
	chars = list(id)
	dict = {}
	for char in chars:
		if char in dict:
			dict[char] = dict[char] + 1
		else:
			dict[char] = 1

	gotTwo = False
	gotThree = False
	for key, value in dict.items():
		if value == 2 and gotTwo == False:
			doubleCounter += 1
			gotTwo = True 
		if value == 3 and gotThree == False:
			tribbleCounter += 1
			gotThree = True 

print("part1: " + str(doubleCounter * tribbleCounter))

# Part 2
viewed = []
for id in input:
	for tmp in viewed:
		idChars = list(id)
		tmpChars = list(tmp)
		mistakes = 0
		output = ""
		for n in range(0, len(idChars)):
			if tmpChars[n] != idChars[n]:
				mistakes += 1
			else:
				output += idChars[n]

		if mistakes == 1:
			print("part2: " + str(output))
			break

	# Put current id in viewed
	viewed.append(id)
	

