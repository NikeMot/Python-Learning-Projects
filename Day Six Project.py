from pathlib import Path
import os

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
    #Allows to delete or add categories to the recipe book
    while True:
        action = (input("""Would you like to add (a) or remove (r) a category?\n
        You can also exit clicking (e)""")).lower()
        if action == "a":
            new_category = str(input("What would you like to call the new category")).capitalize()
            try:
                os.mkdir(Path(book_path, new_category))
                print(f"{new_category} has been added!")
            except OSError:
                print("This folder exists already!")
        elif action == "r":
            removed_category = str(input("What would you like to remove category")).capitalize()
            try:
                os.rmdir(Path(book_path, removed_category))
            except OSError:
                print("Please verify the content of the folder and make sure it exist and it is empty")
        elif action == "e":
            break
        else:
            print("Please make sure to select a,r or e ")


def display_recipes(category_path):
    #Allows to display all the recipes is a specific category
    recipes = [file.name for file in category_path.glob("*.txt")]
    print(f"The available recipes in the chosen category are {recipes}")
    return

def modify_recipes(category_path):
    #Allows to delete or add categories to the recipe book
    while True:
        action = (input("""Would you like to (a) add, (r) remove or (v) view recipe?\n
        You can also exit clicking (e)""")).lower()

        if action == "a":
            recipe_add = (input("What would you like to call the new recipe")).capitalize()
            try:
                new_recipe = category_path / f"{recipe_add}.txt"
                new_recipe_path =Path(new_recipe)
                new_recipe_path.touch(exist_ok=False)
                print(f"{recipe_add} has been added!")
                write_recipes(new_recipe_path)
            except FileExistsError:
                print("This recipe exists already!")


        elif action == "r":
            removed_recipe = (input("Which recipe would you like to remove?")).capitalize()
            try:
                delete_recipe = category_path / f"{removed_recipe}.txt"
                remove_recipe_path = Path(delete_recipe)
                remove_recipe_path.unlink(missing_ok=False)
                print(f"{removed_recipe} has been removed!")

            except FileNotFoundError:
                print("This recipe does not exists!")

        elif action == "v":
            chosen_recipe = input("What recipe would you like to view?").capitalize()
            choose_recipe = category_path / f"{chosen_recipe}.txt"
            chosen_recipe_path = Path(choose_recipe)
            try:
                view_recipe = chosen_recipe_path.read_text()
                print(view_recipe)
                write_recipes(chosen_recipe_path)
            except FileNotFoundError:
                print("Please, make sure you type the recipe's name correctly")

        elif action == "e":
            break

        else:
            print("Please make sure to select a, r, v or e ")

def write_recipes(recipe):
    recipe_choose = input("Would you like to write on the chosen recipes? Y or N").lower()
    if recipe_choose == "n":
        return
    elif recipe_choose == "y":
        recipe_write = input("Would you like to (o) overwrite the contents or (a) append to the end\n").lower()

        if recipe_write == "o":
            new_text = input("Please, type in the new text\n")
            recipe.write_text(new_text)
            print("This has now been overwritten!\n" + recipe.read_text())

        elif recipe_write == "a":
            add_text = input("Please, type in the text to add\n")
            open_file = recipe.open("a")
            open_file.write(add_text)
            open_file.close()
            print("This has now been updated!\n" + recipe.read_text())
        else:
            print("Please, choose one of the options between o and a")


def main():
    book_path = import_recipe_book()

    print(f"""Welcome to the Electronic Recipe book!\nI'm currently parsing {book_path} for all the recipes""")
    print("\n")
    
    while True:
            
    
        categories = display_categories(book_path)
    
        choice = input("""Would you like to (s) Select a category or (m) Modify the current categories?\n
        You can also exit the program by pressing (e) """).lower()
    
        if choice == "s":
            category = input(f" Which category would you like to select?\n{categories}").capitalize()
            category_path = Path(book_path, category,)
            display_recipes(category_path)
            modify_recipes(category_path)
    
        elif choice == "m":
            modify_categories(book_path)
    
        elif choice  == "e":
            print("Closing the recipe book, thanks for using it!")
            break

main()
    

    
