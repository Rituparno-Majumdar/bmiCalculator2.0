"""This is simple program that will ask the user their Height and Weight as inputs and then calculate their BMI
in terms of their Height and Weight and return back result, apart from that it will also notify the user some
additional messages based on their BMI"""

height = float(input("enter your height in m: "))  # This will ask user about the height and takes input
weight = float(input("enter your weight in kg: "))  # This will ask user about the weight and takes input

bmi = weight / (height ** 2)  # This will calculate their BMI
BMI = "{:.2f}".format(bmi)  # This will convert the result up to 2 decimal

print(f"Your BMI according to your height and weight is {BMI}")  # This will print the result

# Simple conditional statements that will print message based on the BMI
if bmi > 35:
    print("You are clinically obese!")
elif bmi > 30:
    print("You are obese!")
elif bmi > 25:
    print("overweight")
elif bmi > 18.5:
    print("normal weight")
else:
    print("underweight")
