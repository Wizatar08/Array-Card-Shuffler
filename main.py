import random # Imports the 'random' library

# INITIALIZE VARIABLES
VALUES = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"] # List of all available values
SUITES = ["Clubs", "Spades", "Hearts", "Diamonds"] # List of all available suites
currentDeck = [] # Current deck, is empty to start off with

def getAction():
  userInput = input("What would you like to do? => "); # Ask user for action
  while not checkInput(userInput, ['0', '1', '2', '3']): # If the input is not 0, 1, 2 or 3
    userInput = input("Invalid input. What would you like to do? => "); # Ask user for another input
  return userInput; # Return user input

# -----------------------------------
# checkInput(<input>, <validInputs>) --> Checks to see if an input matches an item in validInputs
# <input> - what is being checked
# <validInput> - a list of what input must be for this function to return true
# --> Returns true or false, depending on whether input is a value in validInputs
def checkInput(input, validInputs):
  for validInput in validInputs: # Loop through all valid inputs
    if input == validInput: # If one value in validInputs is the user input
      return True; # Return true
  return False; # Return false
  
# -----------------------------------
# buildDeck() --> Creates a deck
# --> Returns list(), which will be the deck
def buildDeck():
  currDeck = []; # Create new empty list
  for suite in SUITES: # Loop through suites and values
    for value in VALUES:
      currDeck.append('%s of %s' % (value, suite)); # Create a card based on both the current looped value and suite
  return currDeck; # Return deck

# -----------------------------------
# shuffleDeck(<deck>) --> Shuffles a deck
# <deck> - a list of strings where the order will be randomized
# --> Returns list(), which will be the shuffled deck
def shuffleDeck(deck):
  shuffledDeck = []; # Create new empty list
  currDeck = deck; # Create new list with values from 'deck' passed through
  while len(currDeck) > 0: # While currDeck has items inside
    ind = random.randint(0, len(currDeck) - 1); # Pick a random number between 0 and the length of currDeck-1
    card = currDeck[ind]; # Get the card corresponding to the index
    shuffledDeck.append(card); # Add this card to shuffledDeck
    currDeck.pop(ind); # Remove this card from currDeck
  return shuffledDeck; # Return shuffledDeck
  
# -----------------------------------
# printDeck(<deck>) --> Prints the deck to the console
# <deck> - a list of strings to be printed
def printDeck(deck):
  print("=================================================") # Print text to make things look pretty
  if len(deck) == 0: # If there is no cards in the deck
    print("You have an empty deck!") # Say so
  else: # If there are cards in the deck
    for i in range(0, len(deck)): # Loop through the indexes of the current deck
      print('(Card %s) => %s' % ((i + 1), deck[i])); # Print the index and corresponding card

# -----------------------------------
# mainMenu() --> Prints the user interface and allows user to pick options
def mainMenu(currentDeck):
  print('''=================================================
Here are your options:
[1] => Create a new deck
[2] => Shuffle the deck
[3] => Print the deck
[0] => Quit the program
=================================================''') # Print the menu
  action = getAction(); # Get action from user
  if action == '1': # If user inputs 1 - build a deck
    currentDeck = buildDeck();
  elif action == '2': # If user inputs 2 - shuffle the deck
    currentDeck = shuffleDeck(currentDeck);
  elif action == '3': # If user inputs 3 - print the deck
    printDeck(currentDeck);
  if action != '0': # If action is not zero, ask user for another action
    mainMenu(currentDeck);

print('=================================================');
print('''Welcome to my card shuffler program!
This program allows you to create a deck of cards and shuffle it. You may then print the deck to see the order of cards in a shuffled or ordered deck.
Your program will start with an empty deck. To begin, create a new deck. Creating a new deck when an existing deck already exists will recreate the deck with all the cards in order.
When prompted, enter 1 into the console to create a deck, enter 2 into the console to shuffle the deck, enter 3 into the console to print the deck and enter 0 into the console to quit the program. If you try to shuffle or print an empty deck, nothing will happen.''') # Print intro and instructions for user
print('=================================================');
input("Press ENTER to continue"); # Allow user to start program when ready

mainMenu(currentDeck); # Print menu for the first time