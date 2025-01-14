# NutriCalc
![Screenshot](https://github.com/william-andersson/nutricalc/blob/main/main_window.png)<br>
The run.sh script initiates a virtual environment and starts the application.<br>
`chmod 755 run.sh`<br>
`./run.sh`

## Description
Calculate nutritional values for product labeling.<br>
Pick the ingredients and amount used according to recepie and optionaly save the product to the database for later use.

> [!NOTE]
> :blue_square: THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT ANY WARRANTY.<br>
> :blue_square: This application is made to comply with EU regulations only.<br>
> :blue_square: All values except 'Fiber content' is required on labels.<br>
> :blue_square: Alcohol content is purpesly left out! (Alcohol content is also used to calculate calories, add it to the code if you need it in production.

## Manage database
![Screenshot](https://github.com/william-andersson/nutricalc/blob/main/db_window.png)<br>
In this window you can remove products from the database by selecting the name and click 'remove'. You can also add products that do not need to be calculated e.g. bought finished products.

> [!NOTE]
> When adding bought products remember that 'Fiber content' is not required on labels BUT is used to correctly calculate calories, contact the producer if the label does not include fiber content.
