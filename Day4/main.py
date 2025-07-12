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
userChoice = [rock, paper, scissors]
userInputs = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if userInputs >= 0 and userInputs <= 2:
    print(userChoice[userInputs])

variableOption = random.randint(0, 2)

print("Select:")
print(userChoice[variableOption])

if userInputs >= 3 or userInputs < 0:
    print("Invalid input. Try again")

elif userInputs == 0 and variableOption == 2:
    print("Congrats, you won")
elif variableOption == 0 and userInputs == 2:
    print("Sorry, you try")
elif variableOption > userInputs:
    print("Sorry try again")
elif userInputs > variableOption:
    print("Congrats, you won")
elif variableOption == userInputs:
    print("Its over")