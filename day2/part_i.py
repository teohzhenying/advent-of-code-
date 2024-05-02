import csv


def divide_data_by_game_id():
    game_data = []
    all_data = ""
    game_dict = {}
    with open('gamecubes.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for r in row:
                all_data += r
                all_data += ','
            all_data += '\n'
    each_data = all_data.split('\n')
    for x in each_data:
        game_data.append(x.split(':'))
    for y in game_data:
        try:
            y[1] = y[1].split(';')
        except IndexError:
            continue
    for space in game_data:
        if space == ['']:
            game_data.remove(space)
    for x in game_data:
        for y in x:
            key = int(x[0][5:])
            game_dict[key] = y
    for key, val in game_dict.items():
        each_list = []
        for x in val:
            x = x.split(',')
            each_list.append(x)
        game_dict[key] = each_list

    final_dict = {}
    for key, value in game_dict.items():
        value_list = []
        for each_value in value:
            each_dict = {}
            for x in each_value:
                x_split = x.split(' ')
                for each_x_split in x_split:
                    if each_x_split == '':
                        x_split.remove(each_x_split)
                        try:
                            colour = x_split[1]
                            num = int(x_split[0])
                        except IndexError:
                            continue
                        if colour not in each_dict:
                            each_dict[colour] = int(num)
                        else:
                            each_dict[colour] += int(num)
            value_list.append(each_dict)
        final_dict[key] = value_list
    return final_dict


first_function = divide_data_by_game_id()
print(first_function)
