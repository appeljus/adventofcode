# %%

current_cycle = 1
register = 1
signal_strength = 0
cycle_of_interest = [20, 60, 100, 140, 180,  220]
register_values = []
with open('./2022/input_puzzle_10.txt', 'r') as fp:
    for line in fp:
        if line.startswith("noop"):
            if current_cycle in cycle_of_interest:
                signal_strength += current_cycle * register
            current_cycle += 1
            register_values.append(register)
        else:
            if current_cycle in cycle_of_interest:
                signal_strength += current_cycle * register
            elif current_cycle + 1 in cycle_of_interest:
                signal_strength += (current_cycle + 1) * register
            register_values.append(register)
            register_values.append(register)
            addx = line.split(" ")[1]
            register += int(addx)
            current_cycle += 2
print(signal_strength)

# %%
screen = ""
current_cycle = 0
register = 1
with open('./2022/input_puzzle_10.txt', 'r') as fp:
    for line in fp:
        # Start of cycle
        if line.startswith("noop"):
            # During cycle
            if abs((current_cycle % 40) - register) < 2:
                screen += "#"
            else:
                screen += "."
            # End of cycle
            current_cycle += 1
        else:
            # During cycle
            if abs((current_cycle % 40) - register) < 2:
                screen += "#"
            else:
                screen += "."
            current_cycle += 1
            if abs((current_cycle % 40) - register) < 2:
                screen += "#"
            else:
                screen += "."
            current_cycle += 1
            # End of cycle
            addx = line.split(" ")[1]
            register += int(addx)
result = ""
for i in range(len(screen)):
    if i % 40 == 0 and i != 0:
        print(result)
        result = ""
    result += screen[i]
print(result)
