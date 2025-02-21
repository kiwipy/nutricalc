## Version (unreleased)
### Changed
- build.py: replaced if statements for match.

## Version 1.2.1 - (2025-02-05)
### Fixed
- resources.qrc: AppIcon alias
- build.py: `check_for_dependencies()` parse requirements.txt using wildcards
  for underscores/hyphens and add * to end for better matching.
- sv_SE.ts: "of which" lower case letters.

### Changed
- Only using PySide6-Essentials to save space
- main.py: moved all database functions to class in database.py
- Source files rename

## Version 1.2.0 - (2025-01-26)
### Added
- Translation layer
- Language: Swedish
- resources.qrc: added AppIcon.png
- New cross-platform build system written in python that makes use of:
  LINGUAS, POTFILES.in and RESOURCES.in
- Hyperlink to GitHub repo in statusbar

### Changed
- main.py: VERSION and APPLICATION using **kwargs in MainWindow class.
- main.py: New database created, not copied.

## Version 1.1.0 - (2025-01-10)
### Added
- nutricalc.py: new main script.
- db_view.py: enable modification of data.

### Changed
- main.py: moved VERSION and APPLICATION variables
- main.py: replaced re_calculate function with lambda function call for
  update_label_values in label_view.py module.
- main.py: moved manage_db function to db_view.py module and call with lambda.

### Removed
- Import calls in main.py (Ui_Dialog, QTableWidgetItem, QDialog)

## Version 1.0.0 - (2024-12-17)
_First release_
