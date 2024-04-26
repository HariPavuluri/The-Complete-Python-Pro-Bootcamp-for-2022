print("welcomee")
x = float(input("what was total bill \n"))
y = int(input("what percent tip u will give 10 or 12 \n"))
z = int(input("how many ppl will share bill \n"))

bill = ( x + (y/100)*x ) / z
print(bill)