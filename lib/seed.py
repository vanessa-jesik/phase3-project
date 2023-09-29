#!/usr/bin/env python3
# lib/seed.py

from models.cookbook import Cookbook
from models.recipe import Recipe


def seed_database():
    Recipe.drop_table()
    Cookbook.drop_table()
    Cookbook.create_table()
    Recipe.create_table()

    # Create seed data
    home_cooking = Cookbook.create(
        "Home Cooking: Everything You Need to Know to Make Fabulous Food",
        "Gordon Ramsay",
        2013,
        4,
        9,
    )
    Recipe.create("Pimento Dip", "North American", 10, 2, home_cooking.id)
    Recipe.create("Stuffed Pork Tenderloin", "North American", 110, 4, home_cooking.id)
    Recipe.create("Gordon's Burger", "North American", 10, 1, home_cooking.id)

    bobs_burgers_burger_book = Cookbook.create(
        "The Bob's Burgers Burger Book: Real Recipes for Joke Burgers",
        "Loren Bouchard",
        2016,
        3,
        22,
    )
    Recipe.create(
        "Hummus A Tune Burger", "Canadian", 20, 1, bobs_burgers_burger_book.id
    )
    Recipe.create(
        "Blue Is The Warmest Cheese Burger",
        "Canadian",
        20,
        1,
        bobs_burgers_burger_book.id,
    )
    Recipe.create(
        "Bet It All On Black Garlic Burger",
        "Canadian",
        20,
        1,
        bobs_burgers_burger_book.id,
    )

    i_dont_want_to_cook = Cookbook.create(
        "The 'I Dont Want to Cook' Book: 100 Tasty, Healthy, Low-Prep Recipes for When You Just Dont Want to Cook",
        "Alyssa Brantley",
        2022,
        7,
        12,
    )
    Recipe.create(
        "Air Fryer Stuffed Mini Peppers",
        "Traditional Spanish",
        15,
        6,
        i_dont_want_to_cook.id,
    )
    Recipe.create("Baguette Pizza", "French", 20, 15, i_dont_want_to_cook.id)
    Recipe.create(
        "Sweet and Spicy Gochujang Chicken", "Korean", 15, 6, i_dont_want_to_cook.id
    )

    minecraft_cookbook = Cookbook.create(
        "Minecraft: Gather, Cook, Eat! Official Cookbook", "Tara Theoharis", 2023, 4, 4
    )
    Recipe.create("Suspicious Stew", "Minecraftian", 35, 4, minecraft_cookbook.id)
    Recipe.create("Torch Shooters", "Minecraftian", 35, 4, minecraft_cookbook.id)
    Recipe.create("Slimeball Tea", "Minecraftian", 20, 1, minecraft_cookbook.id)



seed_database()
print("Seeded database")
