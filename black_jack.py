# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = "Hit or stand?"
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards=[]

    def __str__(self):

        result = ""
        for i in range(len(self.cards)):
            result+=str(self.cards[i])+" "
        return result

    def add_card(self, card):
        self.cards.append(card)
        # add a card object to a hand

    def get_value(self):
        result=0
        hasAce = False
        for card in self.cards:
            val = VALUES[card.get_rank()]
            result+=val
            if val==1:
                hasAce=True
        if result+9<=21 and hasAce==True:
            result+=9
        
            
        return result
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
            # draw a hand on the canvas, use the draw method for cards
        for i in range(len(self.cards)):
            self.cards[i].draw(canvas, (pos[0]+i*80, pos[1]))
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                card=Card(suit,rank)
                self.deck.append(card)
    def shuffle(self):
        random.shuffle(self.deck)
        # shuffle the deck 
           # use random.shuffle()

    def deal_card(self):
        return self.deck.pop()	# deal a card object from the deck
    
    def __str__(self):
        result = ""
        for i in range(len(self.deck)):
            result+=str(self.deck[i])+" "
        return result	# return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, in_play, newdeck,player_hand,dealer_hand,score
    if in_play==True:
        score-=1
    newdeck=Deck()
    newdeck.shuffle()
    player_hand=Hand()
    dealer_hand=Hand()
    player_hand.add_card(newdeck.deal_card())
    dealer_hand.add_card(newdeck.deal_card())
    player_hand.add_card(newdeck.deal_card())
    dealer_hand.add_card(newdeck.deal_card())
    # your code goes here
    outcome="Hit or stand?"
    in_play = True

def hit():
    # replace with your code below
    global outcome, in_play,score
    # if the hand is in play, hit the player
    if in_play == False:
        return
    if player_hand.get_value()<=21:
        player_hand.add_card(newdeck.deal_card())
    
    if player_hand.get_value()>21:
    
        outcome= "Player has busted. New deal?"
        score-=1
        in_play=False
    
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    # replace with your code below
    global outcome, in_play,score
    if in_play == False:
        return
    if player_hand.get_value()>21:
        outcome= "You have busted. New deal?"
    else:
        while dealer_hand.get_value()<17:
            dealer_hand.add_card(newdeck.deal_card())
            
    if dealer_hand.get_value()>21:
        outcome="dealer has busted. New deal?"
        score+=1
    else:
        if dealer_hand.get_value()>=player_hand.get_value():
            outcome= "dealer wins. New deal?"
            score-=1
        else:
            outcome= "player wins. New deal?"
            score+=1
            
    in_play=False
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    player_hand.draw(canvas, [200,400])
    dealer_hand.draw(canvas,[200,200])
    canvas.draw_text('player', (220, 520), 24, 'Red')
    canvas.draw_text('dealer', [220, 180], 24, 'Blue')
    canvas.draw_text(outcome, [100, 100], 40, 'Pink')
    canvas.draw_text('score:' + str(score),[430,60],30,"Yellow")
    if in_play:
        pos=[200,200]
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * 0, 
                    CARD_CENTER[1] + CARD_SIZE[1] * 0)
        canvas.draw_image(card_back, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric