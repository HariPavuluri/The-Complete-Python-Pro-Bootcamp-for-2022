x = int(input("enter the year \n"))

if x % 4 == 0:
    if(x% 100 == 0):
        if  x % 400 == 0:
            print(f"{x} is leap yr")
        else:
            print("x is not leap yr ")
    else:
        print("x is not leap yr")
else:
    print("x is not leap yr")



# x = "AbcAbcd"
# b = x.lower()
# c = x.count("d")
# print(b)