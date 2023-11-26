from art import logo,vs
from game_data import data
import random
import os

def choose_acc():
    return random.choice(data)
def compare(guess,a,b):
    if a>b:
        return guess=='a'
    else:
        return guess=='b'
def format_data(acc):
    name = acc["name"]
    description = acc["description"]
    country = acc["country"]
  # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = choose_acc()
  account_b = choose_acc()

  while game_should_continue:
    account_a = account_b
    account_b = choose_acc()

    while account_a == account_b:
      account_b = choose_acc()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = compare(guess, a_follower_count, b_follower_count)

    os.system('clear')
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()