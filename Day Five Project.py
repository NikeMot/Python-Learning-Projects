from random import choice

def letter_select():
  word_list = ["yogurt", "oblongate", "extrapolation", 
             "anachronism", "molarity", "homophone", 
             "indexing", "terracotta", "bauxite"]
  secret_word = choice(word_list)
  while True:
    selected_letter = input("Make sure to select only 1 letter at a time\n").lower()

  if len(selected_letter) == 1 and selected_letter.isalpha():

    return secret_word,selected_letter

def dash_output(secret_word,selected_letter):
  
  for letter in secret_word:
    letter_list.append(letter)
    dash_list.append(" _ ")
  print("Guess the word", dash_list)
  return letter_list,dash_list,secret_word,selected_letter

def main_game():
  
  count = 0
  dash_list = []
  letter_list = []
  
  secret_word,selected_letter=letter_select()
  
  
  body_dict = {1:"Incorrect, right leg gone", 
             2:"Nope, left leg gone", 
             3:"Wrong, body gone", 
             4:"Negative, right arm gone", 
             5:"Not at all, left arm gone", 
             6:"YOU LOST!! Head's gone :( "}
  
  while count < 6:
    letter_list,dash_list,secret_word,selected_letter = dash_output(secret_word,selected_letter)
    
    if letter_list.find(selected_letter) == -1:
      
      count += 1
      print(body_dict[count])
      print("")
      
      
    else:
      for index in enumerate(letter_list):
        if selected_letter == letter_list[index]:
          dash_list.pop(index)
          dash_list.insert(index, selected_letter)
          print("You guessed correctly! " , dash_list)
          if dash_list == letter_list:
            print("You won! Well done!")
            return 
      
      

  else:
    print(body_dict[6])
    return

main_game()
