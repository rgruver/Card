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
        print('Reverse: '+str(deck.reverse))
        print('Study set: '+ deck.studyType)
        print('(0) Study deck')
        print('(1) Reverse Deck')
        print('(2) Set deck to all cards')
        print('(3) Set deck to flagged cards only')
        print('(4) Set deck to unflagged cards only')
        print('(5) Set deck to cards due today only')
        print('(6) Edit deck name')
        print('(7) Add cards')
        print('(8) Back to decks list')
        cmd = input()
        if cmd == '0':
            study(deck)
        if cmd == '1':
            deck.reverse = not deck.reverse
        if cmd == '2':
            self.studyType = 'All'
        if cmd == '3':
            self.studyType = 'Flag'
        if cmd == '4':
            self.studyType = 'NoFlag'
        if cmd == '5':
            self.studyType = 'Due'
        if cmd == '6':
            print('Enter a new name for the deck or enter .. to cancel')
            name = input()
            if name not == '..':
                deck.name = name
        if cmd == '7':

class Deck:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.reverse = False
        self.studyType = 'All'
        
    def loadCards():
        self.cards = [card1, card2]
    

deck = Deck("")
start()
