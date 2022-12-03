PRIORITY = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Input reading
with open("input.txt", "r") as file:
	lines = file.readlines()

# Newline cleanup
for i in range(len(lines)):
	lines[i] = lines[i][:-1]

total = 0

# Steps of 3 to get elves in batches of 3
for i in range(0, len(lines), 3):
	elves = lines[i:i+3]
	
	first_intersection = set(elves[0]).intersection(elves[1])
	second_intersection = list(first_intersection.intersection(elves[2]))[0]

	total += (PRIORITY.index(second_intersection) + 1)

print(total)
