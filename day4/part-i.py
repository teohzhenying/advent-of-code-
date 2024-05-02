import pandas as pd
import re

scratch_cards = pd.read_csv('input.csv')

def split_cards(x):  # don't forget about the first row
    
    total = 0
    
    pattern = ":|\\|"  # get patterns of either : or |
    x_to_list = x.to_list()  # change to list
    for each_card in x_to_list:
        point_for_each_card = 0  # points for each card (the total) after matching winning card with elf's card
        each_card = re.split(pattern, each_card)  # split the card by the patterns above
        winning_cards = each_card[1].split(" ")  # winning card is the numbers after Card number : and before |
        winning_cards = [x for x in winning_cards if x != ''] # remove all whitespaces
        elfs_cards = each_card[2].split(" ")  # elf card is the numbers after |
        elfs_cards = [x for x in elfs_cards if x != ''] # remove all whitespaces
        for e in elfs_cards: # check which number (still in string format) in elf card matches in winning card
            if e in winning_cards:
                if point_for_each_card == 0: # each match is worth 1 for the first point
                    point_for_each_card += 1
                else: # and then, double the total points in the card if there is a match
                    point_for_each_card *= 2
        total += point_for_each_card
    
    return total

first_row = pd.DataFrame(["Card   1: 58 96 35 20 93 34 10 27 37 30 | 99 70 93 11 63 41 37 29  7 28 34 10 40 96 38 35 27 30 20 21  4 51 58 39 56"])  # the first row
first_row = first_row.apply(lambda x: print(split_cards(x)))

scratch_cards = scratch_cards.apply(lambda x: print(split_cards(x)))

print(22385 + 512)  # depends on output of print statement and scratch cards (I did it in Jupyter Notebook)
