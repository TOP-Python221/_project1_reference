"""Модуль верхнего уровня для учебного проекта 1: Крестики-Нолики"""

# импорт дополнительных модулей проекта
from pathlib import Path
from sys import argv


# глобальные переменные
SCRIPT_DIR = Path(argv[0]).parent
PLAYERS_INI_PATH = SCRIPT_DIR / "players.ini"
SAVES_INI_PATH = SCRIPT_DIR / "saves.ini"

STATS = {}
SAVES = {}

PLAYERS = ()

HELP = """Раздел помощи:
...
..."""


# суперцикл
while True:
    command = input(' > ').lower()
    if command in ('quit', 'exit', 'q', 'e'):
        break
    elif command in ('new', 'n'):
        # начало партии
        pass
    # elif ...
