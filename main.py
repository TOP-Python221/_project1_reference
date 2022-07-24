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

DIM = 3

BOARD = [[' ']*DIM for _ in range(DIM)]
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



# начало отработки Этапов работы приложения согласно Архитектуре

# 1. Загрузка файлов настроек
if read_ini():
    # 2. ЕСЛИ первый запуск приложения:
    #         вывод раздела помощи
    show_help()

# 3. Запрос имени игрока
get_player_name()

# суперцикл
while True:
    # 4. Ожидание ввода пользовательских команд
    command = input(' > ').lower()

    if command in ('quit', 'exit', 'q', 'e'):
        break

    elif command in ('new', 'n'):
        # 5. Запрос режима игры
        #    6. Запрос символа для игры
        game_mode()
        # 8. Партия
        #    7. ЕСЛИ первая партия для любого из игроков
        result = game()
        if result is None:
            # 9. ЕСЛИ партия закончена досрочно:
            #         сохранение данных о партии
            save_game()
        else:
            # 10. Внесение изменений в статистику игрока(-ов)
            update_stats(result)

    elif command in ('load', 'l'):
        if flag := load():
            game(flag)
        else:
            print('no saved games for you')

    # elif ... прочие команды
