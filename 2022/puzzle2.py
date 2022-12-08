# %%

# Rock    A, X
# Paper   B, Y
# Scissor C, Z
score = 0

with open("input_puzzle_2.txt", 'r') as fp:
    for line in fp:
        chars = line.split()
        if chars[1] == 'X':
            score += 1
            if chars[0] == 'A':
                score += 3
            if chars[0] == 'C':
                score += 6
        if chars[1] == 'Y':
            score += 2
            if chars[0] == 'B':
                score += 3
            if chars[0] == 'A':
                score += 6
        if chars[1] == 'Z':
            score += 3
            if chars[0] == 'C':
                score += 3
            if chars[0] == 'B':
                score += 6

print(score)

# %%
# Rock    A
# Paper   B
# Scissor C
# X lose
# Y draw
# Z win

score = 0

with open("input_puzzle_2.txt", 'r') as fp:
    for line in fp:
        chars = line.split()
        if chars[1] == 'X':
            if chars[0] == 'A':
                score += 3
            if chars[0] == 'B':
                score += 1
            if chars[0] == 'C':
                score += 2
        if chars[1] == 'Y':
            score += 3
            if chars[0] == 'A':
                score += 1
            if chars[0] == 'B':
                score += 2
            if chars[0] == 'C':
                score += 3
        if chars[1] == 'Z':
            score += 6
            if chars[0] == 'A':
                score += 2
            if chars[0] == 'B':
                score += 3
            if chars[0] == 'C':
                score += 1

print(score)

# %%


f = lambda x: ('  BXCYAZAXBYCZCXAYBZ'.index(x[0]+x[2]),
               '  BXCXAXAYBYCYCZAZBZ'.index(x[0]+x[2]))

print(*[
    sum(x)//2 for x in zip(
        *map(f, open('input_puzzle_2.txt'))
    )
])
