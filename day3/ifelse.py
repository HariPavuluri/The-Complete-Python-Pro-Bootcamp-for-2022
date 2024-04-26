x = int(input("enter the num \n"))

if x%2 == 0:
    print("x is even")
else:
    print("x is odd")




    # Under 18.5 they are underweight
    # Over 18.5 but below 25 they have a normal weight
    # Over 25 but below 30 they are slightly overweight
    # Over 30 but below 35 they are obese
    # Above 35 they are clinically obese.

a = int(input("enter weight \n"))
b = float(input("enter height \n"))

bmi = a / (b ** 2)

print(round(bmi))
if bmi < 18.5:
    print("under weight")
elif bmi < 25 and bmi >18.5:
    print("normal weight")
elif bmi < 30 and bmi > 25:
        print("slightly weight")
elif bmi <35 and bmi >30:
        print("obese")
elif bmi >35:
    print("clii obese") 
