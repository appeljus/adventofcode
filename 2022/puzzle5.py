# %%

class Stack:
    content: list[str]
    identifier: int

    def __init__(self, identifier):
        self.identifier = identifier
        self.content = []

    def __str__(self) -> str:
        return str(self.content)

    def __repr__(self) -> str:
        return str(self.content)

    def pop(self) -> str:
        if len(self.content) < 1:
            raise Exception("No crates left!")
        top_crate = self.content[-1]
        self.content = self.content[:-1]
        return top_crate

    def stash(self, char: str) -> None:
        self.content.append(char)

    def grab(self, nr_of_crates: int) -> list[str]:
        if len(self.content) < nr_of_crates:
            raise Exception("No crates left!")
        top_crates = self.content[-nr_of_crates:]
        self.content = self.content[:-nr_of_crates]
        return top_crates

    def store(self, crates: list):
        self.content.extend(crates)

    def get_content(self) -> list[str]:
        return self.content


def rearrange_9000(from_stack: Stack, to_stack: Stack, nr_of_crates: int):
    for i in range(nr_of_crates):
        to_stack.stash(from_stack.pop())


def rearrange_9001(from_stack: Stack, to_stack: Stack, nr_of_crates: int):
    to_stack.store(from_stack.grab(nr_of_crates))


def get_stack_by_id_dict():
    result: dict[int, Stack] = {}
    char_matrix: list[list[str]] = []
    with open('./2022/input_puzzle_5.txt', 'r') as fp:
        for line in fp:
            if line.startswith("move"):
                break
            char_matrix.append(list(line))
    char_matrix = char_matrix[:-1]
    ids = char_matrix[-1]

    for i in range(len(ids)):
        if ids[i] != " " and ids[i] != "\n":
            new_stack = Stack(int(ids[i]))
            for j in range(len(char_matrix) - 2, -1, -1):
                try:
                    crate = char_matrix[j][i]
                    if crate == " ":
                        continue
                    else:
                        new_stack.stash(char_matrix[j][i])
                except IndexError:
                    pass
            result[int(ids[i])] = new_stack

    return result


# %%
stacks_by_id = get_stack_by_id_dict()
with open('./2022/input_puzzle_5.txt', 'r') as fp:
    for line in fp:
        if line.startswith("move"):
            split_line = line.split(" ")
            rearrange_9000(
                stacks_by_id[int(split_line[3])],
                stacks_by_id[int(split_line[5])],
                int(split_line[1]),
            )
result_string = []
for stack in stacks_by_id.values():
    result_string.append(stack.get_content()[-1])
print("".join(result_string))

# %%
stacks_by_id = get_stack_by_id_dict()
with open('./2022/input_puzzle_5.txt', 'r') as fp:
    for line in fp:
        if line.startswith("move"):
            split_line = line.split(" ")
            rearrange_9001(
                stacks_by_id[int(split_line[3])],
                stacks_by_id[int(split_line[5])],
                int(split_line[1]),
            )
result_string = []
for stack in stacks_by_id.values():
    result_string.append(stack.get_content()[-1])
print("".join(result_string))
