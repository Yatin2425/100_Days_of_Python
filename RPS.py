import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, scissor, paper]

computer_choice = random.randint(0, 2)
user_choice = int(input("Input your choice: 1 for rock, 2 for scissors, 3 for paper: ")) - 1

if user_choice < 0 or user_choice > 2:
    print("Invalid choice. Please select 1 for rock, 2 for scissors, or 3 for paper.")
else:
    print(f"Your move:\n{choices[user_choice]}")
    print(f"Computer's move:\n{choices[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("Computer wins!")
