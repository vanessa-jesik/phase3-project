import sqlite3

CONN = sqlite3.connect("publisher.db")
CURSOR = CONN.cursor()
