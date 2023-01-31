@echo off
IF EXIST env (
    echo Virtual Environment already exists! Skipping install...
    call env\Scripts\Activate.bat
) ELSE (
echo Starting Virtual Environment...
    python -m venv env
    call env\Scripts\Activate.bat
    echo Installing Python Dependencies...
    pip install -r requirements.txt
)
start "Server" cmd /k "python server.py" /min
timeout 3
python main.py