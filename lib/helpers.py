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


def find_cookbook_by_name():
    name = input("Enter the Cookbooks's name: ")
    cookbook = Cookbook.find_by_name(name)
    print(cookbook) if cookbook else print(f"Cookbook {name} not found. Please enter a vaild Name from the database.")


def find_cookbook_by_author():
    author = input("Enter the Author's name: ")
    cookbook = Cookbook.find_by_author(author)
    print(cookbook) if cookbook else print(f"Cookbook by {author} not found. Please enter a vaild Author from the database.")


def find_cookbook_by_id():
    try:
        id_ = int(input("Enter the Cookbook's id: "))
        cookbook = Cookbook.find_by_id(id_)
        print(cookbook) if cookbook else print(f"Cookbook {id_} not found. Please enter vaild integer from database.")
    except Exception:
        print("Cookbook id has to be an integer.")


def create_cookbook():
    name = input("Enter the Cookbook's name: ")
    author = input("Enter the Cookbook's author: ")
    year = get_num("Enter the Cookbook's publishing year: ")
    month = get_num("Enter the Cookbook's publishing month: ")
    day = get_num("Enter the Cookbook's publishing day: ")
    try:
        cookbook = Cookbook.create(name, author, year, month, day)
        print(f"Success: {cookbook}")
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
            year = get_num("Enter the Cookbook's new publishing year: ")
            month = get_num("Enter the Cookbook's new publishing month: ")
            day = get_num("Enter the Cookbook's new publishing day: ")
            cookbook.pub_date = f"{year:04d}/{month:02d}/{day:02d}"
            cookbook.update()
            print(f"Success: {cookbook}")
        except Exception as exc:
            print("Error updating cookbook: ", exc)
    else:
        print(f"cookbook {id_} not found")


def delete_cookbook():
    id_ = input("Enter the Cookbook's id: ")
    if cookbook := Cookbook.find_by_id(id_):
        cookbook.delete()
        print(f"Cookbook {id_} deleted")
    else:
        print(f"Cookbook {id_} not found")


def list_recipes():
    recipes = Recipe.get_all()
    for recipe in recipes:
        print(recipe)


def find_recipe_by_name():
    name = input("Enter the recipe's name: ")
    recipe = Recipe.find_by_name(name)
    print(recipe) if recipe else print(f"Recipe name containing {name} not found.")


def find_recipe_by_id():
    id_ = input("Enter the recipe's ID: ")
    recipe = Recipe.find_by_id(id_)
    print(recipe) if recipe else print(f"Recipe {id_} not found.")


def find_recipes_by_cuisine():
    cuisine = input("Enter a cuisine type: ")
    recipes = Recipe.find_by_cuisine(cuisine)
    if recipes:
        for recipe in recipes:
            print(recipe)
    else:
        print(f"Recipes of type {cuisine} not found.")


def find_recipes_by_servings():
    servings = input("Enter desired servings: ")
    recipes = Recipe.find_by_servings(servings)
    if recipes:
        for recipe in recipes:
            print(recipe)
    else:
        print(f"Recipes serving {servings} not found.")


def find_recipes_by_cook_time_parameters():
    minutes = input(
        "Find recipes taking fewer than ___ minutes to cook. Enter minutes: "
    )
    recipes = Recipe.find_by_time(minutes)
    if recipes:
        for recipe in recipes:
            print(recipe)
    else:
        print(f"No recipes taking fewer than {minutes} minutes to cook were found.")


def get_num(message):
    try:
        return int(input(message))
    except:
        print("Not a valid number.")
        return get_num(message)


# IS THIS THE BEST WAY TO ASSURE INTEGERS BECAUSE THROWS ERROR IF USER INPUTS LETTERS
def create_recipe():
    name = input("Enter the recipe's name: ")
    cuisine = input("Enter the recipe's cuisine type: ")
    cook_time = get_num("Enter the recipe's cook time in minutes: ")
    servings = get_num("Enter how many the recipe serves: ")
    cookbook_id = get_num(
        "Enter the ID of the cookbook in which the recipe is published: "
    )

    try:
        recipe = Recipe.create(name, cuisine, cook_time, servings, cookbook_id)
        print(f"Success: {recipe}")
    except Exception as exc:
        print("Error creating recipe: ", exc)


def update_recipe():
    id_ = input("Enter the recipe's ID: ")
    if recipe := Recipe.find_by_id(id_):
        try:
            name = input("Enter the recipe's new name: ")
            recipe.name = name
            cuisine = input("Enter the recipe's new cuisine type: ")
            recipe.cuisine = cuisine
            cook_time = int(input("Enter the recipe's new cook time in minutes: "))
            recipe.cook_time = cook_time
            servings = int(input("Enter how many the recipe now serves: "))
            recipe.servings = servings
            cookbook_id = int(
                input("Enter the ID of the cookbook in which the recipe is published: ")
            )
            recipe.cookbook_id = cookbook_id
            recipe.update()
            print(f"Success: {recipe}")
        except Exception as exc:
            print(f"Error updating recipe: ", exc)
    else:
        print(f"Recipe {id_} not found.")


def delete_recipe():
    id_ = input("Enter the recipe's ID: ")
    if recipe := Recipe.find_by_id(id_):
        recipe.delete()
        print(f"Recipe {id_} deleted.")
    else:
        print(f"Recipe {id_} not found.")


def list_cookbook_recipes():
    id_ = input("Enter the cookbook's ID: ")
    if cookbook := Cookbook.find_by_id(id_):
        for recipe in cookbook.recipes():
            print(recipe)
    else:
        print(f"Cookbook {id_} not found.")
