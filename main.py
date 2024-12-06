print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $\n"))
tip = int(input("What percentage tip would you like to give? 10 12 15 \n"))
people = int(input("How many people to split the bill? \n"))
total = ((bill *(tip/100))+bill)/people
print(f"Each person should pay: {round(total,2)}$")
