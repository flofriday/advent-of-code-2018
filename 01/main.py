# Read the input file
file = open("input.txt")
list = file.readlines()

# PART 1
result = 0
resultList = [0]

for item in list:
	item = int(item)
	result += item
	
print("part1:" + str(result))

# PART 2
result = 0
resultlist = set()
while True:
	for item in list:
		item = int(item.strip())
		result += item

		if result in resultlist:
			# Hurra we are done here!
			print("part2:" + str(result))
			exit()

		else:
			# The current result is not in the list so we add it
			resultlist.add(result)
