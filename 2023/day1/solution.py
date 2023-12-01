# %%
import re

# %% input
with open('./2023/day1/input/input.txt', 'r', encoding='utf-8') as fp:
    input_file = fp.readlines()

# %% puzzle 1
result = 0
for line in input_file:
    line = line.strip()
    digits = [x for x in line if x.isdigit()]
    result += int(digits[0] + digits[-1])
print(f"Result for puzzle 1: {result}")

# %% puzzle 2
string_to_digit =  {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
result = 0
for line in input_file:
    digits = re.findall(r'\d', line)
    string_digits =  re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine))', line)

    if not digits:
        first_digit = string_to_digit[string_digits[0]]
        last_digit = string_to_digit[string_digits[-1]]
    elif not string_digits:
        first_digit = digits[0]
        last_digit = digits[-1]
    else:
        if line.index(digits[0]) < line.index(string_digits[0]):
            first_digit = digits[0]
        else:
            first_digit = string_to_digit[string_digits[0]]

        if line.rindex(digits[-1]) < line.rindex(string_digits[-1]):
            last_digit = string_to_digit[string_digits[-1]]
        else:
            last_digit = digits[-1]
    result += int(str(first_digit) + str(last_digit))
print(f"Result for puzzle 2: {result}")
