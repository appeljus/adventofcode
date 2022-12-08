# %%

calories = 0
first_calories = 0
second_calories = 0
third_calories = 0


with open("input_puzzle_1.txt", 'r') as fp:
    for line in fp:
        if line == "\n":
            if calories > third_calories:
                if calories > second_calories:
                    if calories > first_calories:
                        third_calories = second_calories
                        second_calories = first_calories
                        first_calories = calories
                    else:
                        third_calories = second_calories
                        second_calories = calories
                else:
                    third_calories = calories
            calories = 0
        else:
            calories += int(line)

print(first_calories + second_calories + third_calories)
