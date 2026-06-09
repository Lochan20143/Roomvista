@echo off
cd /d %~dp0
if not exist venv ( python -m venv venv )
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
pause