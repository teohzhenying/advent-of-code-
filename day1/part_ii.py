import csv


def calibration_values():
    num_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
                'seven': 7, 'eight': 8, 'nine': 9}
    all_numbers = []
    with open('calibration_vals.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            each_number = []
            for each_value in row:
                for each_digit_index in range(len(each_value)):
                    try:
                        if int(each_value[each_digit_index]):
                            # print(each_digit_index)
                            each_number.append(each_value[each_digit_index])
                    except ValueError:
                        # if type(each_value[each_digit_index]) is str:
                        first_letter = each_value[each_digit_index]
                        for key, value in num_dict.items():
                            if key[0] == first_letter:
                                length = len(key) + each_digit_index
                                if each_value[each_digit_index:length] == key:
                                    each_number.append(value)
                                    break  # no need to pop??
                all_numbers.append(each_number)
    # print(all_numbers)
    return all_numbers


def find_sum(list_of_lists):
    final_sum = 0
    for list in list_of_lists:
        if len(list) > 0:
            first_num = str(list[0])
            last_num = str(list[-1])
            num = first_num + last_num
            final_sum += int(num)
        elif len(list) == 0:
            first_num = str(list[0])
            num = first_num + first_num
            final_sum += int(num)

    return final_sum


list_given = calibration_values()
print(find_sum(list_given))
