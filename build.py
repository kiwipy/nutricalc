#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright 2025, William Andersson <contact.kiwipy@gmail.com>
# Website: <https://github.com/kiwipy>
"""
Cross-platform (Linux/Windows) build script for PySide6 projects.
It initiates a virtual environment and installs all packages specified
in requirements.txt

It uses data/RESOURCES.in, lang/LINGUAS and lang/POTFILES.in to compile
resources for PySide6 and looks for any file with .ico extension in data/
directory for Windows executable.
"""

import os
import sys
import shutil
import platform
import fnmatch
from pathlib import Path

__version__ = "1.1.0"

PLATFORM = platform.uname().system
PYTHON_VER = f"{sys.version_info.major}.{sys.version_info.minor}"
APP_NAME = Path.cwd().name
APP_ICON = sorted(Path().glob("data/*.ico"))
GENERATED_FILES = []

def check_for_dependencies():
    insert_wild = {"-": "?", "_": "?"}
    installed = []
    missing = []

    if PLATFORM == 'Linux':
        for _file in Path().glob(f".venv/lib/python{PYTHON_VER}/site-packages/*"):
            installed.append(_file.name.lower())
    elif PLATFORM == 'Windows':
        for _file in Path().glob(f".venv/Lib/site-packages/*"):
            installed.append(_file.name.lower())

    if "pyinstaller" not in installed:
        missing.append("pyinstaller")

    with open('requirements.txt', 'r') as _file:
        for line in _file:
            _line = line.strip().lower()
            for old, new in insert_wild.items():
                _line = _line.replace(old, new)
            if not fnmatch.filter(installed, _line + '*'):
                missing.append(line.strip())

    to_install = ' '.join(missing)
    if len(missing) > 0:
        print(f"Installing packages...")
        os.system(f"pip install {to_install}")


def compile_project_files():
    check_for_dependencies()
    with open('lang/POTFILES.in', 'r') as _file:
        potfiles = []
        for line in _file:
            if '#' not in line.strip():
                potfiles.append(line.strip())

    pot_string = ' '.join(potfiles)
    with open('lang/LINGUAS', 'r') as _file:
        for _line in _file:
            if '#' not in _line.strip():
                os.system(f"pyside6-lupdate {pot_string} -ts lang/{_line.strip()}.ts")
                os.system(f"pyside6-lrelease lang/{_line.strip()}.ts -qm lang/{_line.strip()}.qm")
                GENERATED_FILES.append(f"lang/{_line.strip()}.qm")

    print("Compiling UI files...")
    for _file in Path().glob("src/*.ui"):
        print(f"    Compiling: {_file} --> {_file.with_suffix('.py')}")
        os.system(f"pyside6-uic {_file} -o {_file.with_suffix('.py')}")
        GENERATED_FILES.append(_file.with_suffix('.py'))

    print("Compiling resource files...")
    for _file in Path().glob("src/*.qrc"):
        print(f"    Compiling: {_file} --> {_file.with_suffix('.py')}")
        os.system(f"pyside6-rcc {_file} -o {_file.with_suffix('.py')}")
        GENERATED_FILES.append(_file.with_suffix('.py'))

    try:
        with open('.venv/generated_files', 'w') as _file:
            for line in GENERATED_FILES:
                _file.write(f"{line}\n")
    except Exception as e:
        print(e)


def build_binary_app():
    GENERATED_FILES.append(f"{APP_NAME}.spec")
    compile_project_files()

    print("Building binary application...")
    pyi_opt = [f"src/{APP_NAME.lower()}.py",
               f"--name={APP_NAME}",
               f"--icon={os.path.relpath(APP_ICON[0])}",
               f"--onedir",
               f"--windowed",
               f"--noconfirm",
               f"--contents-directory=.",
               f"--workpath=./build/build",
               f"--distpath=./build"
    ]
    with open('data/RESOURCES.in', 'r') as _file:
        for line in _file:
            if '#' not in line.strip():
                pyi_opt.extend(("--add-data", f"{line.strip()}:Resources"))

    import PyInstaller.__main__
    PyInstaller.__main__.run(pyi_opt)

    if PLATFORM == 'Linux':
        os.system(f"cd ./build/{APP_NAME}/ && ./{APP_NAME}")
    elif PLATFORM == 'Windows':
        os.system(f"cd build\\{APP_NAME} && start {APP_NAME}.exe")
    else:
        print("Could not determine system.")


def clean_up_project(_all):
    print("Cleaning up source tree...")
    build_dirs = ("build", "src/__pycache__")
    for directory in build_dirs:
        try:
            shutil.rmtree(directory)
            print(f"Removed {directory}/")
        except Exception as e:
            print(e)

    with open('.venv/generated_files', 'r') as _file:
        for line in _file:
            try:
                os.remove(line.strip())
                print(f"Removed {line.strip()}")
            except Exception as e:
                print(e)

    if _all == True:
        try:
            shutil.rmtree(".venv")
            print(f"Removed virtual environment: .venv/")
        except Exception as e:
            print(e)
            if PLATFORM == 'Windows':
                print("Remove virtual environment:")
                print("  On Windows you have to manually remove the .venv directory!")


def get_virtual_env(option):
    if not 'VIRTUAL_ENV' in os.environ:
        if not os.path.exists(".venv"):
            print("Creating new virtual environment...")
            os.system("python -m venv .venv")
        print("Restarting into virtual environment...")
        if PLATFORM == 'Linux':
            os.system(f"source .venv/bin/activate && ./build.py {option}")
        elif PLATFORM == 'Windows':
            os.system(f"call .venv\\Scripts\\activate.bat && build.py {option}")
        else:
            print("Could not determine system.")
        sys.exit(1)


def print_help():
    print("""Usage: build.py <OPTION>
Cross-platform (Linux/Windows) build script for PySide6 projects.

Options:
  --source                   run project from source
  --binary                   compile and run the application
  --clean                    cleanup source tree
  --reset                    cleanup source tree and remove virtual environment""")
    sys.exit(1)


if __name__=="__main__":
    if len(sys.argv) < 2:
        print_help()
    else:
        option = sys.argv[1]
        if option == '--help':
            print_help()

    if option == '--clean':
        clean_up_project(None)
    elif option == '--reset':
        clean_up_project(True)
    elif option == '--binary':
        get_virtual_env(option)
        build_binary_app()
    elif option == '--source':
        get_virtual_env(option)
        compile_project_files()
        os.system(f"python src/{APP_NAME.lower()}.py")
    else:
        print("Invalid option.")
        sys.exit(1)
