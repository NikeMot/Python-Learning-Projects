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
