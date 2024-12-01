data_file  = open("advent_of_code_2020/day_8/data.dat", "r")
data_lines = data_file.read().split('\n')

def doesTerminate(modifiedLine):
    accumulator = 0

    instruction_order = []
    lineNo = 0
    while True:
        if lineNo >= len(data_lines):
            return True

        line = data_lines[lineNo]

        instruction = line[0:3]

        if lineNo in instruction_order:
            return False
        elif lineNo==len(data_lines):
            return True

        instruction_order.append(lineNo)
        
        if instruction == "nop":
            if lineNo==modifiedLine:
                sign  = line[4]
                value = line[5:]

                if sign == "+":
                    lineNo += int(value)
                else:
                    lineNo -= int(value)
            else:
                lineNo += 1  
        elif instruction == "acc":
            sign  = line[4]
            value = line[5:]

            if sign == "+":
                accumulator += int(value)
            else:
                accumulator -= int(value)

            lineNo += 1
        elif instruction == "jmp":
            if lineNo==modifiedLine:
                lineNo += 1
            else:
                sign  = line[4]
                value = line[5:]

                if sign == "+":
                    lineNo += int(value)
                else:
                    lineNo -= int(value)

for i in range(len(data_lines)):
    if (doesTerminate(i)):
        print("Yay! " + str(i))

# for i in range(len(instruction_order)):
#     print(str(instruction_order[i]) + ': ' + data_lines[instruction_order[i]])

# i = 247
# print(str(instruction_order[i]) + ': ' + data_lines[instruction_order[i]])


#print(accumulator)