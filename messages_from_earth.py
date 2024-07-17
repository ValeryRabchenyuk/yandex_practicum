"""Ya.Contest try ID: 116175442."""
import string


def decipher(sequence: str) -> str:
    """Main function."""
    stack = []
    letter_counter = 0
    letter = ''

    for character in sequence:
        if character in string.digits:
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
