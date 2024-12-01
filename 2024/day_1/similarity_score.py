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


  # This is pretty horrific.
  similarity_score = 0
  for i in range(len(list1)):
    for j in range(len(list2)):
      if list1[i] == list2[j]:
        similarity_score += list1[i]

  return similarity_score

assert main('test.dat') == 31
print(main('input.dat')) 

  