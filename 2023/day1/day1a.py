import re


def get_calibration_values(line):
    numbers = re.sub("\\D", "", line)
    # return first+last character
    return numbers[0] + numbers[-1]


def sum_numbers(list):
    "Sum all the values in the list"
    total = 0
    for number in list:
        total += int(number)
    return total


calibration_values = []


def main():
    with open("2023/day1/input.txt", "r") as file:
        for line in file.readlines():
            # get calibration values
            calibration_values.append(get_calibration_values(line))
        return sum_numbers(calibration_values)


if __name__ == "__main__":
    print(main())
