# PSEC CA1-2 (Security Application)

## Requirements
- [Python 3.9+](https://www.python.org/downloads/)
- [Nmap 7.93+](https://nmap.org/download.html)
## Installation

```bash
git clone https://github.com/gatariee/PSEC-CA1-2
cd PSEC-CA1-2
```

### Windows (Automatic Setup)
```bash
./start.bat
```

### Linux (Automatic Setup)
```bash
chmod +x start.sh
./start.sh
source env/bin/activate && source env/Scripts/activate
python server.py
python main.py
```

### Windows (Manual Setup)
```bash
python -m venv env
./env/Scripts/activate.bat
pip install -r requirements.txt
python main.py
```

### Linux (Manual Setup)
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python main.py
```

