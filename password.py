import random
import string

def create_pass(size):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(size))

try:
    pass_length = int(input("Enter the desired password length: "))
    if pass_length < 1:
        print("Password length must be at least 1.")
    else:
        print(f"Generated Password: {create_pass(pass_length)}")
except ValueError:
    print("Please enter a valid number.")
