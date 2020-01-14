import time
import random
import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from Player import Player, card_dictionary, card_images

# dimensions for canvas size
HEIGHT = 500
WIDTH = 600


class WarGame:
    def __init__(self):
        # initialized root for the base of tkinter GUI
        self.root = tk.Tk()
        self.root.title("War Card Game")  # application title
        self.canvas = tk.Canvas(self.root, height=HEIGHT, width=WIDTH)  # window size
        self.canvas.pack()

        # optional background image
        self.background_image = tk.PhotoImage(file='skies.png')
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # frame used as the parent of children widgets
        self.frame = tk.Frame(self.root, bg='#80c1ff', bd=0.1)
        self.frame.place(relx=0.1, rely=0.1, relwidth=.8, relheight=0.8)
        self.title_label = tk.Label(self.frame, text="War Card Game")
        self.title_label.place(relx=.35, rely=.1, relwidth=.3, relheight=.1)

        # labels to prompt player for names
        self.player1_input_label = tk.Label(self.frame, text="Enter Player 1's name: ")
        self.player1_input_label.place(relx=.1, rely=.3, relwidth=.3, relheight=.1)
        self.player2_input_label = tk.Label(self.frame, text="Enter Player 2's name: ")
        self.player2_input_label.place(relx=.1, rely=.45, relwidth=.3, relheight=.1)

        # entry boxes for inputting names
        self.player1_entry = tk.Entry(self.frame, font=40)
        self.player1_entry.place(relx=.4, rely=.3, relwidth=.3, relheight=.1)
        self.player2_entry = tk.Entry(self.frame, font=40)
        self.player2_entry.place(relx=.4, rely=.45, relwidth=.3, relheight=.1)

        # labels for player names used in start function
        self.player1_label = tk.Label(self.frame, text="")
        self.player1_label.place_forget()
        self.player2_label = tk.Label(self.frame, text="")
        self.player2_label.place_forget()

        # labels for card count used in start function
        self.card_count_label1 = tk.Label(self.frame, text="")
        self.card_count_label1.place_forget()
        self.card_count_label2 = tk.Label(self.frame, text="")
        self.card_count_label2.place_forget()

        # label for turn number used in start function
        self.turn_label = tk.Label(self.frame, text="")
        self.turn_label.place_forget()

        # draw button and war button initialized for usage in start function
        self.draw_button = tk.Button(self.frame, text="Draw Card")
        self.draw_button.place_forget()
        self.war_button = tk.Button(self.frame, state="disabled", text="War!")  # war button initially disabled
        self.war_button.place_forget()

        # start button that calls start function
        self.start_button = tk.Button(self.frame, text="Start Game", command=lambda: self.start(
            self.player1_entry.get(), self.player2_entry.get()))
        self.start_button.place(relx=.35, rely=.6, relwidth=.3, relheight=.1)

        # Image file and label to display image
        self.card_image1 = Image.open(card_images["Blue Back"])
        self.card_image1 = ImageOps.fit(self.card_image1, (98, 150))
        self.card_image1 = ImageTk.PhotoImage(self.card_image1)
        self.card_label1 = tk.Label(self.frame, image=self.card_image1)
        self.card_label1.place_forget()
        # Image file and label to display image
        self.card_image2 = Image.open(card_images["Blue Back"])
        self.card_image2 = ImageOps.fit(self.card_image2, (98, 150))
        self.card_image2 = ImageTk.PhotoImage(self.card_image2)
        self.card_label2 = tk.Label(self.frame, image=self.card_image2)
        self.card_label2.place_forget()

        self.turn_number = 0  # turn number
        self.current_card1 = ""  # strings declared to hold card names in other functions
        self.current_card2 = ""

        self.root.mainloop()

    def start(self, name1, name2):
        # removes game title, start button, prompt labels, and entry boxes on calling start function
        self.title_label.after(100, self.title_label.destroy())
        self.start_button.after(100, self.start_button.destroy())
        self.player1_input_label.after(100, self.player1_input_label.destroy())
        self.player2_input_label.after(100, self.player2_input_label.destroy())
        self.player1_entry.after(100, self.player1_entry.destroy())
        self.player2_entry.after(100, self.player2_entry.destroy())

        # sets player name labels to the names received from user input
        self.player1_label['text'] = name1
        self.player1_label.place(relx=.35, rely=.05, relwidth=.3, relheight=.1)
        self.player2_label['text'] = name2
        self.player2_label.place(relx=.35, rely=.85, relwidth=.3, relheight=.1)

        # places card image for each player on the board
        self.card_label1.place(relx=.55, rely=.2)
        self.card_label2.place(relx=.25, rely=.4)

        # creates list of keys from card_dictionary and splits into two halves
        deck = list(card_dictionary.keys())
        random.shuffle(deck)
        deck_size = len(deck)
        half_deck = int(deck_size / 2)

        # creates two player objects from Player class with parameters for name, stack size, and remaining cards boolean
        player1 = Player(name1, deck[:half_deck], True)
        player2 = Player(name2, deck[deck_size - half_deck:], True)

        # places each players' card count on the board
        self.card_count_label1 = tk.Label(self.frame, text="Cards: " + str(len(player1.stack)))
        self.card_count_label1.place(relx=.8, rely=.05, relwidth=.15, relheight=.1)
        self.card_count_label2 = tk.Label(self.frame, text="Cards: " + str(len(player2.stack)))
        self.card_count_label2.place(relx=.05, rely=.85, relwidth=.15, relheight=.1)

        # places turn number on the board
        self.turn_label = tk.Label(self.frame, text="Turn: " + str(self.turn_number))
        self.turn_label.place(relx=.05, rely=.05, relwidth=.1, relheight=.1)

        # places war button on the board with war_draw function on press
        self.war_button['command'] = lambda: self.war_draw(player1, player2)
        self.war_button.place(relx=.77, rely=.67, relwidth=.2, relheight=.1)

        # places draw button on the board with draw function on press
        self.draw_button['command'] = lambda: self.draw(player1, player2)
        self.draw_button.place(relx=.77, rely=.87, relwidth=.2, relheight=.1)

    def draw(self, player1, player2):
        # checks if player has cards remaining to keep playing
        if player1.has_cards is True and player2.has_cards is True:
            self.turn_number += 1
            self.turn_label['text'] = "Turn: " + str(self.turn_number)

            # set player 1's card if stack not empty
            if not player1.stack:
                print("Draw: Player 1 out of cards")
                player1.has_cards = False
            else:
                card1 = player1.stack.pop()
                self.current_card1 = card1

            # set player 2's card if stack not empty
            if not player2.stack:
                print("Draw: Player 2 out of cards")
                player2.has_cards = False
            else:
                card2 = player2.stack.pop()
                self.current_card2 = card2

            print(self.turn_number)
            print(player1.name + " draws " + card1)
            print(player2.name + " draws " + card2)
            print(player1.stack)
            print(player2.stack)

            # matches each player's card ranks to determine who claims both cards to bottom of their deck
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
            else:  # if cards are equal rank, war begins
                self.war_button['state'] = "normal"  # war button activated
                self.draw_button['state'] = "disabled"  # draw button disabled
                print("Both player drew cards of same rank. War begins!")

            # refreshes card counts after drawing phase
            self.card_count_label1['text'] = "Cards: " + str(len(player1.stack))
            self.card_count_label2['text'] = "Cards: " + str(len(player2.stack))

            # displays card image for each player on the board
            self.show_card1(card1, .55, .2)
            self.show_card2(card2, .25, .4)

    def war_draw(self, player1, player2):
        # continues playing war if both player has cards remaining to play
        if player1.has_cards is True and player2.has_cards is True:
            war_stack = []  # stack of all face down cards during war
            offset1 = .05  # offset distances to change card positions
            offset2 = .05
            # loops 3 times for face down player 1 draws
            for card in range(3):
                if not player1.stack:
                    print("War: Player 1 out of cards to draw.")
                    player1.has_cards = False
                    break
                else:
                    war_card1 = player1.stack.pop()  # pops card from player 1's stack
                    war_stack.insert(0, war_card1)  # adds face down card to war stack
                    self.show_card1("Blue Back", .55 + offset1, .2)  # displays face down cards
                    offset1 += .05  # increase offset distance

            # loops 3 times for face down player 2 draws
            for card in range(3):
                if not player2.stack:
                    print("War: Player 2 out of cards to draw.")
                    player2.has_cards = False
                    break
                else:
                    war_card2 = player2.stack.pop()  # pops card from player 2's stack
                    war_stack.insert(0, war_card2)  # adds face down card to war stack
                    self.show_card2("Blue Back", .25 - offset2, .4)  # displays face down cards
                    offset2 += .05  # increase offset distance

            # draws player 1's war card
            if not player1.stack:
                print("War: Player 1 out of cards to draw.")
                player1.has_cards = False
            else:
                war_card1 = player1.stack.pop()
                self.show_card1(war_card1, .55 + offset1, .2)
                print(player1.name + " draws " + war_card1)

            # draws player 2's war card
            if not player2.stack:
                print("War: Player 2 out of cards to draw.")
                player2.has_cards = False
            else:
                war_card2 = player2.stack.pop()
                self.show_card2(war_card2, .25 - offset2, .4)
                print(player2.name + " draws " + war_card2)

            # compares war card's ranks to determine winner
            if card_dictionary[war_card1] > card_dictionary[war_card2]:
                player1.stack.insert(0, self.current_card1)
                player1.stack.insert(0, self.current_card2)
                player1.stack.insert(0, war_card1)
                player1.stack.insert(0, war_card2)
                for card in war_stack:
                    player1.stack.insert(0, card)
                self.war_button['state'] = "disabled"  # disables war button
                self.draw_button['state'] = "normal"  # enables draw button
                print(player1.name + "'s card has the higher rank.")
                print(player1.name + " has won the round and add winnings to bottom of their deck.")
            elif card_dictionary[war_card1] < card_dictionary[war_card2]:
                player2.stack.insert(0, self.current_card1)
                player2.stack.insert(0, self.current_card2)
                player2.stack.insert(0, war_card1)
                player2.stack.insert(0, war_card2)
                for card in war_stack:
                    player2.stack.insert(0, card)
                self.war_button['state'] = "disabled"  # disables war button
                self.draw_button['state'] = "normal"  # enables draw button
                print(player2.name + "'s card has the higher rank.")
                print(player2.name + " has won the round and add winnings to bottom of their deck.")
            else:
                # war continues again
                self.war_button['state'] = "normal"  # keeps war button enabled
                self.draw_button['state'] = "disabled"  # keeps draw button disabled
                print("Both player drew cards of same rank. Another war!")

            # refreshes card count for both players
            self.card_count_label1['text'] = "Cards: " + str(len(player1.stack))
            self.card_count_label2['text'] = "Cards: " + str(len(player2.stack))

    def show_card1(self, card, x, y):
        self.card_image1 = Image.open(card_images[card])
        self.card_image1 = ImageOps.fit(self.card_image1, (98, 150))
        self.card_image1 = ImageTk.PhotoImage(self.card_image1)
        self.card_label1 = tk.Label(self.frame, image=self.card_image1)
        self.card_label1.place(relx=x, rely=y)

    def show_card2(self, card, x, y):
        self.card_image2 = Image.open(card_images[card])
        self.card_image2 = ImageOps.fit(self.card_image2, (98, 150))
        self.card_image2 = ImageTk.PhotoImage(self.card_image2)
        self.card_label2 = tk.Label(self.frame, image=self.card_image2)
        self.card_label2.place(relx=x, rely=y)


# creates an object of the war game
game = WarGame()
