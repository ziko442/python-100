import random

letters = list('abcdefghijklmnopqrstuvwxyz')
symbols = list('!@#$%^&*()_')
numbers = list('0123456789')

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

charachters = ""

for l in range(nr_letters + 1):
    charachters += random.choice(letters)
for s in range(nr_symbols + 1):
    charachters += random.choice(symbols)
for n in range(nr_numbers + 1):
    charachters += random.choice(numbers)

print(charachters)

