from collections import defaultdict


def main():
    part_one()
    part_two()


def part_one():
    current_frequency = 0

    input_file = open('input.txt', 'r')

    for current_line in input_file:
        frequency = int(current_line)
        current_frequency += frequency

    input_file.close()

    print 'Resulting Frequency is ' + str(current_frequency)


def part_two():
    current_frequency = 0

    past_frequencies_dic = defaultdict(bool)

    past_frequencies_dic[0] = True

    with open('input.txt', 'r') as input_file:
        lines = [int(line) for line in input_file]

    frequency_twice_not_found = True

    while frequency_twice_not_found:
        for current_line in lines:
            frequency = int(current_line)
            current_frequency += frequency
            if past_frequencies_dic[current_frequency]:
                print str(current_frequency) + ' appeared twice'
                frequency_twice_not_found = False
                break
            else:
                past_frequencies_dic[current_frequency] = True


if __name__ == '__main__':
    main()
