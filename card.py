decks = []

def start():
    while True:
        print('(0) Decks\n(1) Add Deck\n(2) Quit\n')
        cmd = input()
        if cmd == '0':
            decks()
        elif cmd == '1':
            addDeck()
        elif cmd == '2':
            break
        else:
            print('Bad input')

def decks():
    while True:
        decks = loadDecks()
        for i in range(len(decks)):
            print('('+str(i)+') '+decks[i].name)
        print('('+str(i+1)+') back')
        cmd = input()
        if int(cmd) <= i:
            deckPage(decks[i])
        if cmd == str(i+1):
            break
        else:
            print('Bad input')

def loadDecks():
    return [Deck('Math'), Deck('dsfjkl'), Deck('sldkfj')]

def deckPage(deck):
    while True:
        print(deck.name)
        print('Reverse: '+deck.reverse)
        print(
        print('(0) Study deck')
        print('(1) Reverse Deck')

class Deck:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.reverse = False
    def loadCards():
        self.cards = [card1, card2]
    

deck = Deck("")
start()
