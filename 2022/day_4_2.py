total = 0

with open("input.txt", "r") as file:
	lines = file.readlines()

for line in lines:
	line = line[:-1].split(",")
	left = line[0].split("-")
	right = line[1].split("-")

	left_set = set([i for i in range(int(left[0]), int(left[1]) + 1)])
	right_set = set([i for i in range(int(right[0]), int(right[1]) + 1)])

	if len(left_set.intersection(right_set)) > 0:
		total += 1

print(total)
