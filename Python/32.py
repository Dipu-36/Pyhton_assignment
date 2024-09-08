def capitalize_lines(lines):
  capitalized_lines = []
  for line in lines:
    capitalized_line = line.upper()
    capitalized_lines.append(capitalized_line)
  return capitalized_lines


input_lines = []
while True:
  line = input()
  if line == "":
    break
  input_lines.append(line)


capitalized_lines = capitalize_lines(input_lines)
for line in capitalized_lines:
  print(line)