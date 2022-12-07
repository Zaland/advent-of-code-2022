import os

stack = []
counter = 0

stack2 = []

with open(os.path.dirname(os.path.abspath(__file__)) + "/structure.txt", "r") as file:
    while (line := file.readline().rstrip()):
        letters = line.split(' ')

        stack.append([])
        stack2.append([])

        for index, letter in enumerate(letters):
            stack[counter].append(letter)
            stack2[counter].append(letter)
        
        counter += 1

with open(os.path.dirname(os.path.abspath(__file__)) + "/data.txt", "r") as file:
    while (line := file.readline().rstrip()):
        numbers = [int(s) for s in line.split() if s.isdigit()]

        tempStack = []

        for i in range(numbers[0]):
            poppedItem = stack[numbers[1] - 1].pop()
            stack[numbers[2] - 1].append(poppedItem)

            poppedItem2 = stack2[numbers[1] - 1].pop()
            tempStack.append(poppedItem2)

        for i in range(len(tempStack)):
            poppedItem = tempStack.pop()
            stack2[numbers[2] - 1].append(poppedItem)


solution = []
solution2 = []

for i in range(len(stack)):
    solution.append(stack[i].pop())

for i in range(len(stack2)):
    solution2.append(stack2[i].pop())

print('Part 1 solution:', ''.join(solution))
print('Part 2 solution:', ''.join(solution2))
