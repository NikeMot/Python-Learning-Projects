from random import choice

def rules():

  word_list = ["yogurt","oblongate", "extrapolation", "anachronism", "molarity", "homophone", "indexing", "terracotta", "bauxite"]
  secret_word = choice(word_list)
  selected_letter = input("Welcome to HANGMAN! You have 6 tries to guess the word I'm thinking".lower())
  return selected_letter, secret_word
