#Day 2 project: Tip calculator
#Topics: Primitive data types, Type conversion, mathematical ooperations, number manipulation and F strings

print("Welcome to the Tip calculator!")
totalBill=input("What was the total bill?\n")
totalTip=input("How much tip would you like to give? 10, 12, or 15 %?\n")
totalPeople=input("How many people will split the bill?\n")

conversionTip=float(totalTip)/100
totalPercent= float(totalBill) * conversionTip
totalWithTip=float(totalBill) + totalPercent
splittedBill=totalWithTip/int(totalPeople)
finalBill=round(splittedBill, 2)
print(f"Each person shoud pay: @{round(finalBill):.2f}")