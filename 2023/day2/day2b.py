import re

powers = []


def get_max_value(list):
    numbers = [int(i) for i in list]
    return max(numbers)


def compare_with_bag(max_colors_dict):
    bag = {"blue": 14, "red": 12, "green": 13}
    if (
        bag["blue"] < max_colors_dict["blue"]
        or bag["green"] < max_colors_dict["green"]
        or bag["red"] < max_colors_dict["red"]
    ):
        return False
    else:
        return True


with open("2023/day2/input.txt") as f:
    for line in f:
        # game number is the first number in the string
        game = int(re.search("\d+", line).group())
        # find all occurences and get me only the numbers associated with colors
        red = re.findall("(\d+)\s*red", line)
        blue = re.findall("(\d+)\s*blue", line)
        green = re.findall("(\d+)\s*green", line)
        # find the maximum value for each color
        max_colors_dict = {
            "blue": get_max_value(blue),
            "red": get_max_value(red),
            "green": get_max_value(green),
        }
        power = max_colors_dict["blue"] * max_colors_dict["red"] * max_colors_dict["green"]
        powers.append(power)
    print(sum(powers))
