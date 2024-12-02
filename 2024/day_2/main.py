def is_report_safe(report):
  levels = report.strip('\\n').split(' ')
  prev_no = int(levels[0])
  increasing = int(levels[0]) < int(levels[1])
  for i in range(1, len(levels)):
    if increasing:
      if int(levels[i]) < prev_no:
        return False
    else:
      if int(levels[i]) > prev_no:
        return False

    if (int(levels[i]) - prev_no) == 0:
      return False

    if abs(int(levels[i]) - prev_no) > 3:
      return False
    
    prev_no = int(levels[i])
  
  return True

def main(file):
  no_safe = 0

  with open(file) as f:
    for report in f:
      if is_report_safe(report):
        no_safe += 1
  
  return no_safe

assert main('test.dat') == 2
print(main('input.dat')) 

  