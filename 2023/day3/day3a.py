import re
import numpy as np

numbers_to_add = []


def check_surroundings(text_list, start_position, index, length):
    row_before = index - 1 if index - 1 > 0 else 0
    row_after = index + 2 if index + 2 <= len(text_list) else len(text_list)
    start_index = start_position - 1 if start_position - 1 > 0 else 0
    end_index = (
        start_position + length + 1
        if start_position + length + 1 < len(text_list[0])
        else len(text_list[0])
    )

    text_array = np.array([list(string) for string in text_list])
    surroundings = text_array[row_before:row_after, start_index:end_index]
    array_to_string = "".join(surroundings.flatten())
    # kontrola, jestli jsou vsechny znaky alfanumeric
    if array_to_string.isalnum():
        return False
    return True


with open("2023/day3/input.txt") as f:
    # get the input as a list and replace "." for A so a dot is not a symbol anymore
    text = f.read().replace(".", "A")
    # udelam z textu slovnik
    text_list = text.splitlines()
    for index, row in enumerate(text_list):
        for match in re.finditer(r'(\d+)', row):
            number = match.group()
            length = len(number)
            start_position = match.start()
            if check_surroundings(text_list, start_position, index, length):
                numbers_to_add.append(int(number))

    print(sum(numbers_to_add))

