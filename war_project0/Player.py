# Player class for creating objects for player name, stack size, and boolean for having cards left
class Player:
    def __init__(self, name, stack, has_cards):
        self.name = name
        self.stack = stack
        self.has_cards = has_cards


# card dictionary has card name as the key and card rank as the value
card_dictionary = {
    "Ace of Spades": 14,
    "King of Spades": 13,
    "Queen of Spades": 12,
    "Jack of Spades": 11,
    "Ten of Spades": 10,
    "Nine of Spades": 9,
    "Eight of Spades": 8,
    "Seven of Spades": 7,
    "Six of Spades": 6,
    "Five of Spades": 5,
    "Four of Spades": 4,
    "Three of Spades": 3,
    "Two of Spades": 2,

    "Ace of Clubs": 14,
    "King of Clubs": 13,
    "Queen of Clubs": 12,
    "Jack of Clubs": 11,
    "Ten of Clubs": 10,
    "Nine of Clubs": 9,
    "Eight of Clubs": 8,
    "Seven of Clubs": 7,
    "Six of Clubs": 6,
    "Five of Clubs": 5,
    "Four of Clubs": 4,
    "Three of Clubs": 3,
    "Two of Clubs": 2,

    "Ace of Hearts": 14,
    "King of Hearts": 13,
    "Queen of Hearts": 12,
    "Jack of Hearts": 11,
    "Ten of Hearts": 10,
    "Nine of Hearts": 9,
    "Eight of Hearts": 8,
    "Seven of Hearts": 7,
    "Six of Hearts": 6,
    "Five of Hearts": 5,
    "Four of Hearts": 4,
    "Three of Hearts": 3,
    "Two of Hearts": 2,

    "Ace of Diamonds": 14,
    "King of Diamonds": 13,
    "Queen of Diamonds": 12,
    "Jack of Diamonds": 11,
    "Ten of Diamonds": 10,
    "Nine of Diamonds": 9,
    "Eight of Diamonds": 8,
    "Seven of Diamonds": 7,
    "Six of Diamonds": 6,
    "Five of Diamonds": 5,
    "Four of Diamonds": 4,
    "Three of Diamonds": 3,
    "Two of Diamonds": 2,
}