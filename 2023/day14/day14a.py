
import re

with open("2023/day14/input.txt") as f:
    lines = f.read().splitlines()
    n_rows = len(lines)
    transponsed_list = ["".join(row) for row in zip(*lines)]
    summary = 0
    pattern = re.compile(r"#")

    for line in transponsed_list:
        # Find all matches of '#' and get their starting positions
        _positions = [match.start() for match in pattern.finditer(line)]
        positions = list(set([0] + _positions + [len(line)]))
        positions.sort()
        for i in range(len(positions) - 1):
            line_part = line[positions[i] : positions[i + 1]]
            stones = line_part.count("O")
            # shift kvuli sloupcum co nezacinaji #
            if (i == 0 and 0 not in _positions) or i == len(line):
                shift = 0
            else:
                shift = 1
            summary += (n_rows - positions[i] - shift) * stones - (
                (stones - 1) * stones
            ) / 2
    print(summary)
