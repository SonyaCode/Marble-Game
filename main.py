import random
from random import randint

Even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print("  __  __          _____  ____  _      ______ ")
print(" |  \/  |   /\   |  __ \|  _ \| |    |  ____|")
print(" | \  / |  /  \  | |__) | |_) | |    | |__   ")
print(" | |\/| | / /\ \ |  _  /|  _ <| |    |  __|  ")
print(" | |  | |/ ____ \| | \ \| |_) | |____| |____ ")
print(" |_|__|_/_/    \_\_|  \_\____/|______|______|")
print("  / ____|   /\   |  \/  |  ____|             ")
print(" | |  __   /  \  | \  / | |__                ")
print(" | | |_ | / /\ \ | |\/| |  __|               ")
print(" | |__| |/ ____ \| |  | | |____              ")
print("  \_____/_/    \_\_|  |_|______|             ")

player = random.choice(range(1, 456))
print("Welcome to the Marble Game, Player",player)

marble = 10
computer = 10

while marble > 0 and marble != 20:
  number = randint(1, computer)
  user = input("Even or odd? ")
  
  if user.lower() == "even":
    if number in Even:
      marble += number
      computer -= number
      print("Correct! You have", marble, "marbles and opponent has", computer, "marbles.")
    else:
      marble -= number
      computer += number
      print("Wrong. You have", marble, "marbles and opponent has", computer, "marbles.")
  elif user.lower() == "odd":
    if number in Odd:
      marble += number
      computer -= number
      print("Correct! You have", marble, "marbles and opponent has", computer, "marbles.")
    else:
      marble -= number
      computer += number
      print("Wrong. You have", marble, "marbles and opponent has", computer, "marbles.")
  else:
    print("Invalid input. Please enter \"Even\" or \"Odd\".")

if marble == 20:
  print("You win.")
else:
  print("You lose.")