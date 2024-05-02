import csv


def sum_of_calibration_values():
    all_numbers = []
    final_sequence = []
    with open('calibration_vals.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            number = ''
            for each_value in row:
                # print(each_value)
                for x in each_value:
                    # print(x)
                    try:
                        if int(x):
                            number += x
                            # print(number)
                    except ValueError:
                        continue
                all_numbers.append(number)
    # print(all_numbers)
    for each_number in all_numbers:
        if len(each_number) > 1:
            first_num = each_number[0]
            second_num = each_number[-1]
            num = first_num + second_num
            final_sequence.append(int(num))
        elif len(each_number) == 1:
            first_num = each_number[0]
            num = first_num + first_num
            final_sequence.append(int(num))
    print(sum(final_sequence))

sum_of_calibration_values()
