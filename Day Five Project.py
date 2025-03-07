from random import choice

word_list = ["yogurt", "oblongate", "extrapolation", 
             "anachronism", "molarity", "homophone", 
             "indexing", "terracotta", "bauxite"]


def letter_select(word_list):
  #Checks user only inputs 1 alphabetic character at a time
  
  while True:
    selected_letter = input("Make sure to select only 1 letter at a time\n").lower()
    if len(selected_letter) == 1 and selected_letter.isalpha():
      return selected_letter

def dash_output(secret_word):
  #Creates and print a dashed output corresponding 
  #in length to the secret word
  
  dash_list = []
  letter_list = []

  for letter in secret_word:
    letter_list.append(letter)
    dash_list.append("_")
  on_screen_dash = "  ".join(dash_list)
  
  print("Guess the word", on_screen_dash)
  print("\n")
  
  return letter_list,dash_list,secret_word,on_screen_dash

def correct_guess(letter_list,selected_letter,dash_list,on_screen_dash):
  #Checks whether the chosen letter is present 
  #in the secret word
  
  for index,number in enumerate(letter_list):
        if selected_letter == letter_list[index]:
          dash_list.pop(index)
          dash_list.insert(index, selected_letter)
  on_screen_dash = "  ".join(dash_list)
  print("You guessed correctly! " , on_screen_dash)
  print("\n")
  if dash_list == letter_list:
    print("You won! Well done!")
    print("\n")
    play_again()
        
def play_again():
  #Asks whether you want to play again
  
  again = str(input("Press Y to play again\n"))
  again.lower()
  if again == "y":
    main_game(word_list)
  else:
    print("Thank you for playing!")
    return

def main_game(word_list):
  
  
  secret_word = choice(word_list)
  
  count = 0
 
  body_dict = {1:"Incorrect, right leg gone", 
             2:"Nope, left leg gone", 
             3:"Wrong, body gone", 
             4:"Negative, right arm gone", 
             5:"Not at all, left arm gone", 
             6:"YOU LOST!! Head's gone :( "}
  
  print("Welcome to Hangman! You have 6 tries to get the secret word")
  print("\n")

   
  letter_list,dash_list,secret_word,on_screen_dash = dash_output(secret_word)
  
  while count < 6:
    selected_letter=letter_select(word_list)
    
    
    if str(letter_list).find(selected_letter) == -1:
      count += 1
      print(body_dict[count])
      print("\n")
      continue
        
    else:
      correct_guess(letter_list,selected_letter,dash_list,on_screen_dash)
      
  else:
    play_again()
    


main_game(word_list)
