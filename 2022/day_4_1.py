total = 0

with open("input.txt", "r") as file:
	lines = file.readlines()

for line in lines:
	line = line[:-1].split(",")
	left = line[0].split("-")
	right = line[1].split("-")
	
	if ((int(left[0]) <= int(right[0]) and 
			int(left[1]) >= int(right[1])) 
		or 
		(int(right[0]) <= int(left[0]) and 
			int(right[1]) >= int(left[1]))):
		total += 1

print(total)
