#Day 3 project: Treasure Island
#Topic: Control flow and conditional statements, logic operators

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

move1=input("Now, you are in the treasure island. Do  you want to to left or right?"
            "Type 'left' or 'right': ").lower()

if move1=="left":
    move2=input("You have been to a middle of the island."
                "Type 'swim' if you want to swim."
                "Type 'wait' if you want to wait.").lower()
    if move2=="wait":
        move3=input("You have been to a main door."
                    "There are three of them, Red or Blue or Yellow"
                    "which one would you like to choose?").lower()
        if move3=="red":
            print("Burned by fire. "
                  "Game over.")
        if move3=="blue":
            print("Eaten by beasts."
                  "Game over.")
        if move3=="yellow":
            print("You win!")
        else:
            print("Game over")
    else:
        print("Attacked by trout. Game over.")
else:
    print("Fall into a blue. Game over.")



