def main():
    polymer = parse_input()
    print(part_one(polymer))
    part_two(polymer)


def parse_input():
    polymer = ''
    with open('input.txt', 'r') as data:
        for line in data:
            polymer += line.strip()

    return polymer


def part_one(polymer):
    stack = []
    for potential_reacting_char in polymer:
        tail_char = None
        if len(stack) > 0:
            tail_char = stack[-1]
        if potential_reacting_char != tail_char and (
                tail_char == potential_reacting_char.upper() or tail_char == potential_reacting_char.lower()):
            stack.pop()
        else:
            stack.append(potential_reacting_char)
    return len(stack)


def part_two(polymer):
    pass


if __name__ == '__main__':
    main()
