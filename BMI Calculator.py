weight=float(input("enter your weight in kgs: "))
height=float(input("enter your height in meters:"))
bmi=weight/(height**2)
print(f"bmi = {bmi}")
if bmi < 18.5:
    print ("underweight")
elif bmi < 25:
    print ("normal")
elif bmi < 30:
    print("overweight")
else:
    print ("obese")      