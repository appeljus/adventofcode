# %%
import re
import os

# %% input
with open('./2023/day2/input/input.txt', 'r', encoding='utf-8') as fp:
    input_file = fp.readlines()

#%%
print(os.getcwd())

# %% Util functions
def parse_line(line: str):
    game_id = re.findall(r"\d+", line)[0]
    pulls = line.split(":")[-1]
    pulls = pulls.split(";")
    parsed_pulls = []
    i = 0
    for pull in pulls:
        blue_nr = re.findall(r"\d+(?= blue)", pull)
        blue_nr = int(blue_nr[0]) if blue_nr else 0
        green_nr = re.findall(r"\d+(?= green)", pull)
        green_nr = int(green_nr[0]) if green_nr else 0
        red_nr = re.findall(r"\d+(?= red)", pull)
        red_nr = int(red_nr[0]) if red_nr else 0
        parsed_pulls.append(
            {
                "index": i,
                "red_nr": red_nr,
                "blue_nr": blue_nr,
                "green_nr": green_nr,
            }
        )
        i += 1
    return {"game_id": game_id, "pulls": parsed_pulls}

# %% Puzzle 1
max_red_cubes = 12
max_green_cubes = 13
max_blue_cubes = 14
parsed_lines = []
for line in input_file:
    parsed_lines.append(parse_line(line))

# %%
result = 0
for game in parsed_lines:
    max_red = max(pull["red_nr"] for pull in game["pulls"])
    max_blue = max(pull["blue_nr"] for pull in game["pulls"])
    max_green = max(pull["green_nr"] for pull in game["pulls"])
    if max_red > max_red_cubes or max_blue > max_blue_cubes or max_green > max_green_cubes:
        continue
    else:
        result += int(game["game_id"])
print(f"Solution for puzzle 1: {result}")

# %%
result = 0
for game in parsed_lines:
    max_red = max(pull["red_nr"] for pull in game["pulls"])
    max_blue = max(pull["blue_nr"] for pull in game["pulls"])
    max_green = max(pull["green_nr"] for pull in game["pulls"])
    result += max_red * max_blue * max_green
print(f"Solution for puzzle 2: {result}")
