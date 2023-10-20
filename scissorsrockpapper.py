import random
print("What do you choose| press 0 for Rock | press 1 for Papper | press 2 for Scissors")
answer = int(input())

if answer == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif answer == 1:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif answer == 2:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
    print("Make correct choise")
    
computer_answer= random.randint(0, 2)
if computer_answer==0:
       print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif computer_answer == 1:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif computer_answer == 2:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")