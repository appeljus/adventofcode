# %%
import re

# %% input
with open('./2023/day4/input/input.txt', 'r', encoding='utf-8') as fp:
# with open('./input/input.txt', 'r', encoding='utf-8') as fp:
    input_file = fp.readlines()

# %% Solution for puzzle 1
result = 0
for line in input_file:
    winning_numbers = re.findall(r'\d+', line.split("|")[0].split(":")[1])
    own_numbers = re.findall(r'\d+', line.split("|")[1])
    assert len(winning_numbers) == 10
    assert len(own_numbers) == 25
    sub_result = 0
    for i in range(len(set(own_numbers).intersection(set(winning_numbers)))):
        if i == 0:
            sub_result = 1
        else:
            sub_result *= 2
    result += sub_result

print(f"Solution for puzzle 1: {result}")

# %% Parse input for puzzle 2
cards = []
for line in input_file:
    card_id = re.findall(r'\d+', line)[0]
    winning_numbers = re.findall(r'\d+', line.split("|")[0].split(":")[1])
    own_numbers = re.findall(r'\d+', line.split("|")[1])
    cards.append({
        "card_id": int(card_id),
        "winning_numbers": winning_numbers,
        "own_numbers": own_numbers,
        "type": "original"
    })

# %% Solution for puzzle 2
max_index = max(x["card_id"] for x in cards)
for card in cards:
    index = int(card["card_id"])
    winning_numbers = card["winning_numbers"]
    own_numbers = card["own_numbers"]
    number_of_winning_numbers = len(set(own_numbers).intersection(set(winning_numbers)))
    end_of_range = min(index + number_of_winning_numbers + 1, max_index)
    if number_of_winning_numbers > 0:
        for i in range(index + 1, end_of_range):
            card_to_copy = [x for x in cards if x["type"] == "original" and x["card_id"] == i][0]
            card_copy = {
                **card_to_copy,
                "type": "copy",
            }
            cards.append(card_to_copy)

print(f"Solution for puzzle 2: {len(cards)}")
