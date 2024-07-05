# Name: Hero Brouwer
# Description: This program implements The Hangman Game.
# The computer picks a random word from a list and the player has to
# guess the word.


import random

# List of all possible drawings for Hangman
def show_hangman(tries):
    hangman_drawings = [
    '''
        |
        |
        |
        |
        |
        |
        |
        |
        ============
    ''',
    '''
        =========
        |       |
        |       |
        |
        |
        |
        |
        |
        |
        ============
    ''',
    '''
        =========
        |       |
        |       |
        |       O
        |
        |
        |
        |
        |
        ============
    ''',
    '''
        =========
        |       |
        |       |
        |       O
        |       |
        |       |
        |
        |
        |
        ============
    ''',
    '''
        =========
        |       |
        |       |
        |       O
        |       |\\
        |       |
        |
        |
        |
        ============
    ''',
    '''
        =========
        |       |
        |       |
        |       O
        |      /|\\
        |       |
        |
        |
        |
        ============
    ''',
    '''
        =========
        |       |
        |       |
        |       O
        |      /|\\
        |       |
        |        \\
        |
        |
        ============
    ''',
    '''
        =========
        |       |
        |       |
        |       O
        |      /|\\
        |       |
        |      / \\
        |
        |
        ============
    '''
    ]
    return hangman_drawings[tries]

words = ['science', 'deadlock', 'starvation', 'kickboxing']

# Chose a random word. For future: use a dictionary.
def choose_word():
    word = random.choice(words)
    return word.upper()

def game(word):
    word_completion = "_" * len(word)
    guessed_word = False
    guessed_letters = []
    guessed_words = []
    tries_left = 0

    print("Welcome to Hangman!")
    print("You can guess 7 letters wrong before you lose.")
    print("Good Luck!")
    print(show_hangman(tries_left))
    print(word_completion)

    while not guessed_word and tries_left < 7:
        guess = input("Guess the letter or word: ").upper()

        if len(guess) > 1 and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word!")

                guessed_words.append(guess)

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed this letter!")
            elif word.count(guess) == 0:
                tries_left += 1

        else:
            print("Input contains symbols that are not in the alphabet!\n")
            print("")

        show_hangman(tries_left)
        print(word_completion)

        # if guess_message not in 
        # If letter is wrong: add 1 with tries and display the new stage

while True:
    game(choose_word())