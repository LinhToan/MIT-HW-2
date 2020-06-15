# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:34:29 2020

@author: Hiro
"""

# Hangman Game
import string

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    secret_word = list(set(secret_word)) #converts secret_word into list because strings are immutable
    
    for letter in letters_guessed: #loops through each element in letters_guessed
        if letter in secret_word: #if letter is in list
            secret_word.remove(letter) #removes letters from secret_word
            if secret_word == []: #stopping condition is when secret_word is empty list
                return True
                break
            
    return False #returns True if all letters guessed are in secret_word
               #returns False if at least 1 letter is not in secret_word




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    secret_word = list(secret_word)
    
    for letter in range(len(secret_word)):
        if secret_word[letter] not in letters_guessed:
            secret_word[letter] = '_'
            
    secret_word = ''.join(secret_word)
    return secret_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    
    test = list(string.ascii_lowercase)
    
    for letter in range(len(letters_guessed)):
        if letters_guessed[letter] in test:
            test.remove(letters_guessed[letter])
    
    test = ''.join(test)
    return test

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
    print('Welcome to hangman! You will start with 6 guesses.')
    print('I am thinking of a word that is {} letters long'.format(str(len(secret_word))))
    print()
    
    guesses = 6
    letters_guessed = []
    
    while guesses > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        
        user_guess = input('Guess a letter: ')
        letters_guessed.append(user_guess) #keeps track of letters guessed by user
        
        if user_guess in secret_word: #if the word guessed is in secret word
            secret.remove(user_guess) #removes correctly guessed letter from the list
            print('That is correct. You have {} guesses left'.format(str(guesses)))
        else:
            guesses -= 1
            print('That is incorrect. You have {} guesses left'.format(str(guesses)))
        
        if guesses > 0: #if there are still guesses left
            if secret != []: #secret != [] means there are still letters to guess
                print('So far the word looks like: ', get_guessed_word(secret_word, letters_guessed))
                print('Available letters: ', get_available_letters(letters_guessed))
                print()
            else: #secret == [] means all letters in secret_word have been guessed
                print('Correct! The secret word is: ', secret_word)
        else:
            print('The secret word is: ', secret_word)
        
