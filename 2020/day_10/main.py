data_file  = open("advent_of_code_2020/day_10/data.dat", "r")
data_lines = list(map(int, data_file.read().split('\n')))

data_lines.sort()

diff1 = 0
diff3 = 0

difference = data_lines[0] - 0

if (difference == 1):
    diff1 += 1
elif (difference == 3):
    diff3 += 1

for i in range(len(data_lines)-1):
    difference = data_lines[i+1] - data_lines[i]

    if (difference == 1):
        diff1 += 1
    elif (difference == 3):
        diff3 += 1

diff3 += 1

print(diff1)
print(diff3)
print(diff1*diff3)