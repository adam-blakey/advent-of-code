def get_file_input(file):
  list1 = []
  list2 = []
  with open(file) as f:
    for line in f:
      entries = line.split('   ')
      list1.append(int(entries[0]))
      list2.append(int(entries[1]))
  return list1, list2

def main(file):
  list1, list2 = get_file_input(file)
  list1 = sorted(list1)
  list2 = sorted(list2)

  difference = 0
  for i in range(len(list1)):
    difference += abs(list1[i] - list2[i])

  return difference

assert main('test.dat') == 11
print(main('input.dat')) 

  