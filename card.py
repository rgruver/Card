import datetime

def start():
    while True:
        print('(0) Decks\n(1) Add Deck\n(2) Quit\n')
        cmd = input()
        if cmd == '0':
            decks(loadDecks())
        elif cmd == '1':
            addDeck()
        elif cmd == '2':
            break
        else:
            print('Bad input')

def decks(decksList):
    while True:
        for i in range(len(decksList)):
            print('('+str(i)+') '+decksList[i].name)
        print('('+str(i+1)+') back')
        cmd = input()
        if int(cmd) <= i:
            deckPage(decksList[int(cmd)])
        elif cmd == str(i+1):
            break
        else:
            print('Bad input')

def loadDecks():
    #Need to load from database
    return [Deck('Math'), Deck('dsfjkl'), Deck('sldkfj')]

def deckPage(deck):
    while True:
        print(deck.name)
        print('Reverse: '+str(deck.reverse))
        print('Study set: '+ deck.studyType)
        print('Random: '+str(deck.random))
        print('(0) Study deck')
        print('(1) Reverse Deck')
        print('(2) Set deck to all cards')
        print('(3) Set deck to flagged cards only')
        print('(4) Set deck to unflagged cards only')
        print('(5) Set deck to cards due today only')
        print('(6) Shuffle on/off')
        print('(7) Edit deck name')
        print('(8) Add cards')
        print('(9) Back to decks list')
        cmd = input()
        if cmd == '0':
            study(deck)
        elif cmd == '1':
            deck.reverse = not deck.reverse
        elif cmd == '2':
            deck.studyType = 'All'
        elif cmd == '3':
            deck.studyType = 'Flag'
        elif cmd == '4':
            deck.studyType = 'NoFlag'
        elif cmd == '5':
            deck.studyType = 'Due'
        elif cmd == '6':
            deck.random = not deck.random
        elif cmd == '7':
            print('Enter a new name for the deck or enter .. to cancel')
            name = input()
            if not name == '..':
                deck.name = name
        elif cmd == '8':
            print('Enter the new cards one at a time, first the front then the back or enter .. to go back to the deck menu')
            card = input()
            while not card == '..':
                front = card
                back = input()
                deck.addCard(Card(front, back))
                card = input()
        elif cmd == '9':
            break
        else:
            print('Bad input')

def study(deck):
    deck.loadCards()
    cards = zip(deck.cards, range(len(cards)))
    


class Deck:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.reverse = False
        self.studyType = 'All'
        self.random = False        
    def loadCards():
        #Load deck's cards from database
        self.cards = [card1, card2]
    def addCard(card):
        self.cards.add(card)
        #Add to database

class Card:
    def __init__(self, front, back):
        self.front = front
        self.back = back
        self.due = datetime.date.today()+datetime.timedelta(days=1)


start()
