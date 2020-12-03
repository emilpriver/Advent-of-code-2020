""" Advent of code day 3 part 1 """

with open("input.txt") as text_file:
  lines = list(text_file.readlines())
  total_tress = 0
  line_index = 0

  for (index, line) in enumerate(lines):
    if index == 0:
      continue

    line = line.strip("\n")
    line_index = index

    if len(line) <= (line_index * 3) + 3:
      line_index = 0

    if len(line) > line_index * 3 and line[(line_index * 3)]:
      if line[(line_index * 3)] == "#":
        total_tress += 1


  print(total_tress)
