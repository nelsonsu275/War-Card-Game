import random
from Player import Player


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
print("------War Card Game-------")
name1 = input("Enter player one's name: ")
name2 = input("Enter player two's name: ")

deck = list(card_dictionary.keys())
random.shuffle(deck)
deckSize = len(deck)
halfDeck = int(deckSize/2)

player1 = Player(name1, deck[:halfDeck], True)
player2 = Player(name2, deck[deckSize - halfDeck:], True)
turnNumber = 1

while player1.has_cards is True and player2.has_cards is True:

    # displays each turn number
    print("Turn " + str(turnNumber))
    turnNumber += 1

    if not player1.stack:
        print("Draw: Player 1 out of cards")
        player1.has_cards = False
        break
    else:
        card1 = player1.stack.pop()

    if not player2.stack:
        print("Draw: Player 2 out of cards")
        player2.has_cards = False
        break
    else:
        card2 = player2.stack.pop()

    print(player1.name + " draws " + card1)
    print(player2.name + " draws " + card2)

    isWar = False
    if card_dictionary[card1] > card_dictionary[card2]:
        player1.stack.insert(0, card1)
        player1.stack.insert(0, card2)
        print(player1.name + "'s card has the higher rank")
        print(player1.name + " wins the round and add winnings to bottom of their deck.")
    elif card_dictionary[card1] < card_dictionary[card2]:
        player2.stack.insert(0, card1)
        player2.stack.insert(0, card2)
        print(player2.name + "'s card has the higher rank")
        print(player2.name + " wins the round and add winnings to bottom of their deck.")
    else:
        isWar = True
        print("Both player drew cards of same rank. War begins!")

    warStack = []
    while isWar:
        for card in range(3):
            if not player1.stack:
                print("War: Player 1 out of cards to draw.")
                player1.has_cards = False
                break
            else:
                warStack = player1.stack.pop()

        for card in range(3):
            if not player2.stack:
                print("War: Player 2 out of cards to draw.")
                player2.has_cards = False
                break
            else:
                warStack = player2.stack.pop()

        if not player1.stack:
            print("War: Player 1 out of cards to draw.")
            player1.has_cards = False
            break
        else:
            warCard1 = player1.stack.pop()
            print(player1.name + " draws " + warCard1)

        if not player2.stack:
            print("War: Player 2 out of cards to draw.")
            player2.has_cards = False
            break
        else:
            warCard2 = player2.stack.pop()
            print(player2.name + " draws " + warCard2)

        isWar = False
        if card_dictionary[warCard1] > card_dictionary[warCard2]:
            player1.stack.insert(0, card1)
            player1.stack.insert(0, card2)
            player1.stack.insert(0, warCard1)
            player1.stack.insert(0, warCard2)
            player1.stack.insert(0, warStack)
            print(player1.name + "'s card has the higher rank.")
            print(player1.name + " has won the round and add winnings to bottom of their deck.")
        elif card_dictionary[warCard1] < card_dictionary[warCard2]:
            player2.stack.insert(0, card1)
            player2.stack.insert(0, card2)
            player2.stack.insert(0, warCard1)
            player2.stack.insert(0, warCard2)
            player2.stack.insert(0, warStack)
            print(player2.name + "'s card has the higher rank.")
            print(player2.name + " has won the round and add winnings to bottom of their deck.")
        else:
            isWar = True
            print("Both player drew cards of same rank. Another war!")

    print("--------------------------")

print("-----War Game Results-----")

if player1.has_cards is False:
    print(player2.name + " has won the war game!")

if player2.has_cards is False:
    print(player1.name + " has won the war game!")

print("War Card Game lasted for " + str(turnNumber - 1) + " turns.")

# print(player1.stack)
# print(player2.stack)
