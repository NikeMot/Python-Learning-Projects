from random import randint

name = input("What is your name, player?")

print(f"Hello {name} welcome to the game!/n I have thought of a number between 1 and 100./n You have 8 tries to get it right. Let's play!")

secret_number = randint(1, 100)

"""
while count < 8:
  guess  = input("Please, type your guess below\n")
  try:
    guess = int(guess)
  
    
    if guess == secret_number:
      
      count += 1
      print(f"YOU WIN!!! That was the right number!\nYou got it on guess number {count}")
      print("\n")
      break
  
    
    elif (guess < 1) or (guess > 100):
      
      count += 1
      print(f"This value is outside the scope of the game! Please try again.\n You have {8 - count} tries remaining")
      print("\n")
    
    elif guess < secret_number:

      count += 1
      print(f"Too low! Try again. \nYou have { 8 - count} tries remaining")
      print("\n")

    else:

      count += 1
      print(f"Too high! Try again. \nYou have {8 - count} tries remaining")
      print("\n")
      

  except ValueError:
    count += 1
    print(f"This is not a valid guess! The number has to be an integer. Please try again \nYou have {8 - count} tries remaining")

else:
  print("Too bad! You have finished your tries") 
"""

for i in range(8):
  
  guess  = input("Please, type your guess below\n")
  try:
    guess = int(guess)
  
    if guess == secret_number:
      
      print(f"YOU WIN!!! That was the right number!\nYou got it on guess number {i+1}")
      print("\n")
      break
  
    
    elif (guess < 1) or (guess > 100):
      
      
      print(f"This value is outside the scope of the game! Please try again.\nThis is guess number {i+1}")
      print("\n")
    
    elif guess < secret_number:

      print(f"Too low! Try again. \nThis is guess number {i+1}")
      print("\n")

    else:

      print(f"Too high! Try again. \nThis is guess number {i+1}")
      print("\n")
      

  except ValueError:
    
    print(f"This is not a valid input! The number has to be an integer. Please try again \nThis is guess number {i+1}")

else:
  print("Too bad! You have finished your tries")
