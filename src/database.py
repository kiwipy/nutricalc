# -*- coding: utf-8 -*-
"""
File name: database.py
Author: William Andersson
License: MIT License
Description: Database window for NutriCalc
"""
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QDoubleSpinBox,
    QFrame, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(925, 652)
        self.verticalLayout_11 = QVBoxLayout(Dialog)
        self.verticalLayout_11.setSpacing(25)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.group1 = QGroupBox(Dialog)
        self.group1.setObjectName(u"group1")
        font = QFont()
        font.setPointSize(11)
        self.group1.setFont(font)
        self.verticalLayout = QVBoxLayout(self.group1)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.table = QTableWidget(self.group1)
        self.table.setObjectName(u"table")
        self.table.setMinimumSize(QSize(890, 400))
        self.table.setMaximumSize(QSize(16777215, 16777215))
        self.table.setFont(font)
        self.table.setFrameShape(QFrame.Shape.StyledPanel)
        self.table.setFrameShadow(QFrame.Shadow.Sunken)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.verticalLayout.addWidget(self.table)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_11.addWidget(self.group1)

        self.group2 = QGroupBox(Dialog)
        self.group2.setObjectName(u"group2")
        self.group2.setFont(font)
        self.verticalLayout_10 = QVBoxLayout(self.group2)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.group2)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.db_title = QLineEdit(self.group2)
        self.db_title.setObjectName(u"db_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.db_title.sizePolicy().hasHeightForWidth())
        self.db_title.setSizePolicy(sizePolicy)
        self.db_title.setMinimumSize(QSize(120, 0))
        self.db_title.setMaximumSize(QSize(150, 16777215))
        self.db_title.setFont(font)

        self.verticalLayout_2.addWidget(self.db_title)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.group2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2)

        self.db_fat = QDoubleSpinBox(self.group2)
        self.db_fat.setObjectName(u"db_fat")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.db_fat.sizePolicy().hasHeightForWidth())
        self.db_fat.setSizePolicy(sizePolicy1)
        self.db_fat.setMinimumSize(QSize(80, 0))
        self.db_fat.setFont(font)
        self.db_fat.setDecimals(1)
        self.db_fat.setSingleStep(0.100000000000000)

        self.verticalLayout_3.addWidget(self.db_fat)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.group2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_4.addWidget(self.label_3)

        self.db_satfat = QDoubleSpinBox(self.group2)
        self.db_satfat.setObjectName(u"db_satfat")
        sizePolicy1.setHeightForWidth(self.db_satfat.sizePolicy().hasHeightForWidth())
        self.db_satfat.setSizePolicy(sizePolicy1)
        self.db_satfat.setMinimumSize(QSize(80, 0))
        self.db_satfat.setFont(font)
        self.db_satfat.setDecimals(1)
        self.db_satfat.setSingleStep(0.100000000000000)

        self.verticalLayout_4.addWidget(self.db_satfat)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.group2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_5.addWidget(self.label_4)

        self.db_carb = QDoubleSpinBox(self.group2)
        self.db_carb.setObjectName(u"db_carb")
        sizePolicy1.setHeightForWidth(self.db_carb.sizePolicy().hasHeightForWidth())
        self.db_carb.setSizePolicy(sizePolicy1)
        self.db_carb.setMinimumSize(QSize(80, 0))
        self.db_carb.setFont(font)
        self.db_carb.setDecimals(1)
        self.db_carb.setSingleStep(0.100000000000000)

        self.verticalLayout_5.addWidget(self.db_carb)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.group2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_6.addWidget(self.label_5)

        self.db_sugar = QDoubleSpinBox(self.group2)
        self.db_sugar.setObjectName(u"db_sugar")
        sizePolicy1.setHeightForWidth(self.db_sugar.sizePolicy().hasHeightForWidth())
        self.db_sugar.setSizePolicy(sizePolicy1)
        self.db_sugar.setMinimumSize(QSize(80, 0))
        self.db_sugar.setFont(font)
        self.db_sugar.setDecimals(1)
        self.db_sugar.setSingleStep(0.100000000000000)

        self.verticalLayout_6.addWidget(self.db_sugar)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.group2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_7.addWidget(self.label_6)

        self.db_prot = QDoubleSpinBox(self.group2)
        self.db_prot.setObjectName(u"db_prot")
        sizePolicy1.setHeightForWidth(self.db_prot.sizePolicy().hasHeightForWidth())
        self.db_prot.setSizePolicy(sizePolicy1)
        self.db_prot.setMinimumSize(QSize(80, 0))
        self.db_prot.setFont(font)
        self.db_prot.setDecimals(1)
        self.db_prot.setSingleStep(0.100000000000000)

        self.verticalLayout_7.addWidget(self.db_prot)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.group2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_8.addWidget(self.label_7)

        self.db_salt = QDoubleSpinBox(self.group2)
        self.db_salt.setObjectName(u"db_salt")
        sizePolicy1.setHeightForWidth(self.db_salt.sizePolicy().hasHeightForWidth())
        self.db_salt.setSizePolicy(sizePolicy1)
        self.db_salt.setMinimumSize(QSize(80, 0))
        self.db_salt.setFont(font)
        self.db_salt.setDecimals(1)
        self.db_salt.setSingleStep(0.100000000000000)

        self.verticalLayout_8.addWidget(self.db_salt)


        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_8 = QLabel(self.group2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_9.addWidget(self.label_8)

        self.db_fiber = QDoubleSpinBox(self.group2)
        self.db_fiber.setObjectName(u"db_fiber")
        sizePolicy1.setHeightForWidth(self.db_fiber.sizePolicy().hasHeightForWidth())
        self.db_fiber.setSizePolicy(sizePolicy1)
        self.db_fiber.setMinimumSize(QSize(80, 0))
        self.db_fiber.setFont(font)
        self.db_fiber.setDecimals(1)
        self.db_fiber.setSingleStep(0.100000000000000)

        self.verticalLayout_9.addWidget(self.db_fiber)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)


        self.verticalLayout_10.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(748, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.rm_btn = QPushButton(self.group2)
        self.rm_btn.setObjectName(u"rm_btn")
        self.rm_btn.setMinimumSize(QSize(95, 0))
        self.rm_btn.setMaximumSize(QSize(95, 16777215))
        self.rm_btn.setFont(font)

        self.horizontalLayout_3.addWidget(self.rm_btn)

        self.add_btn = QPushButton(self.group2)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setMinimumSize(QSize(95, 0))
        self.add_btn.setMaximumSize(QSize(95, 16777215))
        self.add_btn.setFont(font)

        self.horizontalLayout_3.addWidget(self.add_btn)


        self.verticalLayout_10.addLayout(self.horizontalLayout_3)


        self.verticalLayout_11.addWidget(self.group2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Database", None))
        self.group1.setTitle(QCoreApplication.translate("Dialog", u"Database", None))
        self.group2.setTitle(QCoreApplication.translate("Dialog", u"Add product", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Product", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Fat", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Saturated fat", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Carbohydrate", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Sugar", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Protein", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Salt", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Fiber", None))
        self.rm_btn.setText(QCoreApplication.translate("Dialog", u"Remove", None))
        self.add_btn.setText(QCoreApplication.translate("Dialog", u"Add", None))
    # retranslateUi

