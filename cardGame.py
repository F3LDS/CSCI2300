
"""
Author: Alex Felder
   _________    ____  ____     _________    __  _________
  / ____/   |  / __ \/ __ \   / ____/   |  /  |/  / ____/
 / /   / /| | / /_/ / / / /  / / __/ /| | / /|_/ / __/
/ /___/ ___ |/ _, _/ /_/ /  / /_/ / ___ |/ /  / / /___
\____/_/  |_/_/ |_/_____/   \____/_/  |_/_/  /_/_____/

"""

import random # Import the random library in order to generate random numbers

NUMCARDS = 52 # Total cards in the deck
DECK = 0 # Variables to represent each player
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS  # Set up an array of size "52" to store the location of each card
suitName = ("hearts", "diamonds", "spades", "clubs")  #Lists containing every possible suit and rank name
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerHand = list() # Lists that will store the hand of each player
computerHand = list()
deckHand = list()


def clearDeck(): # Resets the location of each card by setting location to zero (deck)
  for i in range(52):
    cardLoc[i] = 0

def assignCard(whichPlayer):
  cardNumber = random.randrange(0, 51) # Get random card (# from 0-51) and assign 0, 1, or 2 to it (a player)
  if cardLoc[cardNumber] == 0: # Make sure the card isn't already taken
    cardLoc[cardNumber] = whichPlayer # If not, go ahead and assign it to whatever player is being delt to
  else:
    assignCard(whichPlayer) #If it is already taken, try another card

def showDeck(): # Function used to list out the entire deck with each card's location
  place = 0 # Counter used to keep track of what card we're dealing with
  for j in suitName: # For each suit name...
    for k in rankName: # Iterate through each rank
      cardName = "%s of %s" % (k, j) # and store this name combo in the cardName string for later
      location = cardLoc[place] # Location of this card (0, 1, or 2)
      if location == 0: # Set the name of the location correctly as well as store that card in its respective list
        location = "Deck"
        deckHand.append(cardName)
      elif location == 1:
        location = "Player"
        playerHand.append(cardName)
      elif location == 2:
        location = "Computer"
        computerHand.append(cardName)
      print "%s\t%s - %s" % (place, cardName, location) # Print out a nicely formatted string of each card and its location
      place = place + 1 # Move on to the next card number


def showHand(whichPlayer):
  if whichPlayer == 0: # Is this the Deck?
    print ""
    print "Deck"
    print "---------------"
    for i in computerHand: # Then print out the cards in it
      print i
  if whichPlayer == 1: # Is this the Player?
    print ""
    print "Player's Hand"
    print "-------------"
    for i in playerHand: # Then print out the cards in his/her hand
      print i
  if whichPlayer == 2: # Is this the Computer?
    print ""
    print "Computer's Hand"
    print "---------------"
    for i in computerHand: # Then print out the cards in its hand
      print i

def main():
  for i in range(5): # Deal five cards each to the Player and the Computer
    assignCard(PLAYER)
    assignCard(COMP)
  print ""
  print ""
  print "Card #      Card      Location"
  print "------------------------------"
  showDeck() # Print the deck and every card's location
  showHand(PLAYER) # Show the player's hand
  showHand(COMP) # Show the computer's hand
  print ""

main() # Init main function