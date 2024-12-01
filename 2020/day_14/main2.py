data_file  = open("./data.dat", "r")
data_lines = data_file.read().split('\n')

def write_combinations(number):
    number_list = []
    if number.find('X') >= 0:
        i = number.find('X')
        call1 = number[0:i] + '0' + number[i+1:]
        call2 = number[0:i] + '1' + number[i+1:]

        call1_list = write_combinations(call1)
        call2_list = write_combinations(call2)

        for item in call1_list:
            number_list.append(item)
        for item in call2_list:
            number_list.append(item)
    else:
        number_list.append(number)

    return number_list

def get_unique(a_list):
    o_list = []
    for item in a_list:
        if item not in o_list:
            o_list.append(item)

    return o_list

memory_dictionary = {}
for line in data_lines:
    if line[0:4] == "mask":
        mask = line[7:]
    elif line[0:3] == "mem":
        right_bracket = line.find(']')
        equals        = line.find('=')

        memory_location   = int(line[4:right_bracket])
        memory_location_2 = str(bin(memory_location))[2:].zfill(36)
        value             = int(line[equals+2:])
        value_2           = str(bin(value))[2:].zfill(36)

        new_memory_locations = ''
        for i in range(len(mask)):
            mask_char     = mask[i]
            location_char = memory_location_2[i]

            if mask_char == 'X':
                new_memory_locations += 'X'
            elif mask_char == '1':
                new_memory_locations += '1'
            elif mask_char == '0':
                new_memory_locations += location_char

            #memory_locations = get_unique(write_combinations(new_memory_locations))
            memory_locations = write_combinations(new_memory_locations)

        for location in memory_locations:
            memory_dictionary[location] = value_2

output = 0
for memory_location in memory_dictionary:
    output += int(memory_dictionary[memory_location], 2)

print(output)