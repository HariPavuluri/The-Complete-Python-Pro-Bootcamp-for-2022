name1 = input("enter name1 \n")
name2 = input("enter name2 \n")

name = name1 + name2
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")

x = t + r + u + e

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

y = l + o + v + e

score =int (str(x)+str(y))

if score<10 or score > 90:
    print(f" {score} like coke and mentos")
elif score>40 and score<50:
    print(f"{score} alright")
else:
    print(f"{score} you have")
