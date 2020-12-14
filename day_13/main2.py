import numpy as np

data_file  = open("advent_of_code_2020/day_13/data.dat", "r")
data_lines = data_file.read().split('\n')

buses = data_lines[1].split(',')

buses_num = []
for i in range(len(buses)):
    if buses[i] == 'x':
        buses_num.append(1)
    else:
        buses_num.append(int(buses[i])-i-2)

start_time = 1068773
end_time   = 1068900
for t in range(start_time, end_time):
    bus_here = []
    for bus in buses:
        if bus != 'x':
            if t % int(bus) == 0:
                bus_here.append('D')
            else:
                bus_here.append('.')

    format_row = "{:<8}"*(len(bus_here)+1)
    #print(format_row.format(t, *bus_here))

print()
#print(np.lcm.reduce(buses_num))
print(np.lcm(67, 67))
print(np.lcm(7, 6))
print(np.lcm(59, 57))
print(np.lcm(61, 58))

# 11254
# 1, 2, 17, 34, 331, 662, 5627, 11254

# 754018
# 1, 2, 17, 34, 67, 134, 331, 662, 1139, 2278, 5627, 11254, 22177, 44354, 377009, 754018




# 201: 17,x,13,19
# 1, 2, 3, 6, 17, 34, 51, 102