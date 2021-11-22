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
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print("Welcome to The Rock, Paper, Scissors Game")
print("You will be playing against the Computer!!")
print("So get Ready!!")

choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
rand_choice=random.randint(0,2) 

if choice==0:
  print("You chose Rock.....")
  print(rock)
  if rand_choice==0:
    print("The Computer chooses.....")
    print(rock)
    print("The Computer also did a Rock")
    print("It's a Draw!")
  elif rand_choice==1:
    print("The Computer chooses.....")
    print(paper)
    print("The Computer did Paper")
    print("You Lose :(")
  else:
    print("The Computer chooses.....")
    print(scissors)
    print("The Computer did Scissors")
    print("You Win :)")
elif choice==1:
  print("You chose Paper.....")
  print(paper)
  if rand_choice==0:
    print("The Computer chooses.....")
    print(rock)
    print("The Computer did a Rock")
    print("You Win :)")
  elif rand_choice==1:
    print("The Computer chooses.....")
    print(paper)
    print("The Computer also did Paper")
    print("It's a Draw!")
  else:
    print("The Computer chooses.....")
    print(scissors)
    print("The Computer did Scissors")
    print("You Lose :(")
else:
  print("You chose Scissors.....")
  print(scissors)
  if rand_choice==0:
    print("The Computer chooses.....")
    print(rock)
    print("The Computer did a Rock")
    print("You Lose :(")
  elif rand_choice==1:
    print("The Computer chooses.....")
    print(paper)
    print("The Computer did Paper")
    print("You Win :)")
  else:
    print("The Computer chooses.....")
    print(scissors)
    print("The Computer also did Scissors")
    print("It's a Draw!")
