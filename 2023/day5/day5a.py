import re

numbers_matched = []

with open("2023/day4/input.txt") as f:
    for line in f:
        # card number is the first number in the string
        card = int(re.search("\d+", line).group())
        colon_position = line.index(":")
        pipe_position = line.index("|")
        subA = line[colon_position + 1 : pipe_position]
        subB = line[pipe_position:]
        # find numbers --> list
        matches = 0
        for number in re.findall("\d+",subB):
            if number in re.findall("\d+",subA):
                matches += 1
        numbers_matched.append(matches)
    result = 0
    for matches in numbers_matched:
        if matches != 0:
            result += 2**(matches-1)
    print(result)
