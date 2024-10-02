#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import os

def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def add_cards(p_d_cards, pack):
    random_index = random.randint(0, len(pack) - 1)
    p_d_cards.append(pack[random_index])
    del pack[random_index]

def value_of_cards(p_d_cards):
    card_value = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
    sum_card = 0
        
    for item in p_d_cards:
        sum_card = sum_card + card_value[item]

    count_of_a = p_d_cards.count('A')

    if (count_of_a == 0):
        return sum_card
    else:
        if (sum_card + 10 <= 21):
            return sum_card + 10
        else:
            return sum_card

player_name = input("Enter your name: ")
clear_output()
player_interested = 'y'
while (player_interested == 'y'):
    card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    pack = 4 * card
    player_cards = []
    dealer_cards = []
    player_new_card = 'y'
    
    add_cards (player_cards, pack)
    add_cards (player_cards, pack)
    add_cards (dealer_cards, pack)
    add_cards (dealer_cards, pack)
    
    player_card_value = value_of_cards(player_cards)
    dealer_card_value = value_of_cards(dealer_cards)
    
    #print(f"Your cards: {player_cards[0]}, {player_cards[1]}. Value is {player_card_value}")
    print(f"Dealer cards: {dealer_cards[0]}, HIDDEN")    
    print(f"{player_name}'s cards: {player_cards}, Total: {player_card_value}")
    print()

    if (player_card_value == 21):
        print ("Player WON!")
    else:
        while (player_new_card == 'y'):
            player_new_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if (player_new_card == 'y'):
                add_cards (player_cards, pack)
                player_card_value = value_of_cards(player_cards)
                print(f"{player_name}'s cards: {player_cards}. Value is {player_card_value}")
        
                if (player_card_value > 21):
                    break
    
        print()
        if (player_card_value > 21):
            print ("Dealer WON!")
        else:
            while (dealer_card_value < 17):
                add_cards (dealer_cards, pack)
                dealer_card_value = value_of_cards(dealer_cards)
        
            if (dealer_card_value > 21):
                print (f"{player_name} WON!")
            elif (dealer_card_value > player_card_value):
                print ("Dealer WON!")
            elif (player_card_value > dealer_card_value):
                print (f"{player_name} WON!")
            elif (player_card_value == dealer_card_value):    
                print ("It's a TIE!")
    
        print()
        print (f"Dealer: {dealer_card_value} -- {dealer_cards}")
        print (f"{player_name}: {player_card_value}  --  {player_cards}")
        
    print()
    player_interested = input(f"Another game, {player_name}? 'y'-yes, 'n'-no: ")
    clear_output()


# In[ ]:




