import csv
from pprint import pprint


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
                each_adjacency = [separated_list[first_idx - 1][second_idx - 1],
                                  separated_list[first_idx - 1][second_idx],
                                  separated_list[first_idx - 1][second_idx + 1],
                                  separated_list[first_idx][second_idx - 1],
                                  separated_list[first_idx][second_idx + 1],
                                  separated_list[first_idx + 1][second_idx - 1],
                                  separated_list[first_idx + 1][second_idx],
                                  separated_list[first_idx + 1][second_idx + 1]]

            if int(first_idx) == 0 and int(second_idx) == 0:
                each_adjacency = [separated_list[first_idx][second_idx + 1],
                                  separated_list[first_idx + 1][second_idx],
                                  separated_list[first_idx + 1][second_idx + 1]]

            if int(first_idx) == 0 and 0 < int(second_idx) < len(separated_list[first_idx]) - 1:
                each_adjacency = [separated_list[first_idx][second_idx - 1],
                                  separated_list[first_idx][second_idx + 1],
                                  separated_list[first_idx + 1][second_idx - 1],
                                  separated_list[first_idx + 1][second_idx],
                                  separated_list[first_idx + 1][second_idx + 1]]

            if 0 < int(first_idx) < len(separated_list[first_idx]) - 1 and int(second_idx) == 0:
                each_adjacency = [separated_list[first_idx - 1][second_idx],
                                  separated_list[first_idx - 1][second_idx + 1],
                                  separated_list[first_idx][second_idx + 1],
                                  separated_list[first_idx + 1][second_idx],
                                  separated_list[first_idx + 1][second_idx + 1]]

            if int(first_idx) == len(separated_list[first_idx]) - 1 and 0 < int(second_idx) < len(
                    separated_list[first_idx]) - 1:
                each_adjacency = [separated_list[first_idx - 1][second_idx - 1],
                                  separated_list[first_idx - 1][second_idx],
                                  separated_list[first_idx - 1][second_idx + 1],
                                  separated_list[first_idx][second_idx - 1],
                                  separated_list[first_idx][second_idx + 1]]

            if int(first_idx) == 0 and int(second_idx) == len(separated_list[first_idx]) - 1:
                each_adjacency = [separated_list[first_idx][second_idx - 1],
                                  separated_list[first_idx + 1][second_idx - 1],
                                  separated_list[first_idx + 1][second_idx]]

            if int(first_idx) == len(separated_list[first_idx]) - 1 and int(second_idx) == 0:
                each_adjacency = [separated_list[first_idx - 1][second_idx],
                                  separated_list[first_idx - 1][second_idx + 1],
                                  separated_list[first_idx][second_idx + 1]]

            if int(first_idx) == len(separated_list[first_idx]) - 1 and int(second_idx) == len(
                    separated_list[first_idx]) - 1:
                each_adjacency = [separated_list[first_idx - 1][second_idx - 1],
                                  separated_list[first_idx - 1][second_idx],
                                  separated_list[first_idx][second_idx - 1]]

            if 0 < int(first_idx) < len(separated_list[first_idx]) - 1 and int(second_idx) == len(
                    separated_list[first_idx]) - 1:
                each_adjacency = [separated_list[first_idx - 1][second_idx - 1],
                                  separated_list[first_idx - 1][second_idx],
                                  separated_list[first_idx][second_idx - 1],
                                  separated_list[first_idx + 1][second_idx - 1],
                                  separated_list[first_idx + 1][second_idx]]

            if each_adjacency:
                all_adjacency.append(each_adjacency)

        final_adjacency.append([num, all_adjacency])

    return final_adjacency


adj_function = adjacency()


# print(adj_function)

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

print(symbols_list)


def flatten_array():
    new_adj_list = []
    for x in adj_function:
        nums = x[0]
        list_of_index = x[1]
        each_list = []
        for y in list_of_index:
            for z in y:
                each_list.append(z)
        new_adj_list.append([nums, each_list])
    return new_adj_list


flattened_adj = flatten_array()


def sum_of_part_of_nums():
    part_of_nums = []
    for x in flattened_adj:
        num = x[0]
        index_list = x[1]
        for i in index_list:
            if i in symbols_list:
                part_of_nums.append(int(num))
                break
    return sum(part_of_nums)


print(sum_of_part_of_nums())  # 532445
