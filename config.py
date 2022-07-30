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
    global STATS, SAVES
    # players.ini -> STATS
    ini_file = CP()
    ini_file.read(PLAYERS_INI_PATH)
    for player in ini_file.sections():
        tr = True if ini_file[player]['training'] == 'True' else False
        st = ini_file[player]['stats'].split(',')
        STATS[player] = {'training': tr, 'stats': {'wins': int(st[0]),
                                                   'ties': int(st[1]),
                                                   'fails': int(st[2])}}
    # pprint(STATS)
    if STATS:
        return False
    else:
        return True
    # saves.ini -> SAVES
    # if not players.ini:
    #     return True
    # else:
    #     return False


def save_ini():
    """Записывает конфигурационные файлы, из глобальных переменных статистики и сохранений."""
    # STATS -> players.ini
    # SAVES -> saves.ini
