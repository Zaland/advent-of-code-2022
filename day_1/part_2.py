import os

file = open(os.path.dirname(os.path.abspath(__file__)) + "/data.txt", "r")

list = []
currentTotal = 0

# loop through all lines in the file
for line in file:
    if line.strip() == '':
        list.append(currentTotal)
        currentTotal = 0
    else:
        currentTotal += int(line)

file.close()

# sort the list
list.sort(reverse=True)

print('1st Elf', list[0])
print('2nd Elf', list[1])
print('3rd Elf', list[2])

print('Total calories:', list[0] + list[1] + list[2])