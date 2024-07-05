# Name: Hero Brouwer
# Description: This program implements The Hangman Game.
# The computer picks a random word from a list and the player has to
# guess the word.


import random

words = ['science', 'deadlock', 'starvation', 'kickboxing']

# Chose a random word. For future: use a dictionary.
def choose_word():
    return random.choice(words)

# Splits the word
def split_word(word):
    return [x for x in word]

word = split_word(choose_word())
print(word)

for x in range(len(word)):
    word[x] = '_'

print(word)
