import random

# Deck class with discard pile and reshuffle auto
class Deck:
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []

        card = self.card_list.pop()
        self.cards_in_play_list.append(card)
        return card

# Function to convert a number (0-51) into a card string that is readable
def card_to_string(card_num):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    rank = ranks[card_num % 13]
    suit = suits[card_num // 13]
    return f"{rank} of {suit}"

# Function to run the poker hand and draw phase
def poker_game():
    deck = Deck(52)
    
    # Deal 5 cards
    hand = [deck.deal() for _ in range(5)]
    print("\nYour initial hand:")
    for i, card in enumerate(hand, 1):
        print(f"{i}: {card_to_string(card)}")

    # Ask which cards to replace
    replace_input = input("\nEnter the card numbers to replace (e.g., 1 3 5), or press Enter to keep all: ")
    indices_to_replace = []

    if replace_input.strip():
        try:
            indices_to_replace = [int(i) - 1 for i in replace_input.split() if 1 <= int(i) <= 5]
        except ValueError:
            print("Invalid input. No cards will be replaced.")

    # Replace the selected cards
    for i in indices_to_replace:
        # Move to discard pile
        deck.discards_list.append(hand[i])
        # Deal new card
        hand[i] = deck.deal()               

    print("\nYour final hand:")
    for i, card in enumerate(hand, 1):
        print(f"{i}: {card_to_string(card)}")

# Run the game
poker_game()
