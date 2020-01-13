import random
from Player import Player, card_dictionary

print("------War Card Game-------")
name1 = input("Enter player one's name: ")
name2 = input("Enter player two's name: ")

# takes a list copy of the card dictionary keys and initializes split sizes
deck = list(card_dictionary.keys())
random.shuffle(deck)
deckSize = len(deck)
halfDeck = int(deckSize/2)

# creates two Player objects with parameters for name, deck size, and boolean for having cards remaining
player1 = Player(name1, deck[:halfDeck], True)
player2 = Player(name2, deck[deckSize - halfDeck:], True)
turnNumber = 1

# main loop until either player has no more cards to play
while player1.has_cards is True and player2.has_cards is True:

    # displays each turn number
    print("Turn " + str(turnNumber))
    turnNumber += 1

    # player 1 draws by popping from their stack
    if not player1.stack:
        print("Draw: Player 1 out of cards")
        player1.has_cards = False
        break
    else:
        card1 = player1.stack.pop()

    # player 2 draws by popping from their stack
    if not player2.stack:
        print("Draw: Player 2 out of cards")
        player2.has_cards = False
        break
    else:
        card2 = player2.stack.pop()

    print(player1.name + " draws " + card1)
    print(player2.name + " draws " + card2)

    isWar = False
    # compare ranks of card to determine which player claims both cards or begins a war
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

    # war loop
    war_stack = []
    while isWar:
        # draw 3 cards face down for player 1
        for card in range(3):
            if not player1.stack:
                print("War: Player 1 out of cards to draw.")
                player1.has_cards = False
                break
            else:
                war_card1 = player1.stack.pop()
                war_stack.insert(0, war_card1)

        # draw 3 cards face down for player 2
        for card in range(3):
            if not player2.stack:
                print("War: Player 2 out of cards to draw.")
                player2.has_cards = False
                break
            else:
                war_card2 = player2.stack.pop()
                war_stack.insert(0, war_card2)

        # draw 1 card to compare rank for player 1
        if not player1.stack:
            print("War: Player 1 out of cards to draw.")
            player1.has_cards = False
            break
        else:
            warCard1 = player1.stack.pop()
            print(player1.name + " draws " + warCard1)

        # draw 1 card to compare rank for player 2
        if not player2.stack:
            print("War: Player 2 out of cards to draw.")
            player2.has_cards = False
            break
        else:
            warCard2 = player2.stack.pop()
            print(player2.name + " draws " + warCard2)

        isWar = False
        # compare war card ranks to determine which player claims all original cards, war cards, and war stack
        if card_dictionary[warCard1] > card_dictionary[warCard2]:
            player1.stack.insert(0, card1)
            player1.stack.insert(0, card2)
            player1.stack.insert(0, warCard1)
            player1.stack.insert(0, warCard2)
            for card in war_stack:
                player1.stack.insert(0, card)
            print(player1.name + "'s card has the higher rank.")
            print(player1.name + " has won the round and add winnings to bottom of their deck.")
        elif card_dictionary[warCard1] < card_dictionary[warCard2]:
            player2.stack.insert(0, card1)
            player2.stack.insert(0, card2)
            player2.stack.insert(0, warCard1)
            player2.stack.insert(0, warCard2)
            for card in war_stack:
                player2.stack.insert(0, card)
            print(player2.name + "'s card has the higher rank.")
            print(player2.name + " has won the round and add winnings to bottom of their deck.")
        else:
            isWar = True  # when war cards are same rank, while loop continues and restarts war
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
