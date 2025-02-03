# SPDX-License-Identifier: MIT
# Copyright 2024, The NutriCalc developers
# Author: William Andersson <contact.kiwipy@gmail.com>

import sqlite3

class Database():
    def __init__(self, db_path):
        self.db_path = db_path
        self.NEW_DB = """CREATE TABLE IF NOT EXISTS products (
                         Product TEXT PRIMARY KEY,
                         Fat NUMERIC,
                         Saturated NUMERIC,
                         Carbs NUMERIC,
                         Sugar NUMERIC,
                         Protein NUMERIC,
                         Salt NUMERIC,
                         Fiber NUMERIC);"""

        if not self.db_path.exists():
            self.database = sqlite3.connect(self.db_path)
            self.cursor = self.database.cursor()
            self.cursor.execute(self.NEW_DB)
            self.database.commit()
        else:
            self.database = sqlite3.connect(self.db_path)
            self.cursor = self.database.cursor()

    def add(self, values):
    # Save new product to database
        Names = self.cursor.execute(f"SELECT Product FROM products WHERE Product='{values[0]}'").fetchall()
        if values[0] == "":
            raise NameError("Missing title for product.")
        elif len(Names) > 0 and values[0] == Names[0][0]:
            raise ValueError("Product already exists in database.")
        else:
            self.cursor.execute(f"INSERT INTO products VALUES(?, ?, ?, ?, ?, ?, ?, ?)", values)
            self.database.commit()

    def remove(self, item):
        if item != "":
            self.cursor.execute(f"DELETE FROM products WHERE Product = '{item}'")
            self.database.commit()
        else:
            raise NameError("No product selected for removal.")

    def get_items(self):
        return self.cursor.execute("SELECT Product FROM products")

    def get_item(self, item):
        return self.cursor.execute(f"SELECT * FROM products WHERE Product='{item}'").fetchall()

    def get_rowcount(self):
        rowcount = self.cursor.execute("SELECT COUNT(*) FROM products").fetchone()[0]
        return rowcount

    def select_all(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor

    def select_row(self, row):
        return self.cursor.execute(f"SELECT * FROM products LIMIT 1 OFFSET {row}").fetchall()
