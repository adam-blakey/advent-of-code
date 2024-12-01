import itertools

data_file  = open("advent_of_code_2020/day_9/data.dat", "r")
data_lines = data_file.read().split('\n')

def checkValidity(test_no):
    for i in range(test_no, len(data_lines)):
        test_lines = data_lines[i-test_no:i]

        current_line = data_lines[i]

        found = False
        for a, b in itertools.combinations(test_lines, 2):
            if int(a)+int(b) == int(current_line):
                found = True
                break
        
        if not found:
            print("error in " + str(i) + " with " + data_lines[i])
            return False

    return True

def findRange(baddie):
    for test_no in range(2, 25):
        for i in range(test_no, len(data_lines)):
            test_lines = data_lines[i-test_no:i]

            current_line = data_lines[i]

            found = False
            for nums in itertools.combinations(test_lines, test_no):
                if sum(map(int, nums)) == baddie:
                    found = True
                    break
            
            if found:
                print("Found with " + str(test_no) + " with")
                print(nums)
                print("Max is " + str(max(map(int, nums))))
                print("Min is " + str(min(map(int, nums))))
                print("Sum is " + str(max(map(int, nums)) + min(map(int, nums))))
                return True

    return False

## PART 1 ##
print(checkValidity(25))

## PART 2 ##
badNumber = 1930745883

print(findRange(badNumber))