size = input("enter s or  m or l \n")
bill = 0

if(size == "s"):
    bill = 15
    print("15 $")
elif size == "m":
    bill = 20
    print("20 $")
elif size =="l":
    bill = 25
    print("25 $")
perpor = input(" Perpor Y or N \n")
if(perpor == "y"):
    if(size == "s"):
        bill = bill + 2
        print("extra 2$")
    else:
        bill = bill + 3
        print("extra 3$")
cheese = input(" Cheese Y or N \n")
if(cheese == "y"):
    bill = bill + 1
    print("extra 1$")

print(f" Finall bill is ${bill}")