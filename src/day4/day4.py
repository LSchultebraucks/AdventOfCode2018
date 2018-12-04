from collections import defaultdict


def main():
    guard_sleep_dict = calculate_guard_sleep_dict()
    part_one(guard_sleep_dict)
    part_two(guard_sleep_dict)


def calculate_guard_sleep_dict():
    with open('input.txt', 'r') as data:

        sorted_data = sorted(data)  # This will work too... No extra key required

        guard_sleep_dict = defaultdict(lambda: [0 for x in range(60)])
        current_guard = -1
        start_sleeping = -1
        for line in sorted_data:
            if line[25] == "#":
                current_guard = line.split()[3]
            elif line[25] == "a":
                start_sleeping = int(line[15:17])
            else:  # "wakes up"
                end_sleeping = int(line[15:17])
                for x in range(start_sleeping, end_sleeping):
                    guard_sleep_dict[current_guard][x] += 1

    return guard_sleep_dict


def part_one(guard_sleep_dict):
    guard = sorted(guard_sleep_dict.keys(), key=lambda g: -sum(guard_sleep_dict[g]))[0]

    gh = guard_sleep_dict[guard]
    minute = gh.index(max(gh))
    print int(guard[1:]) * minute


def part_two(guard_sleep_dict):
    guard = sorted(guard_sleep_dict.keys(), key=lambda g: -max(guard_sleep_dict[g]))[0]
    gh = guard_sleep_dict[guard]
    minute = gh.index(max(gh))
    print int(guard[1:]) * minute


if __name__ == '__main__':
    main()
