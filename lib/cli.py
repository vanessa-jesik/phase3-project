# lib/cli.py

from helpers import (
    create_cookbook,
    create_recipe,
    delete_cookbook,
    delete_recipe,
    exit_program,
    find_cookbook_by_id,
    find_cookbooks_by_author,
    find_cookbooks_by_name,
    find_recipe_by_id,
    find_recipes_by_cook_time_parameters,
    find_recipes_by_cuisine,
    find_recipes_by_name,
    find_recipes_by_servings,
    list_cookbook_recipes,
    list_cookbooks,
    list_recipes,
    update_cookbook,
    update_recipe,
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_cookbooks()
        elif choice == "2":
            find_cookbooks_by_name()
        elif choice == "3":
            find_cookbooks_by_author()
        elif choice == "4":
            find_cookbook_by_id()
        elif choice == "5":
            create_cookbook()
        elif choice == "6":
            update_cookbook()
        elif choice == "7":
            delete_cookbook()
        elif choice == "8":
            list_recipes()
        elif choice == "9":
            find_recipes_by_name()
        elif choice == "10":
            find_recipe_by_id()
        elif choice == "11":
            find_recipes_by_cuisine()
        elif choice == "12":
            find_recipes_by_servings()
        elif choice == "13":
            find_recipes_by_cook_time_parameters()
        elif choice == "14":
            create_recipe()
        elif choice == "15":
            update_recipe()
        elif choice == "16":
            delete_recipe()
        elif choice == "17":
            list_cookbook_recipes()
        else:
            print("Invalid choice")


def menu():
    print("*" * 50)
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all cookbooks")
    print("2. Find cookbooks by name")
    print("3. Find cookbooks by author")
    print("4: Find cookbook by id")
    print("5: Create cookbook")
    print("6: Update cookbook")
    print("7. Delete cookbook")
    print("8. List all recipes")
    print("9. Find recipes by name")
    print("10: Find recipe by id")
    print("11: Find recipes by cuisine")
    print("12: Find recipes by servings")
    print("13: Find recipes by cook time parameters")
    print("14: Create recipe")
    print("15: Update recipe")
    print("16: Delete recipe")
    print("17. List all recipes in a cookbook")
    print("*" * 50)


if __name__ == "__main__":
    main()
