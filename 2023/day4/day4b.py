import re

number_of_cards = 0

with open("2023/day4/input.txt") as f:
    f = f.readlines()
    # create a dict to keep number of repetitions
    repetition_dict = {i: 1 for i in range(1, len(f) + 1)}
    for line in f:
        # check matches
        card = int(re.search("\d+", line).group())
        colon_position = line.index(":")
        pipe_position = line.index("|")
        subA = line[colon_position + 1 : pipe_position]
        subB = line[pipe_position:]
        # find numbers transform to list and compare
        card_to_duplicate = card
        for number in re.findall("\d+", subB):
            if number in re.findall("\d+", subA):
                card_to_duplicate += 1
                # for the next cards add number of repetitions according to the number of copies of the current card
                repetition_dict[card_to_duplicate] += repetition_dict[card]

    print(sum(repetition_dict.values()))
