with open("input.txt", "r") as file:
	rounds = file.readlines()

total = 0

for line in rounds:
	opponent = line[0]
	you = line[2]

	# Rock
	if opponent == "A":
		# Rock
		if you == "X":
			total += (1 + 3)
		# Paper
		elif you == "Y":
			total += (2 + 6)
		# Scissors
		elif you == "Z":
			total += (3 + 0)

	# Paper
	elif opponent == "B":
		# Rock
		if you == "X":
			total += (1 + 0)
		# Paper
		elif you == "Y":
			total += (2 + 3)
		# Scissors
		elif you == "Z":
			total += (3 + 6)

	# Scissors
	elif opponent == "C":
		# Rock
		if you == "X":
			total += (1 + 6)
		# Paper
		elif you == "Y":
			total += (2 + 0)
		# Scissors
		elif you == "Z":
			total += (3 + 3)

print(total)
