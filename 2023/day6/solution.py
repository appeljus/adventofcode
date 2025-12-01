# %%
import re
import math

# %% input
# with open('./2023/day5/input/input.txt', 'r', encoding='utf_8') as fp:
with open('./input/input.txt', 'r', encoding='utf_8') as fp:
    input_file = fp.readlines()

# %% Parse input
times = [int(x) for x in re.findall(r'\d+', input_file[0])]
distances = [int(x) for x in re.findall(r'\d+', input_file[1])]
races = list(zip(times, distances))

# %% Solution for puzzle 1
result = 1
for race in races:
    time = race[0]
    distance = race[1]
    d = (time**2) - (4*(time - distance))
    from_faster = (-time-math.sqrt(d))/(2)
    to_faster = (-time+math.sqrt(d))/(2)
    result *= len(range(math.ceil(from_faster), math.ceil(to_faster)))
print(f"Solution for puzzle 1: {result}")
# %%
