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


# функции
def read_ini() -> bool:
    """Читает конфигурационные файлы, сохраняет прочитанные данные в глобальные переменные статистики и сохранений и возвращает True если приложение запущено впервые, иначе False."""
    # players.ini -> STATS
    # saves.ini -> SAVES
    # if not players.ini:
    #     return True
    # else:
    #     return False


def show_help() -> None:
    """Выводит в stdout раздел помощи."""
    print(HELP)


def get_player_name() -> None:
    """Запрашивает имя игрока и проверяет присутствие этого имени в глобальной переменной статистики, добавляет имя в глобальную переменную текущих игроков."""
    # stdin -> name
    # if name not in STATS:
    #     new_player(name)
    # name -> PLAYERS


def new_player(player_name: str) -> None:
    """Создаёт запись о новом игроке в глобальной переменной статистики."""


# суперцикл
while True:
    command = input(' > ').lower()
    if command in ('quit', 'exit', 'q', 'e'):
        break
    elif command in ('new', 'n'):
        # начало партии
        pass
    # elif ...
