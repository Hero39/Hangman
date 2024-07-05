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
    print(hangman_drawings[tries])

words = ['science', 'deadlock', 'starvation', 'kickboxing']

# Chose a random word. For future: use a dictionary.
def choose_word():
    word = random.choice(words)
    return word.upper()

def game(word):
    word_completion = "_" * len(word)
    word_is_guessed = False
    guessed_letters = []
    guessed_words = []
    tries_left = 0

    print("Welcome to Hangman!")
    print("You can guess 7 letters wrong before you lose.")
    print("Good Luck!")
    show_hangman(tries_left)
    print(word_completion)

    while not word_is_guessed and tries_left < 7:
        guess = input("Guess the letter or word: ").upper()

        # Guess is a word
        if len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word!")

            elif guess != word:
                print(f"No! {guess} is not the word!")
                guessed_words.append(guess)
                tries_left += 1
            else:
                word_is_guessed = True
                word_completion = word

        # Guess is a letter
        elif len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed this letter!")
            elif guess not in word:
                print("")
                tries_left += 1
                guessed_letters.append(guess)
            else:
                print(f"Nice! the letter {guess} is in the word")
                guessed_letters.append(guess)
                word_as_list = [*word_completion]
                indices = [i for i, x in enumerate(word) if x == guess]

                for index in indices:
                    word_as_list[index] = guess

                print(word_as_list)

                word_completion = "".join(word_as_list)
                print(word_completion)

                # Guess completes the word?
                if "_" not in word_completion:
                    word_is_guessed = True

        # Guess contains non-alphabetic symbols
        else:
            print("Guess is not valid")

        show_hangman(tries_left)
        print(word_completion)

        # if guess_message not in 
        # If letter is wrong: add 1 with tries and display the new stage

    if word_is_guessed:
        print("Congratulations! You guessed the word :)")
    else:
        print(f"You lost! The word was {word}")

def main():
    word = choose_word()
    game(word)

    new_round = input("Play again? (Y/N)").upper()

    while new_round == "Y" or new_round == "YES":
        word = choose_word()
        game(word)

if __name__ == "__main__":
    main()