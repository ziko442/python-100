import os
from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    nb_letter = 26
    if cipher_direction == 'decode':
        shift_amount *= -1 
    if cipher_direction == 'encode':
        nb_letter *= -1

    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        while new_position >= 26 or new_position < 0:
            new_position += nb_letter
        end_text += alphabet[new_position]

    print(f"The {cipher_direction}d text is {end_text}")



# print(logo)

should_end = False
while not should_end:
    os.system("cls")
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")


# def encrypt(plain_text, shift_amount):

#     cipher_text = ""
#     for letter in plain_text:
#       position = alphabet.index(letter)
#       new_position = position + shift_amount
#       # new_letter = alphabet[new_position]
#       # cipher_text += new_letter
#       if new_position >= 26:
#           new_position -= 26 
#       cipher_text += alphabet[new_position]
#     print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#   plain_text = ""
#   for letter in cipher_text:
#       position = alphabet.index(letter)
#       new_position = position - shift_amount
#       if new_position < 0:
#           new_position += 26
#       plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")

