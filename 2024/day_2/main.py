def are_levels_safe(level1, level2, increasing):
  if increasing:
    if level1 <= level2:
      return False
  else:
    if level1 >= level2:
      return False

  if abs(level1 - level2) > 3:
    return False
  
  return True

def is_report_safe(levels):
  increasing = int(levels[0]) < int(levels[1])
  for i in range(1, len(levels)):
    if not are_levels_safe(int(levels[i]), int(levels[i-1]), increasing):
      return False
  
  return True

def main(file):
  no_safe = 0

  with open(file) as f:
    for report_raw in f:
      cleaned_report_raw = report_raw.strip('\\n').split(' ')
      for j in range(len(cleaned_report_raw)):
        report = cleaned_report_raw.copy()
        report.pop(j)

        if is_report_safe(report):
          no_safe += 1
          break
  
  return no_safe

assert main('test.dat') == 4
print(main('input.dat')) 

  