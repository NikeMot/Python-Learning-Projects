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

def display_categories(book_path):
    #Allows to display all the categories of the recipe book
    categories = [folder.name for folder in book_path.glob("*/")]
    print(f"The available categories are: {categories}")
    return categories

def modify_categories(book_path):
    #Allows user to delete or add categories to the recipe book
    while True:
        action = (input("""Would you like to add (a) or remove (r) a category?\n
        You can also exit by clicking (e)""")).lower()
        if action == a:
            new_category = str(input("What would you like to call the new category")).capitalize()
            try:
                os.mkdir(Path(book_path, new_category))
                print(f"{new_category} has been added!")
            except OSError:
                print("This folder exists already!")
        elif action == r:
            removed_category = str(input("What would you like to remove category")).capitalize()
            try:
                os.rmdir(Path(book_path, removed_category))
            except OSError:
                print("Please verify the content of the folder and make sure it exist and it is empty")
        elif action == e:
            break
        else:
            print("Please make sure to select a,r or e ")

def display_recipes(category):
    #Allows to display all the recipes in a specific category
    recipes = [file.name for file in category.glob("*.txt")]
    print(f"The available recipes in the chosen category are {recipes}")
    return recipes

def modify_recipes():
    pass


def main():
    book_path = import_recipe_book()

    print(f"""Welcome to the Electronic Recipe book!\n
    I'm currently parsing {book_path} for all the recipes""")
    print("\n")

    categories = display_categories(book_path)

    choice = input("""Would you like to (s) Select a category or (m) Modify the current categories?\n
    You can also exit the program by pressing (e) """).lower()
    if choice == "s":
        pass
    elif choice == "m":
        modify_categories()
    elif choice  == "e":
        print("Closing the recipe book, thanks for using it!")
        return


main()

