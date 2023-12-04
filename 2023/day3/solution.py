# %%
import re

# %% input
with open('./2023/day3/input/input.txt', 'r', encoding='utf-8') as fp:
    input_file = fp.readlines()

# %% Parse input for puzzle 1
numbers_with_index = []
for i, line in enumerate(input_file):
    numbers = re.finditer(r"\d+", line.strip())
    for number in numbers:
        numbers_with_index.append({
            "number": number.group(),
            "start_index": number.start(),
            "end_index": number.end(),
            "row_index": i,
        })

 # %% Puzzle 1
result = 0
for number_with_index in numbers_with_index:
    row_index = number_with_index["row_index"]
    start_index = number_with_index["start_index"]
    end_index = number_with_index["end_index"]
    current_row = input_file[row_index].strip()
    preceeding_char = "" if start_index == 0 else current_row[start_index - 1]
    succeeding_char = "" if end_index == len(current_row) else current_row[end_index]
    if row_index == 0:
        previous_row_in_range = ""
    else:
        previous_row = input_file[row_index - 1].strip()
        previous_preceeding_char = "" if start_index == 0 else previous_row[start_index - 1]
        previous_succeeding_char = "" if end_index == len(previous_row) else previous_row[end_index]
        previous_row_in_range = (
            previous_preceeding_char +
            previous_row[start_index:end_index] +
            previous_succeeding_char
        ).strip()
    if row_index + 1 == len(input_file):
        next_row_in_range = ""
    else:
        next_row = input_file[row_index + 1].strip()
        next_preceeding_char = "" if start_index == 0 else next_row[start_index - 1]
        next_succeeding_char = "" if end_index == len(next_row) else next_row[end_index]
        next_row_in_range = (
            next_preceeding_char +
            next_row[start_index:end_index] +
            next_succeeding_char
        )
    string_to_search = (
        previous_row_in_range +
        preceeding_char +
        succeeding_char +
        next_row_in_range
    )
    if not all(char == "." or char in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] for char in string_to_search):
        result += int(number_with_index["number"])
print(f"Solution for puzzle 1: {result}")

# %% Parse input for puzzle 2
stars_with_index = []
for i, line in enumerate(input_file):
    stars = re.finditer(r"\*", line.strip())
    for star in stars:
        stars_with_index.append({
            "number": star.group(),
            "index": star.start(),
            "row_index": i,
        })

# %% Puzzle 2
result = 0
for star_with_index in stars_with_index:
    row_index = star_with_index["row_index"]
    index = star_with_index["index"]
    part_numbers_in_range = [
        part_number
        for part_number in numbers_with_index
        if (
            part_number["row_index"] in [row_index - 1, row_index, row_index + 1] and
            (
                part_number["start_index"] in [index - 1, index, index + 1] or
                part_number["end_index"] - 1 in [index - 1, index, index + 1]
            )
        )
    ]
    if len(part_numbers_in_range) == 2:
        result += int(part_numbers_in_range[0]["number"]) * int(part_numbers_in_range[1]["number"])
print(f"Solution for puzzle 2: {result}")
