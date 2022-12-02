import os

enemy = {
    "A": 1, # Rock
    "B": 2, # Paper
    "C": 3  # Scissors
}

player = {
    "X": 1, # Rock
    "Y": 2, # Paper
    "Z": 3  # Scissors
}

total = 0

file = open(os.path.dirname(os.path.abspath(__file__)) + "/data.txt", "r")

for line in file:
    letters = line.strip().split(' ')

    total += player[letters[1]]

    if (enemy[letters[0]] == player[letters[1]]):
        total += 3
    elif ((letters[1] == 'X' and letters[0] == 'C') or (letters[1] == 'Y' and letters[0] == 'A') or (letters[1] == 'Z' and letters[0] == 'B')):
        total += 6     

file.close()

print(total)
