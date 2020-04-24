from sqlite3 import *


class Mosque:

    """Mosque class which will be act as a database and a way to manipulate its data"""

    # initializer will make the connection to the database
    def __init__(self):
        self.conn = connect(':memory:')
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute("""CREATE TABLE mosques (
                                 id integer,
                                 name text,
                                 type text,
                                 address text,
                                 coordinates text,
                                 imam_name text
                                 )""")
        except:
            pass

        self.conn.commit()

    # returns all database records
    def display(self):
        self.cursor.execute("SELECT * FROM mosques")
        return self.cursor.fetchall()

    # inserts a record to the database with the given arguments
    def insert(self, id, name, type, address, coordinates, imam_name):
        self.cursor.execute("INSERT INTO mosques VALUES (?, ?, ?, ?, ?, ?)",
                            (id, name, type, address, coordinates, imam_name))
        self.conn.commit()

    # deletes a record from the database with the give ID
    def delete(self, id):
        self.cursor.execute("DELETE FROM mosques WHERE id=?", (id,))
        self.conn.commit()

    # returns a record with a given mosque name
    def search(self, name):
        self.cursor.execute("SELECT * FROM mosques WHERE name=?", (name,))
        return self.cursor.fetchone()

    # change the imam name given a correct mosque name
    def update(self, name, imam_name):
        self.cursor.execute("""UPDATE mosques SET imam_name=? 
                            WHERE name=?""", (imam_name, name))
        self.conn.commit()

    # close the connection to the database
    def __del__(self):
        self.conn.close()
