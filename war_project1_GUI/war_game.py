import tkinter as tk

import PIL

from Player import Player, card_dictionary, card_images
import random
from PIL import Image, ImageTk, ImageOps

# import WarGame as war

HEIGHT = 500
WIDTH = 600


class WarGame:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("War Card Game")
        self.canvas = tk.Canvas(self.root, height=HEIGHT, width=WIDTH)
        self.canvas.pack()
        self.background_image = tk.PhotoImage(file='skies.png')
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)
        self.frame = tk.Frame(self.root, bg='#80c1ff', bd=0.1)
        self.frame.place(relx=0.1, rely=0.1, relwidth=.8, relheight=0.8)
        self.title_label = tk.Label(self.frame, text="War Card Game")
        self.title_label.place(relx=.35, rely=.1, relwidth=.3, relheight=.1)
        self.player1_input_label = tk.Label(self.frame, text="Enter Player 1's name: ")
        self.player1_input_label.place(relx=.1, rely=.3, relwidth=.3, relheight=.1)
        self.player2_input_label = tk.Label(self.frame, text="Enter Player 2's name: ")
        self.player2_input_label.place(relx=.1, rely=.45, relwidth=.3, relheight=.1)
        self.player1_entry = tk.Entry(self.frame, font=40)
        self.player1_entry.place(relx=.4, rely=.3, relwidth=.3, relheight=.1)
        self.player2_entry = tk.Entry(self.frame, font=40)
        self.player2_entry.place(relx=.4, rely=.45, relwidth=.3, relheight=.1)
        self.player1_label = tk.Label(self.frame, text="")
        self.player1_label.place_forget()
        self.player2_label = tk.Label(self.frame, text="")
        self.player2_label.place_forget()
        self.card_count_label1 = tk.Label(self.frame, text="")
        self.card_count_label1.place_forget()
        self.card_count_label2 = tk.Label(self.frame, text="")
        self.card_count_label2.place_forget()
        self.turn_label = tk.Label(self.frame, text="")
        self.turn_label.place_forget()
        self.draw_button = tk.Button(self.frame, text="Draw Card")
        self.draw_button.place_forget()
        self.war_button = tk.Button(self.frame, state="disabled", text="War!")
        self.war_button.place_forget()
        self.start_button = tk.Button(self.frame, text="Start Game", command=lambda: self.start(
            self.player1_entry.get(), self.player2_entry.get()))
        self.start_button.place(relx=.35, rely=.6, relwidth=.3, relheight=.1)

        self.turn_number = 0
        self.current_card1 = ""
        self.current_card2 = ""

        self.root.mainloop()

    def start(self, name1, name2):

        self.title_label.after(100, self.title_label.destroy())
        self.start_button.after(100, self.start_button.destroy())
        self.player1_input_label.after(100, self.player1_input_label.destroy())
        self.player2_input_label.after(100, self.player2_input_label.destroy())
        self.player1_entry.after(100, self.player1_entry.destroy())
        self.player2_entry.after(100, self.player2_entry.destroy())

        self.player1_label['text'] = name1
        self.player1_label.place(relx=.35, rely=.05, relwidth=.3, relheight=.1)
        self.player2_label['text'] = name2
        self.player2_label.place(relx=.35, rely=.85, relwidth=.3, relheight=.1)

        deck = list(card_dictionary.keys())
        random.shuffle(deck)
        deck_size = len(deck)
        half_deck = int(deck_size / 2)
        player1 = Player(name1, deck[:half_deck], True)
        player2 = Player(name2, deck[deck_size - half_deck:], True)

        self.card_count_label1 = tk.Label(self.frame, text="Cards: " + str(len(player1.stack)))
        self.card_count_label1.place(relx=.8, rely=.05, relwidth=.15, relheight=.1)
        self.card_count_label2 = tk.Label(self.frame, text="Cards: " + str(len(player2.stack)))
        self.card_count_label2.place(relx=.05, rely=.85, relwidth=.15, relheight=.1)

        self.turn_label = tk.Label(self.frame, text="Turn: " + str(self.turn_number))
        self.turn_label.place(relx=.05, rely=.05, relwidth=.1, relheight=.1)

        self.war_button['command'] = lambda: self.war_draw(player1, player2)
        self.war_button.place(relx=.77, rely=.67, relwidth=.2, relheight=.1)

        self.draw_button['command'] = lambda: self.draw(player1, player2)
        self.draw_button.place(relx=.77, rely=.87, relwidth=.2, relheight=.1)

    def draw(self, player1, player2):
        if player1.has_cards is True and player2.has_cards is True:
            self.turn_number += 1
            self.turn_label['text'] = "Turn: " + str(self.turn_number)

            if not player1.stack:
                print("Draw: Player 1 out of cards")
                player1.has_cards = False
            else:
                card1 = player1.stack.pop()
                self.current_card1 = card1

            if not player2.stack:
                print("Draw: Player 2 out of cards")
                player2.has_cards = False
            else:
                card2 = player2.stack.pop()
                self.current_card2 = card2

            self.card_count_label1['text'] = "Cards: " + str(len(player1.stack))
            self.card_count_label2['text'] = "Cards: " + str(len(player2.stack))

            print(self.turn_number)
            print(player1.name + " draws " + card1)
            print(player2.name + " draws " + card2)

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
                self.war_button['state'] = "normal"
                self.draw_button['state'] = "disabled"
                print("Both player drew cards of same rank. War begins!")

            self.card_count_label1['text'] = "Cards: " + str(len(player1.stack))
            self.card_count_label2['text'] = "Cards: " + str(len(player2.stack))
            self.show_card1(card1, .55, .2)
            self.show_card2(card2, .25, .4)


    def war_draw(self, player1, player2):
        if player1.has_cards is True and player2.has_cards is True:
            self.card_count_label1['text'] = "Cards: " + str(len(player1.stack))
            self.card_count_label2['text'] = "Cards: " + str(len(player2.stack))
            war_stack = []
            offset1 = .05
            offset2 = .05
            for card in range(3):
                if not player1.stack:
                    print("War: Player 1 out of cards to draw.")
                    player1.has_cards = False
                    break
                else:
                    war_card1 = player1.stack.pop()
                    war_stack += war_card1
                    self.show_card1(war_card1, .55 + offset1, .2)
                    offset1 += .05

            for card in range(3):
                if not player2.stack:
                    print("War: Player 2 out of cards to draw.")
                    player2.has_cards = False
                    break
                else:
                    war_card2 = player2.stack.pop()
                    war_stack += war_card2
                    self.show_card2(war_card2, .25 - offset2, .4)
                    offset2 += .05

            if not player1.stack:
                print("War: Player 1 out of cards to draw.")
                player1.has_cards = False
            else:
                war_card1 = player1.stack.pop()
                self.show_card1(war_card1, .55 + offset1, .2)
                print(player1.name + " draws " + war_card1)

            if not player2.stack:
                print("War: Player 2 out of cards to draw.")
                player2.has_cards = False
            else:
                war_card2 = player2.stack.pop()
                self.show_card2(war_card2, .25 - offset2, .4)
                print(player2.name + " draws " + war_card2)

            if card_dictionary[war_card1] > card_dictionary[war_card2]:
                player1.stack.insert(0, self.current_card1)
                player1.stack.insert(0, self.current_card2)
                player1.stack.insert(0, war_card1)
                player1.stack.insert(0, war_card2)
                player1.stack.insert(0, war_stack)
                self.war_button['state'] = "disabled"
                self.draw_button['state'] = "normal"
                print(player1.name + "'s card has the higher rank.")
                print(player1.name + " has won the round and add winnings to bottom of their deck.")
            elif card_dictionary[war_card1] < card_dictionary[war_card2]:
                player2.stack.insert(0, self.current_card1)
                player2.stack.insert(0, self.current_card2)
                player2.stack.insert(0, war_card1)
                player2.stack.insert(0, war_card2)
                player2.stack.insert(0, war_stack)
                self.war_button['state'] = "disabled"
                self.draw_button['state'] = "normal"
                print(player2.name + "'s card has the higher rank.")
                print(player2.name + " has won the round and add winnings to bottom of their deck.")
            else:
                self.war_button['state'] = "normal"
                self.draw_button['state'] = "disabled"
                print("Both player drew cards of same rank. Another war!")

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


game = WarGame()
