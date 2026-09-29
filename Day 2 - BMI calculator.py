print("Welcome to the BMI calculator:")
height = float(input("what is your height in m? "))
weight = float(input("what is your weight in kg? "))
bmi = weight / height**2

#either:
print("your BMI is: " + str(round(bmi, 2)))

#or:
bmi_2 = round(bmi, 2)
print(f"your height is {height}m and your weight is {weight}kg so your BMI is: {bmi_2}")
