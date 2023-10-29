import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if len(characters) == 0:
        return "Cannot generate password with no character set."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
password = generate_password(length=16, use_digits=True, use_special_chars=True)
print(password)
