import string
from cogs.utils.split import split


def get_alphabet():
    alphabet = {}

    lowercase = split(string.ascii_lowercase)

    for letter in lowercase:
        alphabet[letter] = letter.upper()

    return alphabet
