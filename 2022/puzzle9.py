# %%

def touching(head_pos: tuple[int, int], tail_pos: tuple[int, int]) -> bool:
    if abs(head_pos[0] - tail_pos[0]) < 2 and abs(head_pos[1] - tail_pos[1]) < 2:
        return True
    else:
        return False


def move_head(head_pos: tuple[int, int], command: str) -> tuple[int, int]:
    if command == "R":
        return (head_pos[0] + 1), head_pos[1]
    elif command == "L":
        return (head_pos[0] - 1), head_pos[1]
    elif command == "U":
        return head_pos[0], (head_pos[1] + 1)
    elif command == "D":
        return head_pos[0], (head_pos[1] - 1)
    else:
        print("UNKNOWN COMMAND")


def move_tail(head_pos: tuple[int, int], tail_pos: tuple[int, int]) -> tuple[int, int]:
    result = ()
    if head_pos[0] == tail_pos[0]:
        # move vertical
        if head_pos[1] > tail_pos[1]:
            result = (tail_pos[0], tail_pos[1] + 1)
        elif head_pos[1] < tail_pos[1]:
            result = (tail_pos[0], tail_pos[1] - 1)
        else:
            print("ERROR!")
    elif head_pos[1] == tail_pos[1]:
        # move horizontal
        if head_pos[0] < tail_pos[0]:
            result = (tail_pos[0] - 1, tail_pos[1])
        elif head_pos[0] > tail_pos[0]:
            result = (tail_pos[0] + 1, tail_pos[1])
        else:
            print("ERROR!")
    else:
        # move vertical
        if head_pos[0] < tail_pos[0] and head_pos[1] < tail_pos[1]:
            result = (tail_pos[0] - 1, tail_pos[1] - 1)
        elif head_pos[0] > tail_pos[0] and head_pos[1] < tail_pos[1]:
            result = (tail_pos[0] + 1, tail_pos[1] - 1)
        elif head_pos[0] > tail_pos[0] and head_pos[1] > tail_pos[1]:
            result = (tail_pos[0] + 1, tail_pos[1] + 1)
        elif head_pos[0] < tail_pos[0] and head_pos[1] > tail_pos[1]:
            result = (tail_pos[0] - 1, tail_pos[1] + 1)
        else:
            print("ERROR!")
    assert touching(result, tail_pos)
    return result


# %%
head_position = 0, 0
tail_position = 0, 0
tail_visited = [tail_position]
with open('./2022/input_puzzle_9.txt', 'r') as fp:
    for line in fp:
        move_command = line[0]
        num_steps = int(line[2:])
        for i in range(num_steps):
            head_position = move_head(head_position, move_command)
            if not touching(head_position, tail_position):
                tail_position = move_tail(head_position, tail_position)
                tail_visited.append(tail_position)

print(len(set(tail_visited)))

# %%

num_knots = 10
knot_positions = [(0, 0)] * num_knots
tail_visited = [knot_positions[-1]]
with open('./2022/input_puzzle_9.txt', 'r') as fp:
    for line in fp:
        move_command = line[0]
        num_steps = int(line[2:])
        for _ in range(num_steps):
            knot_positions[0] = move_head(knot_positions[0], move_command)
            for i in range(1, num_knots):
                previous_knot_position = knot_positions[i - 1]
                if not touching(previous_knot_position, knot_positions[i]):
                    knot_positions[i] = move_tail(previous_knot_position, knot_positions[i])
                    if i == (num_knots - 1):
                        print(f"tail position: {knot_positions[i]}")
                        tail_visited.append(knot_positions[i])
print(len(set(tail_visited)))
