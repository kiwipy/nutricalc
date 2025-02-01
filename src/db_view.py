# SPDX-License-Identifier: MIT
# Copyright 2024, The NutriCalc developers
# Author: William Andersson <contact.kiwipy@gmail.com>

import sqlite3
from PySide6.QtWidgets import QTableWidgetItem, QDialog
from database import Ui_Dialog

NEW_DB = """CREATE TABLE IF NOT EXISTS products (
            Product TEXT PRIMARY KEY,
            Fat NUMERIC,
            Saturated NUMERIC,
            Carbs NUMERIC,
            Sugar NUMERIC,
            Protein NUMERIC,
            Salt NUMERIC,
            Fiber NUMERIC);"""

def db_load(self):
    if self.db_store != None:
        if not self.db_store.exists():
            try:
                self.database = sqlite3.connect(self.db_store)
                self.cursor = self.database.cursor()
                self.cursor.execute(NEW_DB)
                self.database.commit()
            except Exception as e:
                print(f"Error: {e}")
                self.err_msg(self.tr("Could not create database."))
        else:
            try:
                self.database = sqlite3.connect(self.db_store)
                self.cursor = self.database.cursor()
            except Exception as e:
                print(f"Error: {e}")
                self.err_msg(self.tr("Could not load database."))
    else:
        self.err_msg(self.tr("No path for database."))

def db_save(self):
    # Save new product to database
    Names = self.cursor.execute(f"SELECT Product FROM products WHERE Product='{self.ui.title.text().lower()}'").fetchall()
    if self.ui.title.text().lower() == "":
        self.info_msg(self.tr("Missing title for product."))
    elif len(Names) > 0 and self.ui.title.text().lower() == Names[0][0]:
        self.info_msg(self.tr("Product already exists in database."))
    else:
        title = self.ui.title.text().lower()
        fat = self.ui.fat_value.text()[:-1]
        satfat = self.ui.sat_fat_value.text()[:-1]
        carbs = self.ui.carb_value.text()[:-1]
        sugar = self.ui.sugar_value.text()[:-1]
        prot = self.ui.protein_value.text()[:-1]
        salt = self.ui.salt_value.text()[:-1]
        fiber = self.ui.fiber_value.text()[:-1]
        self.cursor.execute(f"INSERT INTO products VALUES (\"{title}\", {fat}, {satfat}, {carbs}, {sugar}, {prot}, {salt}, {fiber})")
        self.database.commit()

        for combobox in self.ComboBox_tuple:
            combobox.addItem(self.ui.title.text().lower())
        self.clear()
    self.ui.title.setText("")
    self.ui.title.setPlaceholderText(self.tr("Title"))

def db_manage(self):
    def edit_product(row, column):
        select = self.cursor.execute(f"SELECT * FROM products LIMIT 1 OFFSET {row}").fetchall()
        self.db.table.selectRow(row)
        self.db.db_title.setText(select[0][0])
        self.db.db_fat.setValue(select[0][1])
        self.db.db_satfat.setValue(select[0][2])
        self.db.db_carb.setValue(select[0][3])
        self.db.db_sugar.setValue(select[0][4])
        self.db.db_prot.setValue(select[0][5])
        self.db.db_salt.setValue(select[0][6])
        self.db.db_fiber.setValue(select[0][7])
        self.db.rm_btn.setEnabled(True)
        self.db.add_btn.setText(self.tr("Update"))
            
    def remove_product():
        toDel = self.db.db_title.text()
        if toDel != "":
            self.cursor.execute(f"DELETE FROM products WHERE Product = '{toDel}'")
            self.upd_combobox()
            update_table()
            self.database.commit()
            self.db.add_btn.setText(self.tr("Add"))
            self.db.rm_btn.setEnabled(False)
        else:
            self.info_msg("No product selected for removal.")
                
    def add_product():
        if self.db.add_btn.text() == self.tr("Update"):
                remove_product()
        Names = self.cursor.execute(f"SELECT Product FROM products WHERE Product='{self.db.db_title.text().lower()}'").fetchall()
        if self.db.db_title.text().lower() == "":
            self.db.db_title.setText("")
            self.info_msg(self.tr("Missing title for product."))
        elif len(Names) > 0 and self.db.db_title.text().lower() == Names[0][0]:
            self.db.db_title.setText("")
            self.info_msg(self.tr("Product already exists in database."))
        else:
            new = (self.db.db_title.text().lower(), self.db.db_fat.value(), self.db.db_satfat.value(), self.db.db_carb.value(), self.db.db_sugar.value(), self.db.db_prot.value(), self.db.db_salt.value(), self.db.db_fiber.value())
            self.db.db_title.setText("")
            self.cursor.execute(f"INSERT INTO products VALUES(?, ?, ?, ?, ?, ?, ?, ?)", new)
            self.upd_combobox()
            update_table()
            self.database.commit()
            reset_input()

    def update_table():
        # --- Moved to main.py for translation purposes ---
        #
        # categories = [self.tr("Product"), self.tr("Fat"), self.tr("Saturates"),
        #               self.tr("Carbohydrate"), self.tr("Sugars"),
        #               self.tr("Protein"), self.tr("Salt"), self.tr("Fiber")]
        #
        rowcount = self.cursor.execute("SELECT COUNT(*) FROM products").fetchone()[0]
        self.cursor.execute("SELECT * FROM products")
        self.db.table.clear()
        self.db.table.setRowCount(rowcount)
        self.db.table.setColumnCount(8)
        self.db.table.horizontalHeaderItem(0)
        self.db.table.setHorizontalHeaderLabels(self.db_categories)
        self.db.table.setColumnWidth(0, 150)
        for row, form in enumerate(self.cursor):
            for column, item in enumerate(form):
                self.db.table.setItem(row, column, QTableWidgetItem(str(item)))
                
    def reset_input():
        self.db.db_title.setText("")
        self.db.db_fat.setValue(0)
        self.db.db_satfat.setValue(0)
        self.db.db_carb.setValue(0)
        self.db.db_sugar.setValue(0)
        self.db.db_prot.setValue(0)
        self.db.db_salt.setValue(0)
        self.db.db_fiber.setValue(0)
        self.db.add_btn.setText(self.tr("Add"))
        self.db.rm_btn.setEnabled(False)
                    
    self.dialog = QDialog(self)
    self.db = Ui_Dialog()
    self.db.setupUi(self.dialog)
    update_table()
    reset_input()
    self.dialog.show()
    self.db.table.cellClicked.connect(edit_product)
    self.db.rm_btn.clicked.connect(remove_product)
    self.db.add_btn.clicked.connect(add_product)
