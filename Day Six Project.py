from pathlib import Path
import os


#Import the recipe book from a specific location
def import_recipe_book():
    while True:
        book_path = Path(input("Please, input the path of the recipe book\n"))
        print("\n")
        try:
            os.chdir(book_path)
            return book_path

        except FileNotFoundError:
            print("Could not find the directory. Please try again")

def display_categories():
    pass

def modify_categories():
    pass

def display_recipes():
    pass

def modify_recipes():
    pass


def main(book_path):

    print(f"Welcome to the Nikenna Electronic Recipe book!\nThe recipe is currently stored in {book_path} \n")
    return

book_path = import_recipe_book()
main(book_path)

