import string
import random
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()

    # getting user input
    user_letter = input('Guess a letter: ').upper()
    if used_letter in alphabet - used_letter:
        used_letter.add(used_letter)
        if used_letter in word_letters:
            word_letters.remove(used_letter)


user_input = input('Type something:').upper
print(user_input)
