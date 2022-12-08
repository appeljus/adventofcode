# %%

char_prio = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
             'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
             't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28,
             'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37,
             'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46,
             'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}
#%%

sum_priorirty = 0
with open('input_puzzle_3.txt', 'r') as fp:
    for line in fp:
        line_length = len(line)
        first_half = line[:line_length // 2]
        second_half = line[line_length // 2:]
        common_char = [x for x in first_half if x in second_half][0]
        sum_priorirty += char_prio[common_char]

print(sum_priorirty)

# %%

sum_priorirty = 0
with open('input_puzzle_3.txt', 'r') as fp:
    lines = fp.readlines()
    for i in range(0, len(lines), 3):
        line_one = lines[i]
        line_two = lines[i + 1]
        line_three = lines[i + 2]
        common_char = [x for x in line_one if x in line_two and x in line_three][0]
        sum_priorirty += char_prio[common_char]

print(sum_priorirty)
