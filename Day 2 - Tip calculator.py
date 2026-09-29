print("Welcome to the tip calculator!")
Bill = float(input("What was the total bill? $"))
Tip = int(input("How much tip would you like to give? 10, 12, or 15, "))
Percentage = Tip / 100
People = int(input("How many people to split the bill? "))

Each_person_should_pay = round((Bill + Bill * Percentage) / People, 2)
print(f"Each person should pay : ${Each_person_should_pay}")
