import datetime
import tkinter
from tkinter import *

class Card:
    def __init__(self, front, back):
        self.front = front
        self.back = back
        self.rating = 0
        self.lastEdited = datetime.datetime.now()
        self.reviewDay = datetime.datetime.now()

class Deck:
    def __init__(self, deckName):
        self.name = deckName
        self.cards = {}

class Study:
    def __init__(self, root):
        self.root = root
        self.window = PanedWindow(self.root)
        self.pMain()

    def pMain(self):
        self.window.destroy()
        self.window = PanedWindow(self.root)
        self.window.pack()
        bDecks = Button(self.window, text="Decks", command= lambda:self.pDecks())
        bDecks.pack()

    def pDecks(self):
        self.window.destroy()
        self.window = PanedWindow(self.root)
        self.window.pack()
        for d in decks:
            b1 = Button(self.window, text=d.name, command= lambda d=d:self.pStudy(d))
            b1.pack()

    def pStudy(self, deck):
        print(deck.name)

decks = [Deck('hi'), Deck('Potato')]
root = tkinter.Tk()
s = Study(root)
