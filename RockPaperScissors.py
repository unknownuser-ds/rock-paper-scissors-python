import random

a = ("rock", "paper", "scissor")

print(f"Choose any one : {a}")

x = random.choice(a)          # computer choice
z = input("Enter your choice = ").strip().lower()   # user choice

print(f"Your choice = {z}")
print(f"Computer choice = {x}")

if z == "rock" and x == "paper":
    print("\nYou lose!!!")
elif z == "rock" and x == "scissor":
    print("\nYou won!!!")
elif z == "paper" and x == "rock":
    print("\nYou won!!!")
elif z == "paper" and x == "scissor":
    print("\nYou lose!!!")
elif z == "scissor" and x == "paper":
    print("\nYou won!!!")
elif z == "scissor" and x == "rock":
    print("\nYou lose!!!")
elif z == x:
    print("\nTIE!!")
else:
    print("\nInvalid input!")

print("\nTHANK YOU FOR PLAYING")
