def main(file):
  import re

  valid_regex = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
  result = 0
  with open(file) as f:
    for raw_data in f:
      valid_expressions = re.findall(valid_regex, raw_data)

      for expression in valid_expressions:
        operands = expression.replace("mul(", "").replace(")", "").split(",")
        result += int(operands[0]) * int(operands[1])

  return result

assert main("test.dat") == 161
print(main("input.dat"))
