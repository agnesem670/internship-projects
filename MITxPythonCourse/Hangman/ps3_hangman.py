# Hangman game

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretWord = list(secretWord) # list of strings
    numberOfHits = 0
    for letter in secretWord:
      if letter in lettersGuessed:
        numberOfHits += 1
    if numberOfHits == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretWord = list(secretWord) # list of strings
    guessWord = []
    for letter in secretWord:
      if letter in lettersGuessed:
        guessWord.append(letter)
      else:
        guessWord.append('_')
    return guessWord

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'w', 23: 'v', 24: 'x', 25: 'y', 26: 'z'} # The letters that may still be guessed. Every time a player guesses a letter, the guessed letter must be removed from availableLetters (and if they guess a letter that is not in availableLetters, you should print a message telling them they've already guessed that - so try again!).
    for letter in lettersGuessed:
      if letter in availableLetters:
        availableLetters.remove(letter)
    return ''.join(availableLetters)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    secretWord = chooseWord(wordlist)
    lettersGuessed = [] # a list with guessed letters
    numberOfGuesses = 0
    mistakesMade = 0
    guessWord = getGuessedWord(secretWord, lettersGuessed)
    lastGuessWord = guessWord

# first guess
    if numberOfGuesses == 0: 
      print ('Welcome to the game Hangman!')
      print ('I am thinking of a word that is', len(secretWord), 'letters long.') # number of letters in chooseWord

# every guesses
    while numberOfGuesses >= 0 and mistakesMade <8:
      print ('You have', 8 - mistakesMade, 'guesses left.') # number of left guesses
      print ("Available letters:", getAvailableLetters(lettersGuessed) )
      guess = input ('Please guess a letter: ') # input, a letter
      numberOfGuesses += 1
      guessInLowerCase = guess.lower() # only lower letter

      if guessInLowerCase in lettersGuessed: # checks with previus hits
        mistakesMade += 1
        print ("Oops! You've already guessed that letter:", lastGuessWord)

      elif guessInLowerCase not in lettersGuessed:      # adds letter to list and updates guessWord ang lastGuessWord
        lettersGuessed.append(guessInLowerCase) 
        lastGuessWord = guessWord
        guessWord = getGuessedWord(secretWord, lettersGuessed)

        if lastGuessWord == guessWord:
          mistakesMade += 1
          print ("Oops! That letter is not in my word:", guessWord)

        if lastGuessWord != guessWord:
          print ("Good guess:", guessWord)
          if isWordGuessed(secretWord, lettersGuessed) == True:
            print ("Congratulations, you won!")
            break
    if mistakesMade == 8:
      print ("Sorry, you ran out of guesses. The word was else.")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
