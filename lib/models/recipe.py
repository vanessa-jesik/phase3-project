# lib/models/recipe.py
from models.__init__ import CONN, CURSOR
from models.cookbook import Cookbook


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
            + f"| Cookbook ID: {self.cookbook_id}>"
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if not 3 <= len(name) <= 40:
            raise ValueError("Name must be between 3 and 40 characters, inclusive.")
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

    @property
    def cookbook_id(self):
        return self._cookbook_id

    @cookbook_id.setter
    def cookbook_id(self, cookbook_id):
        if not isinstance(cookbook_id, int):
            raise ValueError("Cookbook ID must be an integer.")
        if not Cookbook.find_by_id(cookbook_id):
            raise ValueError("Cookbook ID must reference a cookbook in the database.")
        else:
            self._cookbook_id = cookbook_id

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Recipe instances."""
        sql = """
            CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY,
            name TEXT,
            cuisine TEXT,
            cook_time INTEGER,
            servings INTEGER,
            cookbook_id INTEGER,
            FOREIGN KEY (cookbook_id) REFERENCES cookbooks(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Recipe instances."""
        sql = """
            DROP TABLE IF EXISTS recipes
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the name, cuisine, cook time, servings,
        and cookbook id values of the current Recipe object. Update
        object id attribute using the primary key value of the new row.
        Save the object in the local dictionary using table row's PK as
        dictionary key.
        """
        sql = """
            INSERT INTO recipes (name, cuisine, cook_time, servings, cookbook_id)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(
            sql,
            (self.name, self.cuisine, self.cook_time, self.servings, self.cookbook_id),
        )
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Recipe instance."""
        sql = """
            UPDATE recipes
            SET name = ?, cuisine = ?, cook_time = ?, servings = ?, cookbook_id = ?
            WHERE id = ?
        """
        CURSOR.execute(
            sql,
            (
                self.name,
                self.cuisine,
                self.cook_time,
                self.servings,
                self.cookbook_id,
                self.id,
            ),
        )
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Recipe instance,
        delete the dictionary entry, and reassign id attribute."""
        sql = """
            DELETE FROM recipes
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name, cuisine, cook_time, servings, cookbook_id):
        """Initialize a new Recipe instance and save the object to the database."""
        recipe = cls(name, cuisine, cook_time, servings, cookbook_id)
        recipe.save()
        return recipe

    @classmethod
    def instance_from_db(cls, row):
        """Return a Recipe object having the attribute values from the table row."""
        # Check the dictionary for  existing instance using the row's primary key
        recipe = cls.all.get(row[0])
        if recipe:
            # Ensure attributes match row values in case local instance was modified
            recipe.name = row[1]
            recipe.cuisine = row[2]
            recipe.cook_time = row[3]
            recipe.servings = row[4]
            recipe.cookbook_id = row[5]
        else:
            # If not in dictionary, create new instance and add to dictionary
            recipe = cls(row[1], row[2], row[3], row[4], row[5])
            recipe.id = row[0]
            cls.all[recipe.id] = recipe
        return recipe

    @classmethod
    def get_all(cls):
        """Return a list containing one Recipe object per table row."""
        sql = """
            SELECT *
            FROM recipes
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Recipe object corresponding to the table row matching the specified primary key."""
        sql = """
            SELECT *
            FROM recipes
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return Recipe object corresponding to first table row matching specified name."""
        sql = """
            SELECT *
            FROM recipes
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_cuisine(cls, cuisine):
        """Return all Recipe objects matching a specified cuisine type."""
        sql = """
            SELECT *
            FROM recipes
            WHERE cuisine is ?
        """
        rows = CURSOR.execute(sql, (cuisine,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_servings(cls, servings):
        """Return all Recipe objects matching the specified number of servings."""
        sql = """
            SELECT *
            FROM recipes
            WHERE servings is ?
        """
        rows = CURSOR.execute(sql, (servings,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_time(cls, minutes):
        """Return all Recipe objects requiring fewer than the specified number of minutes to cook."""
        sql = """
            SELECT *
            FROM recipes
            WHERE cook_time < ?
        """
        rows = CURSOR.execute(sql, (minutes,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
