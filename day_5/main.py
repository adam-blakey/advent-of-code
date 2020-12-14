def boardingPassID(seatString):
    rowNoString = seatString[0:7].replace('F', '0').replace('B', '1')
    rowNo       = int(rowNoString, 2)

    colNoString = seatString[-3:].replace('L', '0').replace('R', '1')
    colNo       = int(colNoString, 2)

    return rowNo*8 + colNo

data_file  = open("advent_of_code_2020/day_5/data.dat", "r")
data_lines = data_file.read().split('\n')

## PART 1 ##
maxSeatID = 0
for line in data_lines:
    seatID = boardingPassID(line)
    if seatID > maxSeatID:
        maxSeatID = seatID
        
print(maxSeatID)

## PART 2 ##
seatFound = [False] * 920
for line in data_lines:
    seatID = boardingPassID(line)
    seatFound[seatID] = True

print("Missing seats:")
missingSeats = [i for i, x in enumerate(seatFound) if not x]
for seat in missingSeats:
    print(seat)