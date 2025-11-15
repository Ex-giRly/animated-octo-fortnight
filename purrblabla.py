height = float(input("Enter your height in cm"))
weight = float(input("Enter your weight in kg"))

BMI = weight / (height/100)**2

print("Your BMI is:", BMI)

if BMI <= 18.4:
    print("You are underweight.Eat more!")
elif BMI <= 24.9:
    print("You have a normal weight.Good job!")
elif BMI <= 29.9:
    print("You are overweight.Work out more!")
elif BMI <= 34.9:
    print("You are severely overweight.Exercise is a must!")
elif BMI <= 39.9:
    print("You are obese.See a doctor!")
else:
    print("You are clinically obese.Seek immediate medical attention!")