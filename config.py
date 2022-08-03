"""Дополнительный модуль: работа с файлами конфигурации и данных."""

from pathlib import Path
from sys import argv
from configparser import ConfigParser as CP


# глобальные переменные модуля config
SCRIPT_DIR = Path(argv[0]).parent
PLAYERS_INI_PATH = SCRIPT_DIR / "players.ini"
SAVES_INI_PATH = SCRIPT_DIR / "saves.ini"

STATS = {}
SAVES = {}


def read_ini() -> bool:
    """Читает конфигурационные файлы, сохраняет прочитанные данные в глобальные переменные статистики и сохранений и возвращает True если приложение запущено впервые, иначе False."""
    # players.ini -> STATS
    # saves.ini -> SAVES
    # if not players.ini:
    #     return True
    # else:
    #     return False


def save_ini():
    """Записывает конфигурационные файлы, из глобальных переменных статистики и сохранений."""
    # STATS -> players.ini
    # SAVES -> saves.ini
