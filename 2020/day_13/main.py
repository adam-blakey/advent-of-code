data_file  = open("advent_of_code_2020/day_13/data.dat", "r")
data_lines = data_file.read().split('\n')

arrival_time = int(data_lines[0])

buses = []
for line in data_lines[1].split(','):
    if line != 'x':
        buses.append(int(line))

wait = -1
found_bus = 0
while(found_bus == 0):
    wait += 1
    for bus in buses:
        if (arrival_time+wait) % bus == 0:
            found_bus = bus
            break

print("Wait: " + str(wait))
print("Bus:  " + str(found_bus))
print(wait*found_bus)