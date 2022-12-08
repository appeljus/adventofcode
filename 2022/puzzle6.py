# %%

with open('input_puzzle_6.txt', 'r') as fp:
    char_list = list(fp.readline())
    for i in range(0, len(char_list)):
        if len(char_list[i:i+4]) == len(set(char_list[i:i+4])):
            print(i+4)
            break

# %%
with open('input_puzzle_6.txt', 'r') as fp:
    char_list = list(fp.readline())
    for i in range(0, len(char_list)):
        if len(char_list[i:i + 14]) == len(set(char_list[i:i + 14])):
            print(i + 14)
            break
