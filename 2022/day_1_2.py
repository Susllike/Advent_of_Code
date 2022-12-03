with open("input.txt", "r") as file:
	elf_list = file.readlines()

all_elves = []
current_elf = 0

for line in elf_list:
	if line != "\n":
		current_elf += int(line)

	else:
		all_elves.append(current_elf)
		current_elf = 0

all_elves.sort()
all_elves.reverse()

print(sum(all_elves[0:3]))
