data_file  = open("advent_of_code_2020/day_14/data.dat", "r")
data_lines = data_file.read().split('\n')

memory_dictionary = {}
for line in data_lines:
    if line[0:4] == "mask":
        mask = line[7:]
    elif line[0:3] == "mem":
        right_bracket = line.find(']')
        equals        = line.find('=')

        memory_location = line[4:right_bracket]
        value           = int(line[equals+2:])
        value_2         = str(bin(value))[2:].zfill(36)

        new_value_2 = ''
        for i in range(len(mask)):
            mask_char  = mask[i]
            value_char = value_2[i]

            if mask_char == 'X':
                new_value_2 += value_char
            elif mask_char == '1':
                new_value_2 += '1'
            elif mask_char == '0':
                new_value_2 += '0'

        new_value = int(new_value_2, 2)

        memory_dictionary[memory_location] = new_value

output = 0
for entry in memory_dictionary:
    output += memory_dictionary[entry]

print(output)