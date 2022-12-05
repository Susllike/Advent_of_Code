import re

initial = []

directions = []

with open("input.txt", "r") as file:
	for i in range(8):
		initial.append(file.readline()[:-1])

	start = []

	for i in range(len(initial)):
		new_line = []
		for j in range(0, len(initial[i]), 4):
			new_line.append(initial[i][j:j+3])

		start.append(new_line)

	# Skipping the numbering and an empty line
	file.readline()
	file.readline()

	# Formatting directions into [n1, n2, n3] lists
	while line := file.readline().rstrip():
		directions.append(list(map(int, re.findall(r"\d+", line))))

table = [[] for i in range(9)]

for i in range(9):
	for row in range(len(start)):
		if start[row][i] != "   ":
			table[i].append(start[row][i])

	table[i].reverse()

for direction in directions:
	moving_column = []
	from_column = direction[1] - 1
	to_column = direction[2] - 1

	for boxes_moved in range(direction[0]):
		moving_box = table[from_column].pop()
		moving_column.append(moving_box)
	
	moving_column.reverse()
	for box in moving_column:
		table[to_column].append(box)

for row in table:
	print(row)

for row	in table:
	print(row[-1][1], end = "")
