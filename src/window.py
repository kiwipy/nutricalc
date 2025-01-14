# -*- coding: utf-8 -*-
"""
File name: window.py
Author: William Andersson
License: MIT License
Description: Main window for NutriCalc
"""
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 578))
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(25)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(360, 560))
        font = QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.product_label = QLabel(self.groupBox)
        self.product_label.setObjectName(u"product_label")
        self.product_label.setFont(font)

        self.horizontalLayout_13.addWidget(self.product_label)

        self.horizontalSpacer = QSpacerItem(170, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)

        self.amount_label = QLabel(self.groupBox)
        self.amount_label.setObjectName(u"amount_label")
        self.amount_label.setFont(font)

        self.horizontalLayout_13.addWidget(self.amount_label)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.combo_1 = QComboBox(self.groupBox)
        self.combo_1.setObjectName(u"combo_1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_1.sizePolicy().hasHeightForWidth())
        self.combo_1.setSizePolicy(sizePolicy)
        self.combo_1.setMinimumSize(QSize(200, 0))
        self.combo_1.setFont(font)
        self.combo_1.setStyleSheet(u"QComboBox { combobox-popup: 0; }")
        self.combo_1.setMaxVisibleItems(20)

        self.horizontalLayout.addWidget(self.combo_1)

        self.spin_1 = QSpinBox(self.groupBox)
        self.spin_1.setObjectName(u"spin_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spin_1.sizePolicy().hasHeightForWidth())
        self.spin_1.setSizePolicy(sizePolicy1)
        self.spin_1.setMinimumSize(QSize(100, 0))
        self.spin_1.setFont(font)
        self.spin_1.setMinimum(0)
        self.spin_1.setMaximum(999999)
        self.spin_1.setSingleStep(1)
        self.spin_1.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_1.setValue(0)
        self.spin_1.setDisplayIntegerBase(10)

        self.horizontalLayout.addWidget(self.spin_1)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.combo_2 = QComboBox(self.groupBox)
        self.combo_2.setObjectName(u"combo_2")
        sizePolicy.setHeightForWidth(self.combo_2.sizePolicy().hasHeightForWidth())
        self.combo_2.setSizePolicy(sizePolicy)
        self.combo_2.setMinimumSize(QSize(200, 0))
        self.combo_2.setFont(font)
        self.combo_2.setStyleSheet(u"QComboBox { combobox-popup: 0; }")
        self.combo_2.setMaxVisibleItems(20)

        self.horizontalLayout_2.addWidget(self.combo_2)

        self.spin_2 = QSpinBox(self.groupBox)
        self.spin_2.setObjectName(u"spin_2")
        sizePolicy1.setHeightForWidth(self.spin_2.sizePolicy().hasHeightForWidth())
        self.spin_2.setSizePolicy(sizePolicy1)
        self.spin_2.setMinimumSize(QSize(100, 0))
        self.spin_2.setFont(font)
        self.spin_2.setMinimum(0)
        self.spin_2.setMaximum(999999)
        self.spin_2.setSingleStep(1)
        self.spin_2.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_2.setValue(0)
        self.spin_2.setDisplayIntegerBase(10)

        self.horizontalLayout_2.addWidget(self.spin_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.combo_3 = QComboBox(self.groupBox)
        self.combo_3.setObjectName(u"combo_3")
        sizePolicy.setHeightForWidth(self.combo_3.sizePolicy().hasHeightForWidth())
        self.combo_3.setSizePolicy(sizePolicy)
        self.combo_3.setMinimumSize(QSize(200, 0))
        self.combo_3.setFont(font)
        self.combo_3.setStyleSheet(u"QComboBox { combobox-popup: 0; }")
        self.combo_3.setMaxVisibleItems(20)

        self.horizontalLayout_3.addWidget(self.combo_3)

        self.spin_3 = QSpinBox(self.groupBox)
        self.spin_3.setObjectName(u"spin_3")
        sizePolicy1.setHeightForWidth(self.spin_3.sizePolicy().hasHeightForWidth())
        self.spin_3.setSizePolicy(sizePolicy1)
        self.spin_3.setMinimumSize(QSize(100, 0))
        self.spin_3.setFont(font)
        self.spin_3.setMinimum(0)
        self.spin_3.setMaximum(999999)
        self.spin_3.setSingleStep(1)
        self.spin_3.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_3.setValue(0)
        self.spin_3.setDisplayIntegerBase(10)

        self.horizontalLayout_3.addWidget(self.spin_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.combo_4 = QComboBox(self.groupBox)
        self.combo_4.setObjectName(u"combo_4")
        sizePolicy.setHeightForWidth(self.combo_4.sizePolicy().hasHeightForWidth())
        self.combo_4.setSizePolicy(sizePolicy)
        self.combo_4.setMinimumSize(QSize(200, 0))
        self.combo_4.setFont(font)
        self.combo_4.setStyleSheet(u"QComboBox { combobox-popup: 0; }")
        self.combo_4.setMaxVisibleItems(20)

        self.horizontalLayout_4.addWidget(self.combo_4)

        self.spin_4 = QSpinBox(self.groupBox)
        self.spin_4.setObjectName(u"spin_4")
        sizePolicy1.setHeightForWidth(self.spin_4.sizePolicy().hasHeightForWidth())
        self.spin_4.setSizePolicy(sizePolicy1)
        self.spin_4.setMinimumSize(QSize(100, 0))
        self.spin_4.setFont(font)
        self.spin_4.setMinimum(0)
        self.spin_4.setMaximum(999999)
        self.spin_4.setSingleStep(1)
        self.spin_4.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_4.setValue(0)
        self.spin_4.setDisplayIntegerBase(10)

        self.horizontalLayout_4.addWidget(self.spin_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.combo_5 = QComboBox(self.groupBox)
        self.combo_5.setObjectName(u"combo_5")
        sizePolicy.setHeightForWidth(self.combo_5.sizePolicy().hasHeightForWidth())
        self.combo_5.setSizePolicy(sizePolicy)
        self.combo_5.setMinimumSize(QSize(200, 0))
        self.combo_5.setFont(font)
        self.combo_5.setStyleSheet(u"QComboBox { combobox-popup: 0; }")
        self.combo_5.setMaxVisibleItems(20)

        self.horizontalLayout_5.addWidget(self.combo_5)

        self.spin_5 = QSpinBox(self.groupBox)
        self.spin_5.setObjectName(u"spin_5")
        sizePolicy1.setHeightForWidth(self.spin_5.sizePolicy().hasHeightForWidth())
        self.spin_5.setSizePolicy(sizePolicy1)
        self.spin_5.setMinimumSize(QSize(100, 0))
        self.spin_5.setFont(font)
        self.spin_5.setMinimum(0)
        self.spin_5.setMaximum(999999)
        self.spin_5.setSingleStep(1)
        self.spin_5.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_5.setValue(0)
        self.spin_5.setDisplayIntegerBase(10)

        self.horizontalLayout_5.addWidget(self.spin_5)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.combo_6 = QComboBox(self.groupBox)
        self.combo_6.setObjectName(u"combo_6")
        sizePolicy.setHeightForWidth(self.combo_6.sizePolicy().hasHeightForWidth())
        self.combo_6.setSizePolicy(sizePolicy)
        self.combo_6.setMinimumSize(QSize(200, 0))
        self.combo_6.setFont(font)
        self.combo_6.setStyleSheet(u"QComboBox { combobox-popup: 0; }")
        self.combo_6.setMaxVisibleItems(20)

        self.horizontalLayout_6.addWidget(self.combo_6)

        self.spin_6 = QSpinBox(self.groupBox)
        self.spin_6.setObjectName(u"spin_6")
        sizePolicy1.setHeightForWidth(self.spin_6.sizePolicy().hasHeightForWidth())
        self.spin_6.setSizePolicy(sizePolicy1)
        self.spin_6.setMinimumSize(QSize(100, 0))
        self.spin_6.setFont(font)
        self.spin_6.setMinimum(0)
        self.spin_6.setMaximum(999999)
        self.spin_6.setSingleStep(1)
        self.spin_6.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_6.setValue(0)
        self.spin_6.setDisplayIntegerBase(10)

        self.horizontalLayout_6.addWidget(self.spin_6)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.combo_7 = QComboBox(self.groupBox)
        self.combo_7.setObjectName(u"combo_7")
        sizePolicy.setHeightForWidth(self.combo_7.sizePolicy().hasHeightForWidth())
        self.combo_7.setSizePolicy(sizePolicy)
        self.combo_7.setMinimumSize(QSize(200, 0))
        self.combo_7.setFont(font)
        self.combo_7.setStyleSheet(u"QComboBox { combobox-popup: 0; }")
        self.combo_7.setMaxVisibleItems(20)

        self.horizontalLayout_7.addWidget(self.combo_7)

        self.spin_7 = QSpinBox(self.groupBox)
        self.spin_7.setObjectName(u"spin_7")
        sizePolicy1.setHeightForWidth(self.spin_7.sizePolicy().hasHeightForWidth())
        self.spin_7.setSizePolicy(sizePolicy1)
        self.spin_7.setMinimumSize(QSize(100, 0))
        self.spin_7.setFont(font)
        self.spin_7.setMinimum(0)
        self.spin_7.setMaximum(999999)
        self.spin_7.setSingleStep(1)
        self.spin_7.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_7.setValue(0)
        self.spin_7.setDisplayIntegerBase(10)

        self.horizontalLayout_7.addWidget(self.spin_7)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.combo_8 = QComboBox(self.groupBox)
        self.combo_8.setObjectName(u"combo_8")
        sizePolicy.setHeightForWidth(self.combo_8.sizePolicy().hasHeightForWidth())
        self.combo_8.setSizePolicy(sizePolicy)
        self.combo_8.setMinimumSize(QSize(200, 0))
        self.combo_8.setFont(font)
        self.combo_8.setStyleSheet(u"QComboBox { combobox-popup: 0; }")
        self.combo_8.setMaxVisibleItems(20)

        self.horizontalLayout_8.addWidget(self.combo_8)

        self.spin_8 = QSpinBox(self.groupBox)
        self.spin_8.setObjectName(u"spin_8")
        sizePolicy1.setHeightForWidth(self.spin_8.sizePolicy().hasHeightForWidth())
        self.spin_8.setSizePolicy(sizePolicy1)
        self.spin_8.setMinimumSize(QSize(100, 0))
        self.spin_8.setFont(font)
        self.spin_8.setMinimum(0)
        self.spin_8.setMaximum(999999)
        self.spin_8.setSingleStep(1)
        self.spin_8.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_8.setValue(0)
        self.spin_8.setDisplayIntegerBase(10)

        self.horizontalLayout_8.addWidget(self.spin_8)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.combo_9 = QComboBox(self.groupBox)
        self.combo_9.setObjectName(u"combo_9")
        sizePolicy.setHeightForWidth(self.combo_9.sizePolicy().hasHeightForWidth())
        self.combo_9.setSizePolicy(sizePolicy)
        self.combo_9.setMinimumSize(QSize(200, 0))
        self.combo_9.setFont(font)
        self.combo_9.setStyleSheet(u"QComboBox { combobox-popup: 0; }")
        self.combo_9.setMaxVisibleItems(20)

        self.horizontalLayout_9.addWidget(self.combo_9)

        self.spin_9 = QSpinBox(self.groupBox)
        self.spin_9.setObjectName(u"spin_9")
        sizePolicy1.setHeightForWidth(self.spin_9.sizePolicy().hasHeightForWidth())
        self.spin_9.setSizePolicy(sizePolicy1)
        self.spin_9.setMinimumSize(QSize(100, 0))
        self.spin_9.setFont(font)
        self.spin_9.setMinimum(0)
        self.spin_9.setMaximum(999999)
        self.spin_9.setSingleStep(1)
        self.spin_9.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_9.setValue(0)
        self.spin_9.setDisplayIntegerBase(10)

        self.horizontalLayout_9.addWidget(self.spin_9)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.combo_10 = QComboBox(self.groupBox)
        self.combo_10.setObjectName(u"combo_10")
        sizePolicy.setHeightForWidth(self.combo_10.sizePolicy().hasHeightForWidth())
        self.combo_10.setSizePolicy(sizePolicy)
        self.combo_10.setMinimumSize(QSize(200, 0))
        self.combo_10.setFont(font)
        self.combo_10.setStyleSheet(u"QComboBox { combobox-popup: 0; }")
        self.combo_10.setMaxVisibleItems(20)

        self.horizontalLayout_10.addWidget(self.combo_10)

        self.spin_10 = QSpinBox(self.groupBox)
        self.spin_10.setObjectName(u"spin_10")
        sizePolicy1.setHeightForWidth(self.spin_10.sizePolicy().hasHeightForWidth())
        self.spin_10.setSizePolicy(sizePolicy1)
        self.spin_10.setMinimumSize(QSize(100, 0))
        self.spin_10.setFont(font)
        self.spin_10.setMinimum(0)
        self.spin_10.setMaximum(999999)
        self.spin_10.setSingleStep(1)
        self.spin_10.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_10.setValue(0)
        self.spin_10.setDisplayIntegerBase(10)

        self.horizontalLayout_10.addWidget(self.spin_10)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.combo_11 = QComboBox(self.groupBox)
        self.combo_11.setObjectName(u"combo_11")
        sizePolicy.setHeightForWidth(self.combo_11.sizePolicy().hasHeightForWidth())
        self.combo_11.setSizePolicy(sizePolicy)
        self.combo_11.setMinimumSize(QSize(200, 0))
        self.combo_11.setFont(font)
        self.combo_11.setStyleSheet(u"QComboBox { combobox-popup: 0; }")
        self.combo_11.setMaxVisibleItems(20)

        self.horizontalLayout_11.addWidget(self.combo_11)

        self.spin_11 = QSpinBox(self.groupBox)
        self.spin_11.setObjectName(u"spin_11")
        sizePolicy1.setHeightForWidth(self.spin_11.sizePolicy().hasHeightForWidth())
        self.spin_11.setSizePolicy(sizePolicy1)
        self.spin_11.setMinimumSize(QSize(100, 0))
        self.spin_11.setFont(font)
        self.spin_11.setMinimum(0)
        self.spin_11.setMaximum(999999)
        self.spin_11.setSingleStep(1)
        self.spin_11.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_11.setValue(0)
        self.spin_11.setDisplayIntegerBase(10)

        self.horizontalLayout_11.addWidget(self.spin_11)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.combo_12 = QComboBox(self.groupBox)
        self.combo_12.setObjectName(u"combo_12")
        sizePolicy.setHeightForWidth(self.combo_12.sizePolicy().hasHeightForWidth())
        self.combo_12.setSizePolicy(sizePolicy)
        self.combo_12.setMinimumSize(QSize(200, 0))
        self.combo_12.setFont(font)
        self.combo_12.setStyleSheet(u"QComboBox { combobox-popup: 0; }")
        self.combo_12.setMaxVisibleItems(20)

        self.horizontalLayout_12.addWidget(self.combo_12)

        self.spin_12 = QSpinBox(self.groupBox)
        self.spin_12.setObjectName(u"spin_12")
        sizePolicy1.setHeightForWidth(self.spin_12.sizePolicy().hasHeightForWidth())
        self.spin_12.setSizePolicy(sizePolicy1)
        self.spin_12.setMinimumSize(QSize(100, 0))
        self.spin_12.setFont(font)
        self.spin_12.setMinimum(0)
        self.spin_12.setMaximum(999999)
        self.spin_12.setSingleStep(1)
        self.spin_12.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_12.setValue(0)
        self.spin_12.setDisplayIntegerBase(10)

        self.horizontalLayout_12.addWidget(self.spin_12)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.clear_btn = QPushButton(self.groupBox)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setFont(font)

        self.verticalLayout.addWidget(self.clear_btn)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 2, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.fat_value = QLabel(self.groupBox_2)
        self.fat_value.setObjectName(u"fat_value")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        self.fat_value.setFont(font1)
        self.fat_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.fat_value, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.carb_value = QLabel(self.groupBox_2)
        self.carb_value.setObjectName(u"carb_value")
        self.carb_value.setFont(font1)
        self.carb_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.carb_value, 3, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.label_9.setFont(font2)

        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.sat_fat_value = QLabel(self.groupBox_2)
        self.sat_fat_value.setObjectName(u"sat_fat_value")
        self.sat_fat_value.setFont(font1)
        self.sat_fat_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.sat_fat_value, 2, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)

        self.salt_value = QLabel(self.groupBox_2)
        self.salt_value.setObjectName(u"salt_value")
        self.salt_value.setFont(font1)
        self.salt_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.salt_value, 6, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)

        self.fiber_value = QLabel(self.groupBox_2)
        self.fiber_value.setObjectName(u"fiber_value")
        self.fiber_value.setFont(font1)
        self.fiber_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.fiber_value, 7, 1, 1, 1)

        self.sugar_value = QLabel(self.groupBox_2)
        self.sugar_value.setObjectName(u"sugar_value")
        self.sugar_value.setFont(font1)
        self.sugar_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.sugar_value, 4, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setUnderline(False)
        self.label_2.setFont(font3)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.protein_value = QLabel(self.groupBox_2)
        self.protein_value.setObjectName(u"protein_value")
        self.protein_value.setFont(font1)
        self.protein_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.protein_value, 5, 1, 1, 1)

        self.energy_value = QLabel(self.groupBox_2)
        self.energy_value.setObjectName(u"energy_value")
        self.energy_value.setFont(font1)
        self.energy_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.energy_value, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, -1, -1, 5)
        self.title = QLineEdit(self.groupBox_3)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 28))
        self.title.setFont(font)

        self.horizontalLayout_14.addWidget(self.title)

        self.save_btn = QPushButton(self.groupBox_3)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setFont(font)

        self.horizontalLayout_14.addWidget(self.save_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.base_btn = QPushButton(self.groupBox_3)
        self.base_btn.setObjectName(u"base_btn")
        self.base_btn.setFont(font)

        self.verticalLayout_2.addWidget(self.base_btn)


        self.gridLayout_2.addWidget(self.groupBox_3, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NutriCalc", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Ingredients", None))
        self.product_label.setText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.amount_label.setText(QCoreApplication.translate("MainWindow", u"Amount (gram)", None))
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Nutrition per 100g", None))
        self.fat_value.setText(QCoreApplication.translate("MainWindow", u"g", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sugar", None))
        self.carb_value.setText(QCoreApplication.translate("MainWindow", u"g", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Fat", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Fiber", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Carbohydrate", None))
        self.sat_fat_value.setText(QCoreApplication.translate("MainWindow", u"g", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Salt", None))
        self.salt_value.setText(QCoreApplication.translate("MainWindow", u"g", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Protein", None))
        self.fiber_value.setText(QCoreApplication.translate("MainWindow", u"g", None))
        self.sugar_value.setText(QCoreApplication.translate("MainWindow", u"g", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Energy", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Saturated fat", None))
        self.protein_value.setText(QCoreApplication.translate("MainWindow", u"g", None))
        self.energy_value.setText(QCoreApplication.translate("MainWindow", u"kcal/kj", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Save to database", None))
        self.title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Titel", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.base_btn.setText(QCoreApplication.translate("MainWindow", u"Manage database", None))
    # retranslateUi

