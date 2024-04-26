import random
strname = input("enter names")

list_names = strname.split(", ")

# ran = random.choice(list_names)

# print(f"{ran} will pay bill")

x = random.randint(0,len(list_names)-1)

print(f" {list_names[x]} will pay bill ")


