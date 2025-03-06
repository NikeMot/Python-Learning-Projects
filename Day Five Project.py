from random import choice

def rules():

  word_list = ["yogurt","oblongate", "extrapolation", "anachronism", "molarity", "homophone", "indexing", "terracotta", "bauxite"]
  secret_word = choice(word_list)
  selected_letter = input("Welcome to HANGMAN! You have 6 tries to guess the word I'm thinking".lower())
  return selected_letter, secret_word

def dash_output(selected_letter,secret_word):
  dash_list = []
  letter_list = []
  for letter in secret_word:
    letter_list.append(letter)
    dash_list.append(" _ ")
  print("Guess the word", dash_list)
  return letter_list,dash_list,secret_word,selected_letter

def main_game(letter_list,dash_list,selected_letter,secret_word):
  
  count = 0
  
  
  body_dict {1:"Incorrect, right leg gone", 
             2:"Nope, left leg gone", 
             3:"Wrong, body gone", 
             4:"Negative, right arm gone", 
             5:"Not at all, left arm gone", 
             6:"YOU LOST!! Head's gone :( "}
  
  while count < 6:
    
    if letter_list.find(selected_letter) == -1:
      
      count += 1
      print(body_dict[count])
      print("")
      
      
    else:
      for index in enumerate(letter_list):
        if selected_letter == letter_list[index]
        dash_list.pop(index)
        dash_list.insert(index, selected_letter)
        print("You guessed correctly! " , dash_list)
        if dash_list == letter_list:
          print("You won! Well done!")
          return 
      
      

  else:
    print(body_dict[6])
    return 
