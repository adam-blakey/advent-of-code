data_file  = open("advent_of_code_2020/day_8/data.dat", "r")
data_lines = data_file.read().split('\n')

accumulator = 0

instruction_order = []
looping = True
lineNo = 0
while looping:
    if lineNo >= len(data_lines):
        break

    line = data_lines[lineNo]

    instruction = line[0:3]

    if lineNo in instruction_order or lineNo==len(data_lines):
        break
        #looping = False

    instruction_order.append(lineNo)
    
    if instruction == "nop":
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
        sign  = line[4]
        value = line[5:]

        if sign == "+":
            lineNo += int(value)
        else:
            lineNo -= int(value)

print(accumulator)