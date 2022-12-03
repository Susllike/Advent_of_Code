with open("input.txt", "r") as file:
	rounds = file.readlines()

total = 0

for line in rounds:
	opponent = line[0]
	you = line[2]

	# Rock
	if opponent == "A":
		# Loss
		if you == "X":
			total += (3 + 0)
		# Draw
		elif you == "Y":
			total += (1 + 3)
		# Win
		elif you == "Z":
			total += (2 + 6)

	# Paper
	elif opponent == "B":
		# Loss
		if you == "X":
			total += (1 + 0)
		# Draw
		elif you == "Y":
			total += (2 + 3)
		# Win
		elif you == "Z":
			total += (3 + 6)

	# Scissors
	elif opponent == "C":
		# Loss
		if you == "X":
			total += (2 + 0)
		# Draw
		elif you == "Y":
			total += (3 + 3)
		# Win
		elif you == "Z":
			total += (1 + 6)

print(total)
