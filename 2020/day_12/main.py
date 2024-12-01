data_file  = open("advent_of_code_2020/day_12/data.dat", "r")
data_lines = data_file.read().split('\n')

start_x = 0
start_y = 0
start_d = 1 # N = 0, E = 1, S = 2, W = 3

x = start_x
y = start_y
d = start_d

for line in data_lines:
    instruction = line[0]
    value       = int(line[1:])

    if instruction == "F":
        if d == 0:
           y += value
        elif d == 1:
           x += value
        elif d == 2:
           y -= value
        elif d == 3:
           x -= value
    elif instruction == "L":
        if value == 0:
            d = d
        elif value == 90:
            d = (d-1) % 4
        elif value == 180:
            d = (d-2) % 4
        elif value == 270:
            d = (d-3) % 4
    elif instruction == "R":
        if value == 0:
            d = d
        elif value == 90:
            d = (d+1) % 4
        elif value == 180:
            d = (d+2) % 4
        elif value == 270:
            d = (d+3) % 4
    elif instruction == "N":
        y += value
    elif instruction == "E":
        x += value
    elif instruction == "S":
        y -= value
    elif instruction == "W":
        x -= value

    print(x)
    print(y)
    print(d)
    print()

print("FINAL")
print(x)
print(y)
print(abs(x) + abs(y))