data_file  = open("advent_of_code_2020/day_7/data.dat", "r")
data_lines = data_file.read().split('\n')

associated_bags = {}

for line in data_lines:
    line_contain = line.split('contain')
    big_bag      = line_contain[0].rstrip()[:-1]
    littler_bags = line_contain[1][1:].split(',')

    sub_associated_bags = []
    for bag in littler_bags:
        bag_stuff = bag.lstrip().rstrip('.').rstrip()
        bag_num   = bag_stuff[0]
        bag_name  = bag_stuff[2:].rstrip()

        if bag_num != '1':
            bag_name = bag_name[:-1]
        
        if bag_name != " other bag":
            sub_associated_bags.append(bag_name)

    associated_bags[big_bag] = sub_associated_bags

def bagFound(sought_bag, bag_to_look_in, level = 0, searched_bags = []):
    for sub_bag in associated_bags[bag_to_look_in]:
        level += 1
        if sub_bag not in searched_bags:
            if sub_bag == sought_bag:
                return True
            else:
                searched_bags.append(sub_bag)
                if bagFound(sought_bag, sub_bag, level, searched_bags):
                    return True

    return False

def bagCount(sought_bag):
    bags_to_consider = []
    count = 0
    for bag in associated_bags:
        if bagFound(sought_bag, bag, count):
            bags_to_consider.append(bag)

    print(count)


#print(bagFound('shiny gold bag', 'light red bag'))

counter = 0
for bag in associated_bags:
    searched_bags = []
    level = 0
    if bagFound('shiny gold bag', bag, level, searched_bags):
        counter += 1

print(counter)

bagCount('shiny gold bag')