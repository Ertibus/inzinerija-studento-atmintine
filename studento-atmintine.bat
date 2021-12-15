@ECHO OFF
python -m venv venv
venv\scripts\pip.exe install -r requirements.txt --quiet
venv\scripts\python.exe run.py
