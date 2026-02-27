@echo off
setlocal

cd /d "%~dp0"

if not exist ".venv\" (
  echo Creating virtual environment...
  py -m venv .venv
)

echo Activating virtual environment...
call ".venv\Scripts\activate.bat"

echo Installing dependencies...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo.
echo Starting PED app...
echo Open this in your browser: http://127.0.0.1:5000
echo Press Ctrl+C to stop the server.
echo.

python -m waitress --listen=127.0.0.1:5000 app:app

