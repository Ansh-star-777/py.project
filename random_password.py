import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

password = ""

for i in range(4):
    password += random.choice(letters)

for i in range(4):
    password += random.choice(numbers)

password = list(password)
random.shuffle(password)
password = "".join(password)

print("Random Password:", password)
