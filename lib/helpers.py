# lib/helpers.py
from models.cookbook import Cookbook
from models.recipe import Recipe


def exit_program():
    print("Goodbye!")
    exit()


def list_cookbooks():
    cookbooks = Cookbook.get_all()
    for cookbook in cookbooks:
        print(cookbook)


def find_cookbook_by_name():    # Need to enter the entire name
    name = input("Enter the Cookbooks's name: ").lower()
    cookbook = Cookbook.find_by_name(name)
    print(cookbook) if cookbook else print(
        f'Cookbook {name} not found')


def find_cookbook_by_author():  # Need to enter the entire name
    author = input("Enter the Author's name: ").lower()
    cookbook = Cookbook.find_by_author(author)
    print(cookbook) if cookbook else print(
        f'Cookbook by {author} not found')


def find_cookbook_by_id():
    try:
        id_ = int(input("Enter the Cookbook's id: "))
        cookbook = Cookbook.find_by_id(id_)
        print(cookbook) if cookbook else print(f'Cookbook {id_} not found')
    except Exception:
        print("Cookbook id has to be an integer.")


def create_cookbook():
    name = input("Enter the Cookbook's name: ")
    author = input("Enter the Cookbook's author: ")
    year = int(input("Enter the Cookbook's publishing year: "))
    month = int(input("Enter the Cookbook's publishing month: "))
    day = int(input("Enter the Cookbook's publishing day: "))
    try:
        cookbook = Cookbook.create(name, author, year, month, day)
        print(f'Success: {cookbook}')
    except Exception as exc:
        print("Error creating cookbook: ", exc)


def update_cookbook():
    id_ = input("Enter the Cookbook's id: ")
    if cookbook := Cookbook.find_by_id(id_):
        try:
            name = input("Enter the Cookbook's new name: ")
            cookbook.name = name
            author = input("Enter the Cookbook's new author: ")
            cookbook.author = author
            year = int(input("Enter the Cookbook's new publishing year: "))
            cookbook.year = year
            month = int(input("Enter the Cookbook's new publishing month: "))
            cookbook.month = month
            day = int(input("Enter the Cookbook's new publishing day: "))
            cookbook.day = day

            cookbook.update()
            print(f'Success: {cookbook}')
        except Exception as exc:
            print("Error updating cookbook: ", exc)
    else:
        print(f'cookbook {id_} not found')


def delete_cookbook():
    id_ = input("Enter the Cookbook's id: ")
    if cookbook := Cookbook.find_by_id(id_):
        cookbook.delete()
        print(f'Cookbook {id_} deleted')
    else:
        print(f'Cookbook {id_} not found')


def list_recipes():
    recipes = Recipe.get_all()
    for recipe in recipes:
        print(recipe)


def find_recipe_by_name():
    pass


def find_recipe_by_id():
    pass


def find_recipes_by_cuisine():
    pass


def find_recipes_by_servings():
    pass


# A STRETCH GOAL IS TO OFFER COOK TIME PARAMETERS
def find_recipes_by_cook_time_parameters():
    pass


def create_recipe():
    pass


def update_recipe():
    pass


def delete_recipe():
    pass


def list_cookbook_recipes():
    pass
