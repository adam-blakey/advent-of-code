import itertools

# Open data file and add data to list.
data_file = open("advent_of_code_2020/day_1/data.dat", "r")
data = map(int, data_file.read().split('\n'))

# Loop over every combination until we get a match.
number_we_want = 2020
for x, y, z in itertools.combinations(data, 3):
	if (x+y+z == number_we_want):
         break

print(x*y*z)