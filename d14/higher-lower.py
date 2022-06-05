import os
import random
from game_data import data
from art import logo, vs


def check_result(guess):
	guess = user_guss
	if A['follower_count'] > B['follower_count']:
		return guess.lower() == 'a'
	if B['follower_count'] > A['follower_count']:
		return guess.lower() == 'b'
		

def format_data(account):
	return f"{account['name']}, a {account['description']}, from {account['country']}."


count = 0
print(logo)
game_end = False
B = random.choice(data)

while not game_end:
	A = B
	B = random.choice(data)
	while A == B:
		b = random.choice(data)
	print(f"Compare A: {format_data(A)}")
	print(vs)
	print(f"Against B: {format_data(B)}")
	# You're right! Current score: 1.
	user_guss = input("Who has more followers? Type 'A' or 'B':")
	os.system('cls')
	print(logo)
	if check_result(user_guss):
		count += 1
		print(f"You're right! Current score: {count}.")
	else:
		print(f"Sorry, that's wrong. Final score: {count}")
		game_end = True







