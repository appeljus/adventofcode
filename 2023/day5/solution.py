# %%
import re

# %% input
# with open('./2023/day5/input/input.txt', 'r', encoding='utf_8') as fp:
with open('./input/input.txt', 'r', encoding='utf_8') as fp:
    input_file = fp.read()

# %%
def create_mapping(mapping_strings: list):
    result = []
    for mapping_string in mapping_strings:
        numbers = [int(x) for x in re.findall(r'\d+', mapping_string)]
        result.append({
            "source_start_index": numbers[1],
            "source_end_index": numbers[1] + numbers[2],
            "destination_start_index": numbers[0],
            "range": numbers[2],
        })
    return result


# %% Parse input for puzzle 1
split_input = input_file.split("\n\n")
seeds = re.findall(r'\d+', split_input[0])

seed_to_soil = split_input[1].split('\n')
assert "seed-to-soil map" in seed_to_soil[0]
seed_to_soil = seed_to_soil[1:]
seed_to_soil_mapping = create_mapping(seed_to_soil)

soil_to_fertilizer = split_input[2].split('\n')
assert "soil-to-fertilizer map" in soil_to_fertilizer[0]
soil_to_fertilizer = soil_to_fertilizer[1:]
soil_to_fertilizer_mapping = create_mapping(soil_to_fertilizer)

fertilizer_to_water = split_input[3].split('\n')
assert "fertilizer-to-water map" in fertilizer_to_water[0]
fertilizer_to_water = fertilizer_to_water[1:]
fertilizer_to_water_mapping = create_mapping(fertilizer_to_water)

water_to_light = split_input[4].split('\n')
assert "water-to-light map" in water_to_light[0]
water_to_light = water_to_light[1:]
water_to_light_mapping = create_mapping(water_to_light)

light_to_temperature = split_input[5].split('\n')
assert "light-to-temperature map" in light_to_temperature[0]
light_to_temperature = light_to_temperature[1:]
light_to_temperature_mapping = create_mapping(light_to_temperature)

temperature_to_humidity = split_input[6].split('\n')
assert "temperature-to-humidity map" in temperature_to_humidity[0]
temperature_to_humidity = temperature_to_humidity[1:]
temperature_to_humidity_mapping = create_mapping(temperature_to_humidity)

humidity_to_location = split_input[7].split('\n')
assert "humidity-to-location map" in humidity_to_location[0]
humidity_to_location = humidity_to_location[1:]
humidity_to_location_mapping = create_mapping(humidity_to_location)

mappings = [
    seed_to_soil_mapping,
    soil_to_fertilizer_mapping,
    fertilizer_to_water_mapping,
    water_to_light_mapping,
    light_to_temperature_mapping,
    temperature_to_humidity_mapping,
    humidity_to_location_mapping,
]
# %% Solution for puzzle 1
locations = []
for seed in seeds:
    current_id = int(seed)
    path = [seed]
    for mapping in mappings:
        for row in mapping:
            if row["source_start_index"] <= current_id < row["source_end_index"]:
                current_id = current_id - row["source_start_index"] + row["destination_start_index"]
                break
        path.append(current_id)
    locations.append(current_id)

print(f"Solution for puzzle 1: {min(locations)}")
# %%
