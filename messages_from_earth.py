"""Ya.Contest try ID: 116127853."""


def decipher(sequence: str) -> str:
    stack = []
    letter_counter = 0
    letter = ''

    for character in sequence:
        if character.isnumeric():
            letter_counter = letter_counter * 10 + int(character)
        elif character == '[':
            stack.append((letter, letter_counter))
            letter = ''
            letter_counter = 0
        elif character == ']':
            last_letter, number = stack.pop()
            letter = last_letter + number * letter
        else:
            letter += character

    return letter


if __name__ == '__main__':
    message = input()
    print(decipher(message))
