# -*- coding: utf-8 -*-
"""
File name: db_view.py
Author: William Andersson
License: MIT License
Description: Open and manage database for NutriCalc
"""
from PySide6.QtWidgets import QTableWidgetItem, QDialog
from database import Ui_Dialog
def manage_db(self):
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
        self.db.add_btn.setText("Update")
            
    def remove_product():
        toDel = self.db.db_title.text()
        if toDel != "":
            print("Removed item:", self.db.db_title.text())
            self.cursor.execute(f"DELETE FROM products WHERE Product = '{toDel}'")
            self.upd_combobox()
            update_table()
            self.database.commit()
            self.db.add_btn.setText("Add")
            self.db.rm_btn.setEnabled(False)
        else:
            print("No product selected for removal.")
            self.info_msg("No product selected for removal.")
                
    def add_product():
        if self.db.add_btn.text() == "Update":
            remove_product()
        Names = self.cursor.execute(f"SELECT Product FROM products WHERE Product='{self.db.db_title.text().lower()}'").fetchall()
        if self.db.db_title.text().lower() == "":
            self.db.db_title.setText("")
            self.info_msg("Missing title for product.")
        elif len(Names) > 0 and self.db.db_title.text().lower() == Names[0][0]:
            self.db.db_title.setText("")
            self.info_msg("Product already exists in database.")
        else:
            new = (self.db.db_title.text().lower(), self.db.db_fat.value(), self.db.db_satfat.value(), self.db.db_carb.value(), self.db.db_sugar.value(), self.db.db_prot.value(), self.db.db_salt.value(), self.db.db_fiber.value())
            self.db.db_title.setText("")
            self.cursor.execute(f"INSERT INTO products VALUES(?, ?, ?, ?, ?, ?, ?, ?)", new)
            self.upd_combobox()
            update_table()
            self.database.commit()
            reset_input()
        
    def update_table():
        categories = ["", "Fat", "Saturated fat", "Carbohydrate", "Sugar", "Protein", "Salt", "Fiber"]
        rowcount = self.cursor.execute("SELECT COUNT(*) FROM products").fetchone()[0]
        self.cursor.execute("SELECT * FROM products")
        self.db.table.clear()
        self.db.table.setRowCount(rowcount)
        self.db.table.setColumnCount(8)
        self.db.table.setHorizontalHeaderLabels(categories)
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
        self.db.add_btn.setText("Add")
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
