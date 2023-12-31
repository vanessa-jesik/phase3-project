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


def find_cookbooks_by_name():
    name = input("Input to search cookbooks by name: ")
    if name:
        cookbooks = Cookbook.find_by_name(name)
        if cookbooks:
            for cookbook in cookbooks:
                print(cookbook)
        else:
            print(f"Cookbook name containing {name} not found")
    else:
        print("Search entry cannot be empty.")


def find_cookbooks_by_author():
    author = input("Enter the Author's name: ")
    if author:
        cookbooks = Cookbook.find_by_author(author)
        if cookbooks:
            for cookbook in cookbooks:
                print(cookbook)
        else:
            print(f"Cookbooks by {author} not found")
    else:
        print("Search entry cannot be empty.")


def find_cookbook_by_id():
    id_ = get_num("Enter the Cookbook's id: ")
    cookbook = Cookbook.find_by_id(id_)
    print(cookbook) if cookbook else print(
        f"Cookbook {id_} not found. ID must reference a cookbook in the database."
    )


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
    id_ = get_num("Enter the id of the Cookbook to update: ")
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
        print(
            f"Cookbook {id_} not found. ID must reference a cookbook in the database."
        )


def delete_cookbook():
    id_ = get_num("Enter the id of the Cookbook to delete: ")
    if cookbook := Cookbook.find_by_id(id_):
        cookbook.delete()
        print(f"Cookbook {id_} deleted")
    else:
        print(
            f"Cookbook {id_} not found. ID must reference a cookbook in the database."
        )


def list_recipes():
    recipes = Recipe.get_all()
    for recipe in recipes:
        print(recipe)


def find_recipes_by_name():
    name = input("Input to search recipes by name: ")
    if name:
        recipes = Recipe.find_by_name(name)
        if recipes:
            for recipe in recipes:
                print(recipe)
        else:
            print(f"Recipe name containing {name} not found.")
    else:
        print("Search entry cannot be empty.")


def find_recipe_by_id():
    id_ = get_num("Enter the recipe's ID: ")
    recipe = Recipe.find_by_id(id_)
    print(recipe) if recipe else print(
        f"Recipe {id_} not found. ID must reference a recipe in the database."
    )


def find_recipes_by_cuisine():
    cuisine = input("Enter a cuisine type: ")
    recipes = Recipe.find_by_cuisine(cuisine)
    if recipes:
        for recipe in recipes:
            print(recipe)
    else:
        print(f"Recipes of cuisine type {cuisine} not found.")


def find_recipes_by_servings():
    servings = get_num("Enter desired number of servings: ")
    recipes = Recipe.find_by_servings(servings)
    if recipes:
        for recipe in recipes:
            print(recipe)
    else:
        print(f"Recipes serving {servings} not found.")


def find_recipes_by_cook_time_parameters():
    minutes = get_num(
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
    id_ = get_num("Enter the ID of the recipe to update: ")
    if recipe := Recipe.find_by_id(id_):
        try:
            name = input("Enter the recipe's new name: ")
            recipe.name = name
            cuisine = input("Enter the recipe's new cuisine type: ")
            recipe.cuisine = cuisine
            cook_time = get_num("Enter the recipe's new cook time in minutes: ")
            recipe.cook_time = cook_time
            servings = get_num("Enter how many the recipe now serves: ")
            recipe.servings = servings
            cookbook_id = get_num(
                "Enter the ID of the cookbook in which the recipe is published: "
            )
            recipe.cookbook_id = cookbook_id
            recipe.update()
            print(f"Success: {recipe}")
        except Exception as exc:
            print("Error updating recipe: ", exc)
    else:
        print(f"Recipe {id_} not found. ID must reference a recipe in the database.")


def delete_recipe():
    id_ = get_num("Enter the ID of the recipe to delete: ")
    if recipe := Recipe.find_by_id(id_):
        recipe.delete()
        print(f"Recipe {id_} deleted.")
    else:
        print(f"Recipe {id_} not found. ID must reference a recipe in the database.")


def list_cookbook_recipes():
    id_ = get_num("Enter the cookbook's ID: ")
    if cookbook := Cookbook.find_by_id(id_):
        for recipe in cookbook.recipes():
            print(recipe)
    else:
        print(
            f"Cookbook {id_} not found. ID must reference a cookbook in the database."
        )
