''' 
This module assigns a number to a user based on what option they use
'''

import Day8Numbers

def initial_choice():
    #Asks user to choose one of the options
    while True:
        CHOICE = input("""What area did you come for today?\n
        \ta) Perfumes
        \tb) Medicine
        \tc) Cosmetics\n\n""").lower
        
        if CHOICE == a or CHOICE == b or CHOICE == c:
            return CHOICE
        else:
            print("Please make sure to choose one of the corrept options")
