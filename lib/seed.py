#!/usr/bin/env python3

from models.cookbook import Cookbook
from models.recipe import Recipe


def seed_database():
    Cookbook.drop_table()
    Recipe.drop_table()
    Cookbook.create_table()
    Recipe.create_table()

    # Create seed data


seed_database()
print("Seeded database")
