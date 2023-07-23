import string
import random

def password_generator(length, use_symbols, use_capitals):
    characters = string.ascii_lowercase + string.digits
    if use_symbols:
        characters += string.punctuation
    if use_capitals:
        characters += string.ascii_uppercase

    for _ in range(length):
        yield random.choice(characters)

def generate_password(length, use_symbols, use_capitals):
    return ''.join(password_generator(length, use_symbols, use_capitals))

# usage
length = int(input("Enter the length of the password: "))
use_symbols = input("Do you want symbols (!@#$%^&*())*&) in your password? (y/n): ").lower() == 'y'
use_capitals = input("Do you want capital letters in your password? (y/n): ").lower() == 'y'

password = generate_password(length, use_symbols, use_capitals)

# Print the password within a box
print("+" + "-"*length + "+")
print(" " + password + " ")
print("+" + "-"*length + "+")
