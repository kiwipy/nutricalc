# SPDX-License-Identifier: MIT
# Copyright 2024, The NutriCalc developers
# Author: William Andersson <contact.kiwipy@gmail.com>

import sys
import platform
from pathlib import Path

def local_path_for(app_name):
    """
    Creates and returns local data directory e.g:
    On Linux: /home/USER_NAME/.local/share/app_name
    On Windows: C:\\Users\\USER_NAME\\AppData\\Local\\app_name
    """
    if platform.system() == "Windows":
        local_path = Path.home() / f"AppData/Local/{app_name}"
    elif platform.system() == "Linux":
        local_path = Path.home() / f".local/share/{app_name}"
    else:
        local_path = None

    if local_path != None:
        if not local_path.exists():
            try:
                local_path.mkdir()
                print(f"Directory '{local_path}' created successfully.")
            except PermissionError:
                print(f"Permission denied: Unable to create '{local_path}'.")
            except Exception as e:
                print(f"Error: {e}")

    return local_path
