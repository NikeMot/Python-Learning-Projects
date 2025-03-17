''' 
This module assigns a number to a user based on what option they use
'''

import Day8Numbers

perfume_gen = numbers.perfume_tracker()
medicine_gen = numbers.medicine_tracker()
cosmetic_gen = numbers.cosmetic_tracker()

def main():
    # Asks user to choose one of the options
    while True:
        CHOICE = input("""Hello. What area did you come for today?\n
        \ta) Perfumes
        \tb) Medicine
        \tc) Cosmetics\n
        You can also click E to exit\n\n""").lower()



        if CHOICE == "a":
            numbers.greeting(perfume_gen)

        elif CHOICE == "b":
            numbers.greeting(medicine_gen)

        elif CHOICE == "c":
            numbers.greeting(cosmetic_gen)

        elif CHOICE == "e":
            print("Goodbye!")
            break

        else:
            print("Please make sure to choose one of the options")


main()
