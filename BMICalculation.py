from math import pow
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))
BMI = weight / pow(height, 2)
if BMI < 18.5:
    print("You are underweight!")
elif 18.5<BMI<=25:
    print("According to your BMI, you have a healthy weight!")
elif 25<BMI<=30:
    print("You are overweight!")
elif 30<BMI<=40:
    print("You are obese!")
else:
    print("Severe obesity!")