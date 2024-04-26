rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

user = int(input("1.rock 2.paper 3.siccsor \n"))
if user<=3 and user>=1:
    if user==1:
        print(rock)
    elif user==2:
        print(paper)
    elif user==3:
        print(scissors)


    print("computer was \n")

    co = random.randint(1,3)
    if co==1:
        print("Rock\n")
        print(rock)
    if co==2:
        print("Paper\n")
        print(paper)
    if co == 3:
        print("scissors\n")
        print(scissors)

    print("result is.. \n")
    if user==co:
        print("draww match")
    if user==1:
        if co==3:
            print("user won")
        if co==2:
            print("computer won")

    if user==2:
        if co==1:
            print("user won")
        if co==3:
            print("computer won")

    if user==3:
        if co==1:
            print("computer won")
        if co==2:
            print("user won")
else:
    print("enter 1 or 2 or 3")





