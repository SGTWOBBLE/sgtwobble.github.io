# Lab_09 Blackjack Advice

# dict for card values
card_values = {
'a': 1,
'2': 2,
'3': 3,
'4': 4,
'5': 5,
'6': 6,
'7': 7,
'8': 8,
'9': 9,
'10': 10,
'j': 11,
'q': 12,
'k': 13
}

# input converted to a string
first_card = input(str('"j" for Jack, "q" for Queen, "k" for king, "a" for Ace lower-case only or "1-10"\nWhat\'s your first card:? '))

second_card = input(str('"j" for Jack, "q" for Queen, "k" for king, "a" for Ace lower-case only or "1-10"\nWhat\'s your second card:? '))

third_card = input(str('"j" for Jack, "q" for Queen, "k" for king, "a" for Ace lower-case only or "1-10"\nWhat\'s your third card:? '))

# inputs for draw take the key and assigns an int type 
first_draw = card_values[first_card]

second_draw = card_values[second_card]

third_draw = card_values[third_card]

# total of 3 draws
total_draw = first_draw + second_draw + third_draw

# while loop breaking if boolean is True
while True:
    if total_draw < 17:
        print(f'{total_draw} "Hit"')
        break
    if total_draw > 17 and total_draw < 21:
        print(f'{total_draw} "Stay"')
        break
    if total_draw == 21:
        print(f'{total_draw} "Blackjack!"')
    elif total_draw > 21:
        print(f'{total_draw} "Already Busted"')
        break
    

"""
Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
"""

