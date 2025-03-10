from pathlib import Path
import os


def import_recipe_book():
    #Import the recipe book from a specific location
    while True:
        book_path = Path(input("Please, input the correct path of the recipe book\n"))
        try:
            os.chdir(book_path)
            return book_path

        except FileNotFoundError:
            import_recipe_book()

def display_categories():
    pass

def modify_categories():
    pass

def display_recipes():
    pass

def modify_recipes():
    pass


def main():

    print("""Welcome to the Nikenna Electronic Recipe book!\n
    The recipe is currently stored in""", Path.home())
