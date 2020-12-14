def passwordValid(passwordPolicy):
    hyphenIndex    = passwordPolicy.find('-')
    colonIndex     = passwordPolicy.find(':')
    characterIndex = colonIndex-1

    mn = int(passwordPolicy[0:hyphenIndex])
    mx = int(passwordPolicy[hyphenIndex+1:characterIndex-1])

    char = passwordPolicy[characterIndex]

    password = passwordPolicy[colonIndex+1:]

    occurences = password.count(char)

    return (mn <= occurences and occurences <= mx)

def passwordValid2(passwordPolicy):
    hyphenIndex    = passwordPolicy.find('-')
    colonIndex     = passwordPolicy.find(':')
    characterIndex = colonIndex-1

    pos1 = int(passwordPolicy[0:hyphenIndex])
    pos2 = int(passwordPolicy[hyphenIndex+1:characterIndex-1])

    char = passwordPolicy[characterIndex]

    password = passwordPolicy[colonIndex+1:]

    return ((password[pos1] == char) != (password[pos2] == char))

data_file  = open("advent_of_code_2020/day_2/data.dat", "r")
data_lines = data_file.read().split('\n')

## PART 1 ##
valid = 0
for line in data_lines:
    if passwordValid(line):
        valid += 1

print(valid)

## PART 2 ##
valid = 0
for line in data_lines:
    if passwordValid2(line):
        valid += 1

print(valid)