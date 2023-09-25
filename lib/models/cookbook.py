from models.__init__ import CURSOR, CONN

class Cookbook:
    all = {}

    def __init__(self, name, author, year, month, day, id=None):
        self.id = id
        self.name = name
        self.author = author
        self.year = year  # Integer for year
        self.month = month  # Integer for month
        self.day = day  # Integer for day

    def __repr__(self):
        return f"<Cookbook {self.id}: {self.name}, {self.author}, {self.pub_date}>" # Year month and day gets set to pub_date on line 39

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
        
    @property                                                       # Creates pub_date property and sets the YYYY/MM/DD format
    def pub_date(self):
        return f"{self._year:04d}/{self._month:02d}/{self._day:02d}"

    @pub_date.setter                                                # Checks all integers and formats with "/" or throws error
    def pub_date(self, date_str):
        year, month, day = map(int, date_str.split('/'))
        
        if isinstance(year, int) and isinstance(month, int) and isinstance(day, int):
            self._year = year
            self._month = month
            self._day = day
        else:
            raise Exception("Year, month, and day must be integers")