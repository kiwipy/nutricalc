# SPDX-License-Identifier: MIT
# Copyright 2024, The NutriCalc developers
# Author: William Andersson <contact.kiwipy@gmail.com>

import sys

from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel
from PySide6.QtCore import QFile, QTranslator, QLocale, QLibraryInfo

import resources
import db_view
from window import Ui_MainWindow
from label_view import update_label_values
from app_path import local_path_for

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
        self.db_categories = (self.tr("Product"), self.tr("Fat"), self.tr("Saturates"),
                              self.tr("Carbohydrate"), self.tr("Sugars"),
                              self.tr("Protein"), self.tr("Salt"), self.tr("Fiber"))

        for index in range(len(self.ComboBox_tuple)):
        # Activate QSpinBox when corresponding QComboBox is used.
        # Also activate the next QComboBox.
        # (index) must be passed to lambda otherwise it's inherited from __init__
            self.ComboBox_tuple[index].activated.connect(lambda checked, index=index: self.SpinBox_tuple[index].setEnabled(True))
            if index+1 != len(self.ComboBox_tuple):
                self.ComboBox_tuple[index].activated.connect(lambda checked, index=index: self.ComboBox_tuple[index+1].setEnabled(True))

        self.ui.clear_btn.clicked.connect(self.clear)
        self.ui.save_btn.clicked.connect(lambda: db_view.db_save(self))
        self.ui.base_btn.clicked.connect(lambda: db_view.db_manage(self))

        self.db_store = local_path_for(kwargs['application']) / "default.db"
        db_view.db_load(self)
        
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
