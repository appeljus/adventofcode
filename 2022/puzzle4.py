# %%

def range_subset(range1, range2):
    """Whether range1 is a subset of range2."""
    if not range1:
        return True  # empty range is subset of anything
    if not range2:
        return False  # non-empty range can't be subset of empty range
    if len(range1) > 1 and range1.step % range2.step:
        return False  # must have a single value or integer multiple step
    return range1.start in range2 and range1[-1] in range2


def range_intersect(range1, range2):
    range_1_set = set(range1)
    intersect = range_1_set.intersection(range2)
    return len(intersect) > 0


# %%

counter = 0

with open('./2022/input_puzzle_4.txt', 'r') as fp:
    for line in fp:
        split_line = line.split(',')
        range_1_str = split_line[0].split('-')
        range_2_str = split_line[1].split('-')
        range_1 = range(int(range_1_str[0]), int(range_1_str[1]) + 1)
        range_2 = range(int(range_2_str[0]), int(range_2_str[1]) + 1)
        if range_subset(range_1, range_2) or range_subset(range_2, range_1):
            counter += 1

print(counter)

# %%

counter = 0

with open('./2022/input_puzzle_4.txt', 'r') as fp:
    for line in fp:
        split_line = line.split(',')
        range_1_str = split_line[0].split('-')
        range_2_str = split_line[1].split('-')
        range_1 = range(int(range_1_str[0]), int(range_1_str[1]) + 1)
        range_2 = range(int(range_2_str[0]), int(range_2_str[1]) + 1)
        if range_intersect(range_1, range_2):
            counter += 1

print(counter)
