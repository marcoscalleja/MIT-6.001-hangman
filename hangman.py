# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
from ast import Return
import random
from re import A
import string
from soupsieve import SelectorSyntaxError

from tangled_up_in_unicode import lowercase


import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

WORDLIST_FILENAME = "Assignments/ps2/words.txt"


def load_words():
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

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

'pepito', ['e','p']
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    letters_guessed_set = set(letters_guessed)
    secret_Letters = set(secret_word)
    return letters_guessed_set == secret_Letters


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    output = []
    for i in list(secret_word):
      if i in letters_guessed:
        output.append(str(i))
      else:
        output.append('_ ')
    output
    out = ''.join(output)
    return out
   
get_guessed_word('secret_word', ['s', 'e','w'])

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    import string
    letters = list(string.ascii_lowercase)
    
    for i in letters_guessed:
      if i in letters:
        letters.remove(i)
    return ''.join(letters)

def is_letter_in_word(word, letter):
  word_list = []
  word_list = [char for char in word]
  if letter in word_list:
    print(f"Good Job! letter '{letter}' is in my word!")
    output = True
  else:
    print('Oops! That letter is not in my word:')
    output = False
  return output

is_letter_in_word('hola', 'a')
  

for char in 'hola':
  print(char)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''


    #load_words()

    secret_word = secret_word
    word_list = []
    word_list = [char for char in secret_word] # We append all chars of the word into a list

    guesses = 6
    warnings = 3
    guessed_letters = []
    letters_used = []
    output = 0
    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    

    while guesses > 0:  #While the number of guesses is still above 6
      print('-------------')
      print(f'I am thinking of a word that is {len(secret_word)} letters long')
      print(f'You have {guesses} guesses left.')
      print(f'Available letters: {get_available_letters(letters_used)}') 
      letter_chosen = str.lower(input('Please guess a letter: '))
      while (len(letter_chosen) != 1 or str.isalpha(letter_chosen)== False): #Checking the element given is a letter
        warnings = warnings - 1
        if warnings > 0:
          print(f'Oops! That is not a valid letter. You have {warnings} warnings left!')
        else:
          print(f'No warnings left! You lost 1 guess')
          guesses = guesses - 1
          if guesses == 0:
            break
          print(f'guesses left: {guesses}')
        letter_chosen = str.lower(input('Please guess a letter: '))

      while letter_chosen in guessed_letters: #Checking the user has not guessed that letter already
        warnings = warnings - 1
        if warnings > 0:
          print(f"Oops! You've already guessed that letter. You have {warnings} warnings left!")
        else:
          print(f'No warnings left! You lost 1 guess')
          guesses = guesses - 1
          print(f'guesses left: {guesses}')
        letter_chosen = input('Please guess a letter: ')


      #letter_chosen = str.lower(letter_chosen)

      if letter_chosen in word_list:
        guessed_letters.append(letter_chosen)
        letters_used.append(letter_chosen)
        print(f"Good Job! letter '{letter_chosen}' is in my word!")
      else:
        print('Oops! That letter is not in my word:')
        letters_used.append(letter_chosen)
        if letter_chosen in ['a', 'e', 'i', 'o', 'u']:
          guesses = guesses - 2
        else:
          guesses = guesses - 1
      print(get_guessed_word(secret_word, guessed_letters))
        

      if get_guessed_word(secret_word, guessed_letters) == secret_word:
        print('Congratulations! You won!')
        print(f'Your total score is {guesses*len(guessed_letters)}')
        output = 1
        break
    if output != 1:
      print(f'Sorry, you ran out of guesses. The word was {secret_word}')

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

#testing
#hangman('fresa')






def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    verification = []
    for index in range(len(my_word)): #We check for each character whether, when there is a letter, it has the same position in the word
      if len(my_word) == len(other_word):
        if my_word[index] == '_':
          verification.append(True)
        elif my_word[index] == other_word[index]:
          verification.append(True)
        else:
          verification.append(False)
      else:
        verification.append(False)

    if False in verification:
      output = False
    else:
      output = True

    return output

# my_guessed_word = get_guessed_word('apple', ['a', 'p']).replace(" ", "")
# list(my_guessed_word)
# another_word = 'apple'
# match_with_gaps(my_guessed_word, another_word)

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    word_list = []
    for word in wordlist:
      if match_with_gaps(my_word, word) == True:
        word_list.append(word)
        print(word)



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''

    #load_words()

    secret_word = secret_word
    word_list = []
    word_list = [char for char in secret_word] # We append all chars of the word into a list

    guesses = 6
    warnings = 3
    guessed_letters = []
    letters_used = []
    output = 0
    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    

    while guesses > 0:  #While the number of guesses is still above 6
      print('-------------')
      print(f'You have {guesses} guesses left.')
      print(f'Available letters: {get_available_letters(letters_used)}') 
      letter_chosen = str.lower(input('Please guess a letter: '))

      if letter_chosen == '*':
        my_splitted_word = get_guessed_word(secret_word, guessed_letters).replace(" ", "")
        show_possible_matches(my_splitted_word)
      else:
        while (len(letter_chosen) != 1 or str.isalpha(letter_chosen)== False): #Checking the element given is a letter
          warnings = warnings - 1
          if warnings > 0:
            print(f'Oops! That is not a valid letter. You have {warnings} warnings left!')
          else:
            print(f'No warnings left! You lost 1 guess')
            guesses = guesses - 1
            if guesses == 0:
              break
            print(f'guesses left: {guesses}')
          letter_chosen = str.lower(input('Please guess a letter: '))

        while letter_chosen in guessed_letters: #Checking the user has not guessed that letter already
          warnings = warnings - 1
          if warnings > 0:
            print(f"Oops! You've already guessed that letter. You have {warnings} warnings left!")
          else:
            print(f'No warnings left! You lost 1 guess')
            guesses = guesses - 1
            print(f'guesses left: {guesses}')
          letter_chosen = input('Please guess a letter: ')


        #letter_chosen = str.lower(letter_chosen)

        if letter_chosen in word_list:
          guessed_letters.append(letter_chosen)
          letters_used.append(letter_chosen)
          print(f"Good Job! letter '{letter_chosen}' is in my word!")
        else:
          print('Oops! That letter is not in my word:')
          letters_used.append(letter_chosen)
          if letter_chosen in ['a', 'e', 'i', 'o', 'u']:
            guesses = guesses - 2
          else:
            guesses = guesses - 1
        print(get_guessed_word(secret_word, guessed_letters))
          

        if get_guessed_word(secret_word, guessed_letters) == secret_word:
          print('Congratulations! You won!')
          print(f'Your total score is {guesses*len(guessed_letters)}')
          output = 1
          break
    if output != 1:
      print(f'Sorry, you ran out of guesses. The word was {secret_word}')



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
