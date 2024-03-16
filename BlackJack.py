# Defining the logo as a multi-line string representing a decorative text.
logo = '''
 ____  _            _       _            _    
| __ )| | __ _  ___| | __  | | __ _  ___| | __
|  _ \| |/ _` |/ __| |/ /  | |/ _` |/ __| |/ /
| |_) | | (_| | (__|   < |_| | (_| | (__|   < 
|____/|_|\__,_|\___|_|\_\___/ \__,_|\___|_|\_\

'''
# Printing the logo.
print(logo)

# Importing the random module.
import random

# Defining the list of cards.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Selecting two random cards for the player and the dealer.
player_cards = random.sample(cards, 2)
dealer_cards = random.sample(cards, 2)

# Defining a function to print a list of items separated by commas.
def printer(print_item):
    return ', '.join(map(str, print_item))

# Displaying the player's cards and the dealer's face-up card.
print(f"This is your cards - {printer(player_cards)}")
print(f"This is dealers card - {dealer_cards[0]}\n")

# Calculating the total value of the player's cards.
def player_card_total():
    player_card_count = 0
    for card in player_cards:
        player_card_count += card
    return player_card_count

player_card_total()

# Calculating the total value of the dealer's cards.
def dealer_card_total():
    dealer_card_count = 0
    for card in dealer_cards:
        dealer_card_count += card
    return dealer_card_count

dealer_card_total()

# Checking if any of the players have a blackjack (total of 21).
def blackjack(_cards_):
    card_count = 0
    for number in _cards_:
      card_count+=number
    if card_count > 21:
        for number in player_cards:
            if number == 11:
                number = 1
                print(number)

# Asking the player if they want a third card.
third_card = input("Do you want third card Y or N: ").lower()

# If the player wants a third card:
if third_card == "y":
    # Adding a random card to the player's hand.
    player_cards.append(random.choice(cards))
    # Displaying the final hands of both the player and the dealer.
    print(f"\nYour final cards are - {printer(player_cards)}")
    print(f"Dealers final cards are - {printer(dealer_cards)}")
    # Checking for blackjack for both player and dealer.
    blackjack(player_cards)
    blackjack(dealer_cards)
    player_card_total()
    # Determining the outcome of the game based on card totals.
    if player_card_total() > 21:
        print("\nYou lose")
    else:
        dealer_card_count = 0
        for card in dealer_cards:
            dealer_card_count += card
        player_card_total()
        if player_card_total() > dealer_card_count:
            print("\nYou win")
        else:
            print("\nDealer wins")

# If the player doesn't want a third card:
elif third_card == "n":
    # Checking if the dealer needs to draw another card (if their total is less than 17).
    if dealer_card_total() < 17:
        dealer_cards.append(random.choice(cards))
    # Checking for blackjack for the player.
    blackjack(player_cards)
    # Displaying the dealer's final hand.
    print(f"Dealers cards are {printer(dealer_cards)}")
    # Determining the outcome of the game based on card totals.
    if dealer_card_total() > 21:
        print("\nYou Win")
    else:
        if player_card_total() > dealer_card_total():
            print("\nYou win")
        elif dealer_card_total() > player_card_total():
            print("\nDealer win")
        elif dealer_card_total() == player_card_total():
            print("\nIt's draw")
