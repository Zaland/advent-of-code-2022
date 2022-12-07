import os

def part1():
    with open(os.path.dirname(os.path.abspath(__file__)) + "/data.txt", "r") as file:
        line = file.readline().rstrip()

        amount = 0
        while amount == 0:
            for index in range(len(line) - 4):
                current = ""
                for i in [0,1,2,3]:
                    if line[index + i] in current:
                        break
                    else:
                        current += line[index+i]
                if len(current) == 4:
                    amount = index + i + 1
                    break
        return amount

def part2():
    with open(os.path.dirname(os.path.abspath(__file__)) + "/data.txt", "r") as file:
        line = file.readline().rstrip()

        amount = 0
        while amount == 0:
            for index in range(len(line) - 14):
                current = ""
                for i in [0,1,2,3,4,5,6,7,8,9,10,11,12,13]:
                    if line[index + i] in current:
                        break
                    else:
                        current += line[index+i]
                if len(current) == 14:
                    amount = index + i + 1
                    break
        return amount



print('Part1:', part1())
print('Part2:', part2())