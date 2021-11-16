from cogs.utils.get_alphabet import get_alphabet


def proper_case(string):
    alphabet = get_alphabet()

    if string[0] in alphabet.keys():
        return f"{alphabet[string[0]]}{string[1:]}"

    return string
