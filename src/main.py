# SPDX-License-Identifier: MIT
# Copyright 2024, The NutriCalc developers
# Author: William Andersson <contact.kiwipy@gmail.com>

import sys

from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QTableWidgetItem, QDialog
from PySide6.QtCore import QFile, QTranslator, QLocale, QLibraryInfo

import resources
import label
from database import Database
from local_path import local_path_for
from MainWindow import Ui_MainWindow
from BaseWindow import Ui_Dialog

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(":/AppIcon.png"))
        self.left_label = QLabel(f"{self.tr('  Version')}: {kwargs['version']}")
        self.right_label = QLabel("<a href=\"https://github.com/kiwipy/nutricalc\">NutriCalc on GitHub</a>")
        self.right_label.setOpenExternalLinks(True)
        self.ui.statusBar.addWidget(self.left_label)
        self.ui.statusBar.addPermanentWidget(self.right_label)
        self.SpinBox_tuple = (self.ui.spin_1, self.ui.spin_2, self.ui.spin_3,
                              self.ui.spin_4, self.ui.spin_5, self.ui.spin_6,
                              self.ui.spin_7, self.ui.spin_8, self.ui.spin_9,
                              self.ui.spin_10, self.ui.spin_11, self.ui.spin_12)
        self.ComboBox_tuple = (self.ui.combo_1, self.ui.combo_2, self.ui.combo_3,
                               self.ui.combo_4, self.ui.combo_5, self.ui.combo_6,
                               self.ui.combo_7, self.ui.combo_8, self.ui.combo_9,
                               self.ui.combo_10, self.ui.combo_11, self.ui.combo_12)
        #self.db_categories = (self.tr("Product"), self.tr("Fat"), self.tr("Saturates"),
        #                      self.tr("Carbohydrate"), self.tr("Sugars"),
        #                      self.tr("Protein"), self.tr("Salt"), self.tr("Fiber"))

        for index in range(len(self.ComboBox_tuple)):
        # Activate QSpinBox when corresponding QComboBox is used.
        # Also activate the next QComboBox.
        # (index) must be passed to lambda otherwise it's inherited from __init__
            self.ComboBox_tuple[index].activated.connect(lambda checked, index=index: self.SpinBox_tuple[index].setEnabled(True))
            if index+1 != len(self.ComboBox_tuple):
                self.ComboBox_tuple[index].activated.connect(lambda checked, index=index: self.ComboBox_tuple[index+1].setEnabled(True))

        self.ui.clear_btn.clicked.connect(self.clear)
        self.ui.save_btn.clicked.connect(self.add_product)
        self.ui.base_btn.clicked.connect(self.manage_db)


        try:
            self.db_store = local_path_for(kwargs['application']) / "default.db"
            self.database = Database(self.db_store)
        except Exception:
            self.err_msg(self.tr("Could not load database."))
        
        for spinbox in self.SpinBox_tuple:
        # When the value off all QSpinBox changes.
            spinbox.valueChanged.connect(lambda: label.update_values(self))
        
        self.upd_combobox()
    
    def upd_combobox(self):
        for combobox in self.ComboBox_tuple:
        # Populate all QComboBox with products from database.
            combobox.clear()
            for product in self.database.get_items():
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


    def add_product(self):
        new_item = (self.ui.title.text().lower(), self.ui.fat_value.text()[:-1],
                    self.ui.sat_fat_value.text()[:-1], self.ui.carb_value.text()[:-1],
                    self.ui.sugar_value.text()[:-1], self.ui.protein_value.text()[:-1],
                    self.ui.salt_value.text()[:-1], self.ui.fiber_value.text()[:-1])
        try:
            self.database.add(new_item)
        except NameError:
            self.info_msg(self.tr("Missing title for product."))
        except ValueError:
            self.info_msg(self.tr("Product already exists in database."))
        else:
            self.upd_combobox()
            self.clear()
            self.ui.title.setText("")
            self.ui.title.setPlaceholderText(self.tr("Title"))


    def manage_db(self):
        def update_table():
            categories = [self.tr("Product"), self.tr("Fat"), self.tr("Saturates"),
                          self.tr("Carbohydrate"), self.tr("Sugars"),
                          self.tr("Protein"), self.tr("Salt"), self.tr("Fiber")]
            rowcount = self.database.get_rowcount()
            self.db.table.clear()
            self.db.table.setRowCount(rowcount)
            self.db.table.setColumnCount(len(categories))
            self.db.table.horizontalHeaderItem(0)
            self.db.table.setHorizontalHeaderLabels(categories)
            self.db.table.setColumnWidth(0, 150)
            for row, form in enumerate(self.database.select_all()):
                for column, item in enumerate(form):
                    self.db.table.setItem(row, column, QTableWidgetItem(str(item)))

        def add_product():
            new_item = (self.db.db_title.text().lower(), self.db.db_fat.value(),
                        self.db.db_satfat.value(), self.db.db_carb.value(),
                        self.db.db_sugar.value(), self.db.db_prot.value(),
                        self.db.db_salt.value(), self.db.db_fiber.value())
            if self.db.add_btn.text() == self.tr("Update"):
                remove_product()

            try:
                self.database.add(new_item)
            except NameError:
                self.info_msg(self.tr("Missing title for product."))
            except ValueError:
                self.info_msg(self.tr("Product already exists in database."))
            else:
                self.db.db_title.setText("")
                self.upd_combobox()
                update_table()
                reset_input()


        def edit_product(row, column):
            select = self.database.select_row(row)
            self.db.table.selectRow(row)
            self.db.db_title.setText(select[0])
            self.db.db_fat.setValue(select[1])
            self.db.db_satfat.setValue(select[2])
            self.db.db_carb.setValue(select[3])
            self.db.db_sugar.setValue(select[4])
            self.db.db_prot.setValue(select[5])
            self.db.db_salt.setValue(select[6])
            self.db.db_fiber.setValue(select[7])
            self.db.rm_btn.setEnabled(True)
            self.db.add_btn.setText(self.tr("Update"))

        def remove_product():
            try:
                self.database.remove(self.db.db_title.text())
            except NameError:
                self.info_msg(self.tr("No product selected for removal."))
            else:
                update_table()
                self.upd_combobox()
                self.db.add_btn.setText(self.tr("Add"))
                self.db.rm_btn.setEnabled(False)

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


    def clear(self):
    # Clear value in all QSpinBox, QComboBox, QLabel and QLineEdit (total vikt)
        for index in range(len(self.ComboBox_tuple)):
            self.SpinBox_tuple[index].setValue(0)
            self.SpinBox_tuple[index].setEnabled(False)
            self.ComboBox_tuple[index].setCurrentIndex(-1)
            if index+1 != len(self.ComboBox_tuple):
                self.ComboBox_tuple[index+1].setEnabled(False)

        self.ui.fat_value.setText(f"0g")
        self.ui.sat_fat_value.setText(f"0g")
        self.ui.carb_value.setText(f"0g")
        self.ui.sugar_value.setText(f"0g")
        self.ui.protein_value.setText(f"0g")
        self.ui.salt_value.setText(f"0g")
        self.ui.fiber_value.setText(f"0g")
        self.ui.energy_value.setText(f"0kcal/0kj")

def main(VERSION, APPLICATION):
    app = QApplication(sys.argv)
    
    # load translation from qt
    path = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    translator = QTranslator(app)
    if translator.load(QLocale.system(), 'qtbase', '_', path):
        app.installTranslator(translator)
    # load translation from resource
    translator = QTranslator(app)
    path = ':'
    if translator.load(QLocale.system(), path):
        app.installTranslator(translator)

    window = MainWindow(version=VERSION, application=APPLICATION)
    window.show()
    sys.exit(app.exec())
