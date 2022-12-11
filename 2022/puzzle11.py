# %%
import math
from typing import Callable


class Monkey:
    items: list[int]
    operation: Callable[[int], int]
    test: Callable[[int], int]
    inspection_count: int
    worry_level_drops: bool

    def __init__(
        self,
        starting_items: list[int],
        operation: Callable[[int], int],
        test: Callable[[int], int],
        worry_level_drops: bool,
    ):
        """
        :param starting_items: items the monkey starts with.
        :param operation: Operation performed when inspecting an item. For example: an operation could be new = old + 3, this means the worry level for that items is 3 higher than before inspecting.
        :param test: Test performed after inspection and after worry level drop to see to which monkey the item should be thrown.
        """
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.inspection_count = 0
        self.worry_level_drops = worry_level_drops

    def turn(self) -> dict[int, list[int]]:
        if not self.items:
            # No items in possession
            return {}
        else:
            result: dict[int, list[int]] = {}
            for item in self.items:
                worry_level = self.operation(item)
                self.inspection_count += 1
                if self.worry_level_drops:
                    worry_level = worry_level // 3
                monkey_id = self.test(worry_level)
                if monkey_id not in result:
                    result[monkey_id] = [worry_level]
                else:
                    result[monkey_id].append(worry_level)
            self.items = []
            return result

    def receive_items(self, items: list[int]):
        self.items.extend(items)

    def get_inspection_count(self):
        return self.inspection_count

    def __str__(self):
        return f"{self.items}, {self.operation}, {self.test}"


def play_round(monkeys: dict[int, Monkey]):
    for monkey in monkeys.values():
        turn_result = monkey.turn()
        if not turn_result:
            # No items
            pass
        else:
            # Distribute items
            for monkey_id, items in turn_result.items():
                monkeys[monkey_id].receive_items(items)


def create_operation_from_str(raw_operation: str) -> Callable[[int], int]:
    if "+" in raw_operation:
        if raw_operation.count("old") > 1:
            return lambda x: x + x
        else:
            return lambda x: x + int(raw_operation.split("+")[1].strip())
    elif "*" in raw_operation:
        if raw_operation.count("old") > 1:
            return lambda x: x * x
        else:
            return lambda x: x * int(raw_operation.split("*")[1].strip())


def create_test_from_str(raw_test_lines: list[str]) -> Callable[[int], int]:
    divisor = int(raw_test_lines[0].split()[-1])
    true_monkey_id = int(raw_test_lines[1].split()[-1])
    false_monkey_id = int(raw_test_lines[2].split()[-1])
    return lambda x: true_monkey_id if x % divisor == 0 else false_monkey_id


def calc_monkey_business(monkeys: dict[int, Monkey]) -> int:
    monkey_business = []
    for monkey in monkeys.values():
        monkey_business.append(monkey.get_inspection_count())
    return math.prod(sorted(monkey_business, reverse=True)[:2])


def parse_input(worry_level_drops: bool):
    result = {}
    with open('./2022/input_puzzle_11.txt', 'r') as fp:
        monkey_input = fp.read().split("\n\n")
        for raw_monkey_str in monkey_input:
            raw_monkey_str_lines = raw_monkey_str.split("\n")
            raw_monkey_id = int(raw_monkey_str_lines[0].split()[1].replace(":", ""))
            starting_items = [
                int(x.strip()) for x in raw_monkey_str_lines[1].split(":")[1].split(",")
            ]
            operation = create_operation_from_str(raw_monkey_str_lines[2].split(":")[1])
            test = create_test_from_str(raw_monkey_str_lines[3:])
            result[raw_monkey_id] = Monkey(starting_items, operation, test, worry_level_drops)
    return result


# %%
# Part 1
monkeys_by_id = parse_input(True)
for _ in range(20):
    play_round(monkeys_by_id)
print(calc_monkey_business(monkeys_by_id))

# %%
# Part 2
monkeys_by_id = parse_input(False)
for i in range(10000):
    print(i)
    play_round(monkeys_by_id)
    if i == 82:
        break
print(calc_monkey_business(monkeys_by_id))
