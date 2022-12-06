import os

part1Total = 0
part2Total = 0

with open(os.path.dirname(os.path.abspath(__file__)) + "/data.txt", "r") as file:
    while (line := file.readline().rstrip()):
        sections = line.split(',')

        section1 = sections[0].split('-')
        section2 = sections[1].split('-')

        if (
                (int(section1[0]) <= int(section2[0]) and int(section2[1]) <= int(section1[1])) or
                (int(section2[0]) <= int(section1[0]) and int(section1[1]) <= int(section2[1]))
            ):
            part1Total += 1
        
        if (
                (int(section2[0]) <= int(section1[0]) and int(section1[0]) <= int(section2[1])) or
                (int(section2[0]) <= int(section1[1]) and int(section1[1]) <= int(section2[1])) or 
                (int(section1[0]) <= int(section2[0]) and int(section2[0]) <= int(section1[1])) or
                (int(section1[0]) <= int(section2[1]) and int(section2[1]) <= int(section1[1]))
            ):
            part2Total += 1

print('Part 1 total =', part1Total)
print('Part 2 total =', part2Total)