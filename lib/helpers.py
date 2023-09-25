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
    pass


def find_cookbook_by_author():
    pass


def find_cookbook_by_id():
    pass


def create_cookbook():
    pass


def update_cookbook():
    pass


def delete_cookbook():
    pass


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
