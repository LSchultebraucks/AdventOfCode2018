from collections import defaultdict
from difflib import SequenceMatcher

from operator import itemgetter


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def main():
    part_one()
    part_two()


def part_one():
    with open('input.txt', 'r') as input_file:
        lines = [line for line in input_file]

    word_twice_count = 0
    word_three_times_count = 0

    for line in lines:
        word_count_dic = defaultdict(int)
        has_char_twice = False
        has_char_three_times = False
        for char in line:
            word_count_dic[char] += 1
        for key in word_count_dic.keys():
            if word_count_dic[key] == 2:
                has_char_twice = True
            elif word_count_dic[key] == 3:
                has_char_three_times = True

        if has_char_twice:
            word_twice_count += 1
        if has_char_three_times:
            word_three_times_count += 1

    checksum = word_twice_count * word_three_times_count

    print 'checksum is ' + str(checksum)


def part_two():
    with open('input.txt', 'r') as input_file:
        lines = [line for line in input_file]

    similarity_strings = [(line, comparing_line, similar(line, comparing_line))
                          for line in lines for comparing_line in lines
                          if line is not comparing_line]

    most_similair_strings = max(similarity_strings, key=itemgetter(2))

    result_word = ''.join([char_word_one
                           for char_word_one, char_word_two in zip(most_similair_strings[0], most_similair_strings[1])
                           if char_word_one == char_word_two])

    print result_word


if __name__ == '__main__':
    main()
