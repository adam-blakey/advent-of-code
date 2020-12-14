from string import ascii_lowercase

def characterFrequency(input):
    dictionary = {}
    for char in input:
        if char in dictionary:
            dictionary[char] += 1
        elif char != ' ':
            dictionary[char] = 1

    return dictionary

def uniqueDictionary(answers):
    temp = {}
    for char in ascii_lowercase:
        good = True
        for answer in answers[:-1]:
            if char not in answer:
                good = False

        if good:
            temp[char] = 1
    return temp

def countQuestions(questions):
    count = 0
    for question in questions:
        characterCount = characterFrequency(question)
        count += len(characterCount)

    return count

def countUniqueQuestions(questions):
    count = 0
    for question in questions:
        per_person = question.split(' ')
        answers = []
        for person in per_person:
            answers.append(characterFrequency(person))

        uniqueAnswers = uniqueDictionary(answers)
        count += len(uniqueAnswers)
    
    return count

# Open data file and add data to list.
#   data_passport has each entry per passport.
data_file     = open("advent_of_code_2020/day_6/data.dat", "r")
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

## PART 1 ##
print(countQuestions(data_lines))

## PART 2 ##
print(countUniqueQuestions(data_lines))