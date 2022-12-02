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

    if (letters[1] == 'Y'):
        total += 3 + enemy[letters[0]]
    elif (letters[1] == 'X'):
        if (letters[0] == 'A'):
            total += player['Z']
        elif (letters[0] == 'B'):
            total += player['X']
        else:
            total += player['Y']
    else:
        total += 6
        if (letters[0] == 'A'):
            total += player['Y']
        elif (letters[0] == 'B'):
            total += player['Z']
        else:
            total += player['X']  

file.close()

print(total)
