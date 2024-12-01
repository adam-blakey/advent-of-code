data_file  = open("advent_of_code_2020/day_3/data.dat", "r")
data_lines = data_file.read().split('\n')

def treeFinder(data_lines, right, down):
    treesFound = 0
    for i in range(0, len(data_lines), down):
        line = data_lines[i]
        lineLength = len(line)

        index = right*int(i/down)

        thing = line[index % lineLength]

        if thing == '#':
            treesFound += 1
    
    return treesFound

## PART 1 ##
print(treeFinder(data_lines, 3, 1))

## PART 2 ##
answer  = treeFinder(data_lines, 1, 1)
answer *= treeFinder(data_lines, 3, 1)
answer *= treeFinder(data_lines, 5, 1)
answer *= treeFinder(data_lines, 7, 1)
answer *= treeFinder(data_lines, 1, 2)

print(answer)