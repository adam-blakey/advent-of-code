# Open data file and add data to list.
#   data_passport has each entry per passport.
data_file     = open("advent_of_code_2020/day_4/data.dat", "r")
data_raw      = data_file.read().split('\n')

# Combine individual fields into passports.
last_i = 0
data_lines = []
for i in range(len(data_raw)):
    if data_raw[i] == '' or i==len(data_raw)-1:
        content = ''
        for j in range(last_i, i):
            content += data_raw[j] + ' ' 

        data_lines.append(content)
        last_i = i+1

#print(len(data_lines))

# Loop over all passports to build dictionaries.
passports = []
for i in range(len(data_lines)):
    data_passport_individual = data_lines[i].split(' ')
    passports.append({})
    for j in range(len(data_passport_individual)):
        key, sep, val = data_passport_individual[j].partition(':')
        if key != '':
            passports[i][key.strip()] = val.strip()
        
# Checks all passports to see which are valid.
valid_count = 0
for i in range(len(passports)):
    valid = True
    fieldCount = 8

    if "ecl" not in passports[i]:
        valid = False
        fieldCount -= 1
    elif not (passports[i]["ecl"] == "amb" or passports[i]["ecl"] == "blu" or passports[i]["ecl"] == "brn" or passports[i]["ecl"] == "gry" or passports[i]["ecl"] == "grn" or passports[i]["ecl"] == "hzl" or passports[i]["ecl"] == "oth"):
        valid = False

    if "pid" not in passports[i]:
        valid = False
        fieldCount -= 1
    elif len(passports[i]["pid"]) != 9:
        valid = False
    else:
        try:
            int(passports[i]["pid"])
        except ValueError:
            valid = False

    if "eyr" not in passports[i]:
        valid = False
        fieldCount -= 1
    elif 2020 > int(passports[i]["eyr"]) or int(passports[i]["eyr"]) > 2030:
        valid = False

    if "hcl" not in passports[i] or passports[i]["hcl"] == '':
        valid = False
        fieldCount -= 1
    elif passports[i]["hcl"][0] != "#" or not int(passports[i]["hcl"][-1:], 16):
        valid = False

    if "byr" not in passports[i] or passports[i]["byr"] == '':
        valid = False
        fieldCount -= 1
    elif 1920 > int(passports[i]["byr"]) or int(passports[i]["byr"]) > 2002:
        valid = False

    if "iyr" not in passports[i]:
        valid = False
        fieldCount -= 1
    elif 2010 > int(passports[i]["iyr"]) or int(passports[i]["iyr"]) > 2020:
        valid = False

    if "hgt" not in passports[i]:
        valid = False
        fieldCount -= 1
    elif passports[i]["hgt"][-2:] == "cm":
        if 150 > int(passports[i]["hgt"][:-2]) or int(passports[i]["hgt"][:-2]) > 193:
            valid = False
    elif passports[i]["hgt"][-2:] == "in":
        if 59 > int(passports[i]["hgt"][:-2]) or int(passports[i]["hgt"][:-2]) > 76:
            valid = False
    else:
        valid = False

    #if "cid" not in passports[i]:
    #    valid = False


    if valid:
        valid_count += 1
    #elif fieldCount == 8:
        #print(passports[i])

    #if "pid" in passports[i] and passports[i]["pid"] == "185953891":
    #    print(valid)

print(valid_count)