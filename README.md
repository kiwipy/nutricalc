# NutriCalc
Pick the ingredients and amount used according to recepie and the application calculates the nutritional values needed for product labeling, including fiber content which is optional on labels.
> [!TIP]
> Don't forget to add water if used.

![Screenshot](https://github.com/kiwipy/nutricalc/blob/main/docs/main_window.png)<br>

## Build instructions
**Use the cross-platform build.py script.**<br>
Linux: `chmod 755 build.py && ./build.py --binary`<br>
Windows: `build.py --binary`<br>

## Manage the database
In this window you can remove products from the database by selecting the name and click 'remove'. You can also add products that do not need to be calculated (e.g. bought finished products) or update the values of existing products.

![Screenshot](https://github.com/kiwipy/nutricalc/blob/main/docs/db_window.png)<br>

> [!NOTE]
> When adding bought products remember that 'Fiber content' is not required on labels BUT is used to correctly calculate calories, contact the producer if the label does not include fiber content.

## Limitations
Alcohol content is left out (Alcohol content is also used to calculate calories), if you need it in production feel free to fork this repo.<br><br>
As for now the application supports up to 12 ingredients.<br>

> [!NOTE]
> :blue_square: THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT ANY WARRANTY.<br>
> :blue_square: This application is made to comply with EU regulations only.<br>

## Credits
<img align="left" src="https://github.com/kiwipy/nutricalc/blob/main/data/AppIcon.png" alt="AppIcon" width="32" height="32">
<a href="https://www.flaticon.com/free-icons/flask" title="flask icons">Flask icons created by Freepik - Flaticon</a>
