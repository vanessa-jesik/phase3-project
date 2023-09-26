from models.__init__ import CONN, CURSOR


class Cookbook:
    all = {}

    def __init__(self, name, author, year, month, day, id=None):
        self.id = id
        self.name = name
        self.author = author
        self.pub_date = f"{year:04d}/{month:02d}/{day:02d}"

    def __repr__(self):
        return f"<Cookbook {self.id}: \n{self.name}, \nBy: {self.author}, \nPublished on: {self.pub_date}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise Exception("Name must be a string")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, str) and len(author):
            self._author = author
        else:
            raise Exception("Author must be a string")

    @property
    def pub_date(self):
        return self._pub_date

    @pub_date.setter
    def pub_date(self, date_str):
        year, month, day = map(int, date_str.split("/"))

        if isinstance(year, int) and isinstance(month, int) and isinstance(day, int):
            self._pub_date = date_str
        else:
            raise Exception("Year, month, and day must be integers")

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Cookbook instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS cookbooks (
            id INTEGER PRIMARY KEY,
            name TEXT,
            author TEXT,
            pub_date TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Cookbook instances"""
        sql = """
            DROP TABLE IF EXISTS cookbooks;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the name, author and pub_date values of the current Cookbook instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO cookbooks (name, author, pub_date)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.author, self.pub_date))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, author, year, month, day):
        """Initialize a new Cookbook instance and save the object to the database"""
        cookbook = cls(name, author, year, month, day)
        cookbook.save()
        return cookbook

    def update(self):
        """Update the table row corresponding to the current Cookbook instance."""
        sql = """
            UPDATE cookbooks
            SET name = ?, author = ?, pub_date = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.author, self.pub_date, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Cookbook instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM cookbooks
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Cookbook object having the attribute values from the table row."""
        cookbook = cls.all.get(row[0])
        if cookbook:
            cookbook.name = row[1]
            cookbook.author = row[2]
            cookbook.pub_date = row[3]
        else:
            date_values = [int(num) for num in row[3].split("/")]
            cookbook = cls(
                row[1], row[2], date_values[0], date_values[1], date_values[2]
            )
            cookbook.id = row[0]
            cls.all[cookbook.id] = cookbook
        return cookbook

    @classmethod
    def get_all(cls):
        """Return a list containing a Cookbook object per row in the table"""
        sql = """
            SELECT *
            FROM cookbooks
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Cookbook object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM cookbooks
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Cookbook object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM cookbooks
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def recipes(self):  # Returns recipes from current cookbook
        """Return list of recipes associated with current cookbook"""
        from models.recipe import Recipe

        sql = """
            SELECT * FROM recipes
            WHERE cookbook_id = ?
        """
        CURSOR.execute(
            sql,
            (self.id,),
        )

        rows = CURSOR.fetchall()
        return [Recipe.instance_from_db(row) for row in rows]
