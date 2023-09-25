# lib/models/recipe.py


class Recipe:
    all = {}

    def __init__(self, name, cuisine, cook_time, servings, cookbook_id, id=None):
        self.id = id
        self.name = name
        self.cuisine = cuisine
        self.cook_time = cook_time
        self.servings = servings
        self.cookbook_id = cookbook_id

    def __repr__(self):
        return (
            f"<Recipe {self.id}: {self.name} | Cuisine: {self.cuisine} "
            + f"| Cook time: {self.cook_time} minutes | Serves: {self.servings} "
            + f"| Cookbook ID: {self.cookbook_id}"
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if not 3 <= len(name) <= 16:
            raise ValueError("Name must be between 3 and 16 characters, inclusive.")
        else:
            self._name = name

    @property
    def cuisine(self):
        return self._cuisine

    @cuisine.setter
    def cuisine(self, cuisine):
        if not isinstance(cuisine, str) and len(cuisine):
            raise ValueError("Cuisine must be a non-empty string.")
        else:
            self._cuisine = cuisine

    @property
    def cook_time(self):
        return self._cook_time

    @cook_time.setter
    def cook_time(self, cook_time):
        if not isinstance(cook_time, int):
            raise ValueError("Cook time must be an integer.")
        else:
            self._cook_time = cook_time

    @property
    def servings(self):
        return self._servings

    @servings.setter
    def servings(self, servings):
        if not isinstance(servings, int):
            raise ValueError("Servings must be an integer.")
        else:
            self._servings = servings
