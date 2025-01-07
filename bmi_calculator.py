height = float(input("What is your height in meters: "))
weight = float(input("What is your weight in kg: "))

bmi = round(weight/height**2)

print('Your BMI is ', bmi)