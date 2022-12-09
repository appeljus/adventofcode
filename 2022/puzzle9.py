# %%

def touching(head_pos: tuple[int, int], tail_pos: tuple[int, int]) -> bool:
    if abs(head_pos[0]-tail_pos[0]) < 2 and abs(head_pos[1]-tail_pos[1]) < 2:
        return True
    else:
        return False


def move_head(head_pos: tuple[int, int], command: str) -> tuple[int, int]:
    if command == "R":
        return head_pos[0] + 1, head_pos[1]
    elif command == "L":
        return head_pos[0] - 1, head_pos[1]
    elif command == "U":
        return head_pos[0], head_pos[1] + 1
    elif command == "D":
        return head_pos[0], head_pos[1] - 1
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


head_position = 0, 0
tail_position = 0, 0
tail_visited = [tail_position]
with open('./2022/input_puzzle_9.txt', 'r') as fp:
    for line in fp:
        move_command = line[0]
        num_steps = line[2]
        for i in range(int(num_steps)):
            head_position = move_head(head_position, move_command)
            print(f"head position:\t{head_position}")
            if not touching(head_position, tail_position):
                tail_position = move_tail(head_position, tail_position)
                print(f"tail position:\t{tail_position}")
                tail_visited.append(tail_position)


print(len(set(tail_visited)))
