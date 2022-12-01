import os

file = open(os.path.dirname(os.path.abspath(__file__)) + "/data.txt", "r")

max = 0
currentTotal = 0

# loop through all lines in the file
for line in file:
    if line.strip() == '':
        if currentTotal > max:
            max = currentTotal
        currentTotal = 0
    else:
        currentTotal += int(line)

file.close()

# check current total when reaching end of file
if currentTotal > max:
    max = currentTotal

print('answer', max)