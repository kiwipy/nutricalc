#!/bin/bash
if [[ ! -d "venv/bin/" ]]; then
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
fi

source venv/bin/activate
cd src
./nutricalc.py
deactivate
