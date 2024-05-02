import pandas as pd
import re

scratch_cards = pd.read_csv('input.csv', header=None)

def split_cards(x):  

    each_card_dict = {}

    pattern = ":|\\|"  # get patterns of either : or |
    x_to_list = x.to_list()  # change to list
    for each_card in x_to_list:
        each_card = re.split(pattern, each_card)  # split the card by the patterns above
        winning_cards = each_card[1].split(" ")  # winning card is the numbers after Card number : and before |
        winning_cards = [x for x in winning_cards if x != ''] # remove all whitespaces
        elfs_cards = each_card[2].split(" ")  # elf card is the numbers after |
        elfs_cards = [x for x in elfs_cards if x != ''] # remove all whitespaces
        title_card = int(each_card[0].split(" ")[-1])
        for e in elfs_cards: # check which number (still in string format) in elf card matches in winning card
            if e in winning_cards:
                try:
                    if each_card_dict[title_card]:
                        each_card_dict[title_card].append(e)
                except KeyError:
                    each_card_dict[title_card] = [e]
    
    # if there is no winning card but card is still available, add them to each_card_dict
    for x in range(1, len(scratch_cards) + 1):
        if x not in each_card_dict.keys():
            each_card_dict[x] = []
            
    original_and_accumulative = {key: [] for key in range(1, len(each_card_dict) + 1)}
    print("each card dict {card number: winning matches made}: ", each_card_dict)
    
    number_of_matches = {}
    for key, value in each_card_dict.items():
        number_of_matches[key] = len(value)
        
    # add original cards first: if the number is not zero. then, if it's number_of_matches[num] is more than 1, append the card for x in range(number_of_matches[num]) to the following lists of each number in original cards. repeat this process to the next original cards
    print("number of matches {card number: number of winning matches}: ", number_of_matches)
    print("original and accumulative (final dict to get all cards - before appending the cards): ", original_and_accumulative)
    
    # append 1 original card to each value in original and accumulative
    for card, matches in original_and_accumulative.items():
        original_and_accumulative[card].append(card)
            
    # get accumulative cards for each value
    def check_accumulative_cards(key_given):
        current_element = original_and_accumulative[key_given]
        access_matches = number_of_matches[key_given]
        all_additional_cards = []
        for ce in range(len(current_element)):  # [2, 2] --> [3, 4, 3, 4]
            for y in range(access_matches):
                all_additional_cards.append(current_element[ce] + y + 1)
        print(all_additional_cards)
        for z in all_additional_cards:
            original_and_accumulative[z].append(z)
    
    # loop through entire original_and_accumulative dict to get the won cards using check_accumulative_cards()
    for k_idx, v_idx in original_and_accumulative.items():
        check_accumulative_cards(k_idx)
    
    # add up the total number of cards
    total_length = 0
    for key_of_final, value_of_final in original_and_accumulative.items():
        total_length += len(value_of_final)
        
    return total_length

scratch_cards = scratch_cards.apply(lambda x: print(split_cards(x)))
