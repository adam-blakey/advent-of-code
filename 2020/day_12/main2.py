import math

data_file  = open("advent_of_code_2020/day_12/data.dat", "r")
data_lines = data_file.read().split('\n')

way_start_x = 10
way_start_y = 1

way_x = way_start_x
way_y = way_start_y

ship_x = 0
ship_y = 0

for line in data_lines:
    instruction = line[0]
    value       = int(line[1:])

    if instruction == "F":
        ship_x += value*way_x
        ship_y += value*way_y
    elif instruction == "L":
        old_way_x = way_x
        old_way_y = way_y

        if value == 90:
            way_x = -old_way_y
            way_y = old_way_x
        elif value == 180:
            way_x = -way_x
            way_y = -way_y
        elif value == 270:
            way_x = old_way_y
            way_y = -old_way_x
    elif instruction == "R":
        old_way_x = way_x
        old_way_y = way_y

        if value == 90:
            way_x = old_way_y
            way_y = -old_way_x
        elif value == 180:
            way_x = -way_x
            way_y = -way_y
        elif value == 270:
            way_x = -old_way_y
            way_y = old_way_x
    elif instruction == "N":
        way_y += value
    elif instruction == "E":
        way_x += value
    elif instruction == "S":
        way_y -= value
    elif instruction == "W":
        way_x -= value

    print(way_x)
    print(way_y)
    print(ship_x)
    print(ship_y)
    print()

print("FINAL")
print(ship_x)
print(ship_y)
print(abs(ship_x) + abs(ship_y))