import csv
from pprint import pprint

import numpy


# separate csv into a list of lists (rows and columns)
def separate_into_lists():
    all_list = []
    with open('engine-schematic.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            each_row_list = []
            each_row = row[0]
            for each_value in each_row:
                each_row_list.append(each_value)
            all_list.append(each_row_list)

    return all_list


separated_list = separate_into_lists()


# print(separate_into_lists())


# find all the unique symbols (not '.' and numbers)
def find_all_symbols():
    all_symbols = []
    for row_idx in range(len(separated_list)):
        for column_idx in range(len(separated_list[row_idx])):
            try:
                if int(separated_list[row_idx][column_idx]):
                    continue
            except ValueError:
                if separated_list[row_idx][column_idx] != '.':
                    if separated_list[row_idx][column_idx] not in all_symbols:
                        all_symbols.append(separated_list[row_idx][column_idx])
    return all_symbols


symbols_list = find_all_symbols()


# print(symbols_list)


# get a list of all the numbers
def find_index_and_numbers():
    curr_num = ""
    all_curr_num = []
    indexes = []
    for row_idx in range(len(separated_list)):
        for column_idx in range(len(separated_list[row_idx])):
            try:
                first_idx = row_idx
                second_idx = column_idx
                if int(separated_list[first_idx][second_idx]) or separated_list[first_idx][second_idx] == '0':
                    # print(separated_list[first_idx][second_idx])
                    curr_num += separated_list[first_idx][second_idx]
                    indexes.append([first_idx, second_idx])
            except ValueError:
                if curr_num != '':
                    all_curr_num.append([curr_num, indexes])
                    indexes = []
                curr_num = ""
                continue
    return all_curr_num


all_numbers = find_index_and_numbers()


# pprint(all_numbers)


# get a lost of all the adjacent indexes of the numbers
def adjacency():
    each_adjacency = None
    final_adjacency = []

    for a in all_numbers:
        all_adjacency = []
        num = a[0]
        list_of_indexes = a[1]

        for l in list_of_indexes:
            first_idx = l[0]
            second_idx = l[1]

            if 0 < int(first_idx) < len(separated_list[first_idx]) - 1 and 0 < int(second_idx) < len(
                    separated_list[first_idx]) - 1:
                each_adjacency = [[first_idx - 1, second_idx - 1],
                                  [first_idx - 1, second_idx],
                                  [first_idx - 1, second_idx + 1],
                                  [first_idx, second_idx - 1],
                                  [first_idx, second_idx + 1],
                                  [first_idx + 1, second_idx - 1],
                                  [first_idx + 1, second_idx],
                                  [first_idx + 1, second_idx + 1]]

            if int(first_idx) == 0 and int(second_idx) == 0:
                each_adjacency = [[first_idx, second_idx + 1],
                                  [first_idx + 1, second_idx],
                                  [first_idx + 1, second_idx + 1]]

            if int(first_idx) == 0 and 0 < int(second_idx) < len(separated_list[first_idx]) - 1:
                each_adjacency = [[first_idx, second_idx - 1],
                                  [first_idx, second_idx + 1],
                                  [first_idx + 1, second_idx - 1],
                                  [first_idx + 1, second_idx],
                                  [first_idx + 1, second_idx + 1]]

            if 0 < int(first_idx) < len(separated_list[first_idx]) - 1 and int(second_idx) == 0:
                each_adjacency = [[first_idx - 1, second_idx],
                                  [first_idx - 1, second_idx + 1],
                                  [first_idx, second_idx + 1],
                                  [first_idx + 1, second_idx],
                                  [first_idx + 1, second_idx + 1]]

            if int(first_idx) == len(separated_list[first_idx]) - 1 and 0 < int(second_idx) < len(
                    separated_list[first_idx]) - 1:
                each_adjacency = [[first_idx - 1, second_idx - 1],
                                  [first_idx - 1, second_idx],
                                  [first_idx - 1, second_idx + 1],
                                  [first_idx, second_idx - 1],
                                  [first_idx, second_idx + 1]]

            if int(first_idx) == 0 and int(second_idx) == len(separated_list[first_idx]) - 1:
                each_adjacency = [[first_idx, second_idx - 1],
                                  [first_idx + 1, second_idx - 1],
                                  [first_idx + 1, second_idx]]

            if int(first_idx) == len(separated_list[first_idx]) - 1 and int(second_idx) == 0:
                each_adjacency = [[first_idx - 1, second_idx],
                                  [first_idx - 1, second_idx + 1],
                                  [first_idx, second_idx + 1]]

            if int(first_idx) == len(separated_list[first_idx]) - 1 and int(second_idx) == len(
                    separated_list[first_idx]) - 1:
                each_adjacency = [[first_idx - 1, second_idx - 1],
                                  [first_idx - 1, second_idx],
                                  [first_idx, second_idx - 1]]

            if 0 < int(first_idx) < len(separated_list[first_idx]) - 1 and int(second_idx) == len(
                    separated_list[first_idx]) - 1:
                each_adjacency = [[first_idx - 1, second_idx - 1],
                                  [first_idx - 1, second_idx],
                                  [first_idx, second_idx - 1],
                                  [first_idx + 1, second_idx - 1],
                                  [first_idx + 1, second_idx]]

            if each_adjacency:
                all_adjacency.append(each_adjacency)

        final_adjacency.append([num, all_adjacency])

    return final_adjacency


adj_function = adjacency()


# print(adj_function)


# make the lists of adjacent indexes into 1 list
def flatten_list():
    adj_list = []
    for x in adj_function:
        num = x[0]
        list_of_index = x[1]
        each_list = []
        for idx in range(len(list_of_index)):
            for each_idx in range(len(list_of_index[idx])):
                row_idx = list_of_index[idx][each_idx][0]
                column_idx = list_of_index[idx][each_idx][1]
                if separated_list[row_idx][column_idx] == '*':
                    if list_of_index[idx][each_idx] not in each_list:
                        each_list.append(list_of_index[idx][each_idx])
        adj_list.append([num, each_list])
    return adj_list


flattened_asterisk = flatten_list()


# print(flattened_asterisk)


# returns a list of only indexes which are asterisks
def asterisk_only():
    all_asterisks = []
    for x in flattened_asterisk:
        num = x[0]
        list_of_index = x[1]
        if len(list_of_index) == 0:
            continue
        else:
            for l in list_of_index:
                all_asterisks.append([num, (l[0], l[1])])
    return all_asterisks


all_asterisks = asterisk_only()


# get a dict where the key is a tuple of the index of the asterisk and the value is an array of
# the numbers adjacent to it
def gear():
    dict = {}
    for a in all_asterisks:
        num = a[0]
        asterisks_tuple = a[1]
        try:
            if dict[asterisks_tuple]:
                dict[asterisks_tuple].append(num)
        except KeyError:
            dict[asterisks_tuple] = [num]
    return dict


gear_dict = gear()
print(gear_dict)


def gear_ratio():
    final_list = []
    multiplied_list = []
    for k, v in gear_dict.items():
        each_list = []
        if len(v) > 1:
            for n in v:
                each_list.append(int(n))
        else:
            continue
        final_list.append(each_list)
    print(final_list)

    for z in final_list:
        multiplied_list.append(numpy.prod(z))

    print(sum(multiplied_list))


print(gear_ratio())
