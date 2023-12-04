import copy


def read_input(input: str):
    with open(input) as f:
        lines = f.read().split("  ")
    return lines


class Monkey:
    def __init__(self, id: int, items: list, operation_type: str, factor_summand: int,
                 div: int, throw_true: int, throw_false: int):
        self.id = id
        self.items = items
        self.operation_type = operation_type
        self.factor_summand = factor_summand
        self.div = div
        self.throw_true = throw_true
        self.throw_false = throw_false
        self.inspections = 0

    def __str__(self):
        return str(self.id) + ": " + str(self.inspections) + " " + str(self.items)

    def inspect(self):
        for i in range(len(self.items)):
            self.inspections += 1
            if self.operation_type == "add":
                self.items[i] = (self.items[i] + self.factor_summand) // 3
            if self.operation_type == "mult":
                self.items[i] = (self.items[i] * self.factor_summand) // 3
            if self.operation_type == "square":
                self.items[i] = (self.items[i] * self.items[i]) // 3

    def test(self, monkeys: list):
        for item in self.items.copy():
            if item % self.div == 0:
                monkeys[self.throw_true].items.append(item)
            else:
                monkeys[self.throw_false].items.append(item)
            self.items.remove(item)

    def inspect_no_division(self, divisors: list):
        for i in range(len(self.items)):
            self.inspections += 1
            if self.operation_type == "add":
                self.items[i] = self.replace_with_congruent(self.items[i] + self.factor_summand, divisors)
            if self.operation_type == "mult":
                self.items[i] = self.replace_with_congruent(self.items[i] * self.factor_summand, divisors)
            if self.operation_type == "square":
                self.items[i] = self.replace_with_congruent(self.items[i] * self.items[i], divisors)

    def replace_with_congruent(self, n: int, divisors: list):
        prod = 1
        for div in divisors:
            prod *= div

        return n % prod


if __name__ == '__main__':
    monkeys_input = [Monkey(0, [89, 74], "mult", 5, 17, 4, 7),
                     Monkey(1, [75, 69, 87, 57, 84, 90, 66, 50], "add", 3, 7, 3, 2),
                     Monkey(2, [55], "add", 7, 13, 0, 7),
                     Monkey(3, [69, 82, 69, 56, 68], "add", 5, 2, 0, 2),
                     Monkey(4, [72, 97, 50], "add", 2, 19, 6, 5),
                     Monkey(5, [90, 84, 56, 92, 91, 91], "mult", 19, 3, 6, 1),
                     Monkey(6, [63, 93, 55, 53], "square", -1, 5, 3, 1),
                     Monkey(7, [50, 61, 52, 58, 86, 68, 97], "add", 4, 11, 5, 4)]
    divisors = [17, 7, 13, 2, 19, 3, 5, 11]

    monkeys_test_input = [Monkey(0, [79, 98], "mult", 19, 23, 2, 3),
                          Monkey(1, [54, 65, 75, 74], "add", 6, 19, 2, 0),
                          Monkey(2, [79, 60, 97], "square", -1, 13, 1, 3),
                          Monkey(3, [74], "add", 3, 17, 0, 1)]
    divisors_test = [23, 19, 13, 17]

    rounds = 20

    monkeys_test = copy.deepcopy(monkeys_test_input)
    for round in range(rounds):
        for monkey in monkeys_test:
            monkey.inspect()
            monkey.test(monkeys_test)
    inspections = [monkey.inspections for monkey in monkeys_test]
    inspections.sort(reverse=True)
    print("test1:", inspections[0] * inspections[1])

    monkeys = copy.deepcopy(monkeys_input)
    for round in range(rounds):
        for monkey in monkeys:
            monkey.inspect()
            monkey.test(monkeys)
    inspections = [monkey.inspections for monkey in monkeys]
    inspections.sort(reverse=True)
    print("task1:", inspections[0] * inspections[1])

    rounds = 10000

    monkeys_test = copy.deepcopy(monkeys_test_input)
    for round in range(rounds):
        for monkey in monkeys_test:
            monkey.inspect_no_division(divisors_test)
            monkey.test(monkeys_test)
    inspections = [monkey.inspections for monkey in monkeys_test]
    inspections.sort(reverse=True)
    print("test2:", inspections[0] * inspections[1])

    monkeys = copy.deepcopy(monkeys_input)
    for round in range(rounds):
        for monkey in monkeys:
            monkey.inspect_no_division(divisors)
            monkey.test(monkeys)
    inspections = [monkey.inspections for monkey in monkeys]
    inspections.sort(reverse=True)
    print("task2:", inspections[0] * inspections[1])
