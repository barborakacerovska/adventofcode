digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def get_coordinates(text: str):
    numbers = [None] * len(text)
    for value, digit in enumerate(digits, 1):
        position = -1
        while True:
            position = text.find(digit, position + 1)
            if position == -1:
                break
            numbers[position] = value

    for position, char in enumerate(text):
        if char.isnumeric():
            numbers[position] = int(char)
    numbers = list(filter(lambda item: item is not None, numbers))
    return int(f"{numbers[0]}{numbers[-1]}")


def get_coordinates(text: str):
    # Initialize a list of None values, with the same length as the input text
    numbers = [None] * len(text)

    # Define a string of digits from '0' to '9'
    digits = "0123456789"

    # Iterate over each digit, starting from '1' (because enumerate starts at 1 here)
    for value, digit in enumerate(digits, 1):
        position = -1  # Start searching from the beginning of the text
        while True:
            # Find the position of the current digit in the text, starting from 'position + 1'
            position = text.find(digit, position + 1)
            if position == -1:  # If the digit is not found, exit the loop
                break
            numbers[
                position
            ] = value  # Assign the corresponding value to the position in the list

    # Iterate over each character in the text
    for position, char in enumerate(text):
        if char.isnumeric():  # If the character is a number
            numbers[position] = int(
                char
            )  # Convert it to an integer and store it at the same position

    # Filter out None values from the 'numbers' list
    numbers = list(filter(lambda item: item is not None, numbers))

    # Convert the first and the last number in the list to a string and concatenate them
    # Then, convert the resulting string back to an integer
    return int(f"{numbers[0]}{numbers[-1]}")


def main():
    sum = 0
    with open("input") as f:
        for line in f:
            sum += get_coordinates(line)
    print(sum)


if __name__ == "__main__":
    main()
