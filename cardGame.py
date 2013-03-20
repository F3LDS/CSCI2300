
""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
import random

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS  # Set up an array of size "52"
suitName = ("hearts", "diamonds", "spades", "clubs")  # Use division and mon?
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")

def clearDeck():
  for i in range(52):
    cardLoc[i] = 0

def assignCard(whichPlayer): # get random number from 0-52 (random card) and assign 0, 1, or 2 to it.
  cardNumber = random.randrange(0, 52)
  cardLoc[cardNumber] = whichPlayer

def showDeck():
  place = 0
  for i in cardLoc:
    if i == 0:
      i = "Deck"
    elif i == 1:
      i = "Player"
    elif i == 2:
      i = "Computer"
    print "%s | Location: %s" % (place, i)
    place = place + 1
def showHand(whichPlayer):
  return 0

def main():
  for i in range(5):
    assignCard(PLAYER)  # Check to make sure same card is not given to BOTH
    assignCard(COMP)

  showDeck()
  #showHand(PLAYER)
  #showHand(COMP)

main()