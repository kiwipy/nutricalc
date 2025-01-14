# -*- coding: utf-8 -*-
"""
File name: main.py
Author: William Andersson
License: MIT License
Description: Main application code for NutriCalc
"""
import sys
import sqlite3
import shutil
from PySide6.QtWidgets import QApplication, QMainWindow, QStyleFactory, QMessageBox, QLabel
from PySide6.QtCore import QFile
from PySide6 import QtGui
from window import Ui_MainWindow
from label_view import update_label_values
from db_view import manage_db 

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.right_label = QLabel(f"Version: {kwargs['version']}")
        self.ui.statusBar.addPermanentWidget(self.right_label)
        self.SpinBox_tuple = (self.ui.spin_1, self.ui.spin_2, self.ui.spin_3,
                              self.ui.spin_4, self.ui.spin_5, self.ui.spin_6,
                              self.ui.spin_7, self.ui.spin_8, self.ui.spin_9,
                              self.ui.spin_10, self.ui.spin_11, self.ui.spin_12)
        self.ComboBox_tuple = (self.ui.combo_1, self.ui.combo_2, self.ui.combo_3,
                               self.ui.combo_4, self.ui.combo_5, self.ui.combo_6,
                               self.ui.combo_7, self.ui.combo_8, self.ui.combo_9,
                               self.ui.combo_10, self.ui.combo_11, self.ui.combo_12)

        for index in range(len(self.ComboBox_tuple)):
        # Activate QSpinBox and the next QComboBox when corresponding QComboBox is used.
            self.ComboBox_tuple[index].activated.connect(lambda checked, index=index: self.SpinBox_tuple[index].setEnabled(True))
            if index+1 != len(self.ComboBox_tuple):
                self.ComboBox_tuple[index].activated.connect(lambda checked, index=index: self.ComboBox_tuple[index+1].setEnabled(True))

        self.ui.clear_btn.clicked.connect(self.clear)
        self.ui.save_btn.clicked.connect(self.save)
        self.ui.base_btn.clicked.connect(lambda: manage_db(self))
        
        self.database = sqlite3.connect("default.db")
        self.cursor = self.database.cursor()
        
        for spinbox in self.SpinBox_tuple:
        # When the value off all QSpinBox changes.
            spinbox.valueChanged.connect(lambda: update_label_values(self))
        
        self.upd_combobox()
    
    def upd_combobox(self):
        for combobox in self.ComboBox_tuple:
        # Populate all QComboBox with products from database.
            combobox.clear()
            for product in self.cursor.execute("SELECT Product FROM products"):
                combobox.addItem(product[0])
            self.clear()
        
    def err_msg(self, info_str):
        self.msgBox = QMessageBox(self)
        self.msgBox.setIcon(QMessageBox.Critical)
        self.msgBox.setText("<b>Error!</b>")
        self.msgBox.setInformativeText(info_str)
        self.msgBox.setStandardButtons(QMessageBox.Close)
        sys.exit(self.msgBox.exec())

    def info_msg(self, info_str):
        self.msgBox = QMessageBox(self)
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText("<b>Information</b>")
        self.msgBox.setInformativeText(info_str)
        self.msgBox.setStandardButtons(QMessageBox.Ok)
        self.msgBox.exec()
        
    def clear(self):
    # Clear value in all QSpinBox, QComboBox, QLabel and QLineEdit (total vikt)
        for index in range(len(self.ComboBox_tuple)):
            self.SpinBox_tuple[index].setValue(0)
            self.SpinBox_tuple[index].setEnabled(False)
            self.ComboBox_tuple[index].setCurrentIndex(-1)
            if index+1 != len(self.ComboBox_tuple):
                self.ComboBox_tuple[index+1].setEnabled(False)

        self.ui.fat_value.setText(f"g")
        self.ui.sat_fat_value.setText(f"g")
        self.ui.carb_value.setText(f"g")
        self.ui.sugar_value.setText(f"g")
        self.ui.protein_value.setText(f"g")
        self.ui.salt_value.setText(f"g")
        self.ui.fiber_value.setText(f"g")
        self.ui.energy_value.setText(f"kcal/kj")
    
    def save(self):
    # Save new product to database
        Names = self.cursor.execute(f"SELECT Product FROM products WHERE Product='{self.ui.title.text().lower()}'").fetchall()
        if self.ui.title.text().lower() == "":
            self.info_msg("Missing title.")
        elif len(Names) > 0 and self.ui.title.text().lower() == Names[0][0]:
            self.info_msg("Product already exists in database.")
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
        self.ui.title.setPlaceholderText("Titel")

def main(VERSION):
    app = QApplication(sys.argv)
    window = MainWindow(version=VERSION)
    window.show()
    sys.exit(app.exec())
