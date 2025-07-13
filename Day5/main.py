#Day 5 Project: Password Generator project
#Topics: Loops, lists & append, random module, user input
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Level 1 easy
''' 
     GeneratedPW = ""
     for i in range(0, nr_letters):
          GeneratedPW  += random.choice(letters)
     
     for i in range(0, nr_symbols):
          GeneratedPW  += random.choice(symbols)
     
     for i in range(0, nr_numbers):
          GeneratedPW  += random.choice(numbers)
     print(GeneratedPW )
     '''
     # level2-hard
finalPassword = []
for i in range(0, nr_letters):
         finalPassword.append(random.choice(letters))

for i in range(0, nr_symbols):
         finalPassword.append(random.choice(symbols))

for i in range(0, nr_numbers):
         finalPassword.append(random.choice(numbers))
print(finalPassword)
random.shuffle(finalPassword)
print(finalPassword)

password = ""
for i in finalPassword:
         password += i

print(f"Here's your password: {password}")
