import re

translation_dictionary = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find_values(text, words, translation_dictionary):
    # Search for numbers
    number_match = re.search(r"\d", text)
    if number_match:
        return number_match.group()
    # Search for words
    for word in words:
        if word in text:
            return translation_dictionary[word]
    return None


def words_to_numbers(line, translation_dictionary):
    words = translation_dictionary.keys()
    calibration_values = []

    # Postupně zepředu přidávám znaky a hledám match
    for i in range(1, len(line) + 1):
        text = line[:i]
        value = find_values(text, words, translation_dictionary)
        if value:
            calibration_values.append(value)
            break

    # přidávám znaky odzadu
    for i in range(len(line) - 1, -1, -1):
        text = line[i:]
        value = find_values(text, words, translation_dictionary)
        if value:
            calibration_values.append(value)
            break

    return calibration_values


def main():
    with open("2023/day1/input.txt", "r") as file:
        total = 0
        for line in file.readlines():
            # translate words to numbers using dictionary
            calibration_values = words_to_numbers(line, translation_dictionary)
            # spojeni dvou cisel a pricteni k totalu
            total = total + int((calibration_values[0] + calibration_values[1]))
    return total


if __name__ == "__main__":
    print(main())
