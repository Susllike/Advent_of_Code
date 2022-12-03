with open("input.txt", "r") as file:
	elf_list = file.readlines()

biggest_elf = 0
current_elf = 0

for line in elf_list:
	if line != "\n":
		current_elf += int(line)

	else:
		if biggest_elf < current_elf:
			biggest_elf = current_elf
		current_elf = 0

print(biggest_elf)
