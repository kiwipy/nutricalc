@echo off
if not exist venv\Scripts\ (
    python -m venv venv
    call "venv\Scripts\activate.bat"
    pip install -r requirements.txt
)

call "venv\Scripts\activate.bat"
cd src
python nutricalc.py
call "deactivate"
