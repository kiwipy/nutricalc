# SPDX-License-Identifier: MIT
# Copyright 2024, The NutriCalc developers
# Author: William Andersson <contact.kiwipy@gmail.com>

def update_values(self):
    kcal = kj = fat = sat_fat = carbs = sugar = protein = salt = fiber = 0
    total_amount = 0

    for index in range(len(self.ComboBox_tuple)):
        # Sum up the values from all QSpinBox.
        total_amount += self.SpinBox_tuple[index].value()

    for index in range(len(self.ComboBox_tuple)):
        # Calculate energy content for each by 100g
        if self.ComboBox_tuple[index].currentIndex() != -1:
            product = self.database.get_item(self.ComboBox_tuple[index].currentText())
            if self.SpinBox_tuple[index].value() != 0:
                #print(f"{product[0]}")
                quotient = self.SpinBox_tuple[index].value() / total_amount
                fat += float(product[0][1]) * quotient
                sat_fat += float(product[0][2]) * quotient
                carbs += float(product[0][3]) * quotient
                sugar += float(product[0][4]) * quotient
                protein += float(product[0][5]) * quotient
                salt += float(product[0][6]) * quotient
                fiber += float(product[0][7]) * quotient

    # Calculation of 'kj' & 'kcal'
    kj = int((protein*17)+(carbs*17)+(fiber*8)+(fat*37))
    kcal = int(kj * 0.239)
    self.ui.fat_value.setText(f"{round(fat, 1)}g")
    self.ui.sat_fat_value.setText(f"{round(sat_fat, 1)}g")
    self.ui.carb_value.setText(f"{round(carbs, 1)}g")
    self.ui.sugar_value.setText(f"{round(sugar, 1)}g")
    self.ui.protein_value.setText(f"{round(protein, 1)}g")
    self.ui.salt_value.setText(f"{round(salt, 1)}g")
    self.ui.fiber_value.setText(f"{round(fiber, 1)}g")
    self.ui.energy_value.setText(f"{kcal}kcal/{kj}kj")
