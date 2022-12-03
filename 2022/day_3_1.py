PRIORITY = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Input reading
with open("input.txt", "r") as file:
	lines = file.readlines()

# Newline cleanup
for i in range(len(lines)):
	lines[i] = lines[i][:-1]

total = 0

for rucksack in lines:
	left = set(rucksack[0:len(rucksack)//2])
	right = set(rucksack[len(rucksack)//2:])

	intersection = list(left.intersection(right))[0]

	total += (PRIORITY.index(intersection) + 1)

print(total)
