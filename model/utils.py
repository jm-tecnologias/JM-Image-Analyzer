import sys
from pathlib import Path

def get_base_path():
    if getattr(sys, 'frozen', False):
        # Executável
        return Path(sys._MEIPASS)
    else:
        # Desenvolvimento
        return Path(__file__).resolve().parent.parent