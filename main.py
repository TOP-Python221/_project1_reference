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


def game_mode() -> str:
    """Запрашивает режим для новой партии, добавляет имя бота либо второго игрока в глобальную переменную текущих игроков, запрашивает очерёдность ходов."""
    # stdin -> mode
    # if mode == 'single':
    #     get_difficulty_level()
    # elif mode == 'double':
    #     get_player_name()
    # stdin -> who_is_cross
    # name -> PLAYERS
    # return -> mode


def is_first_game() -> bool:
    """Проверяет является ли данная партия первой для любого из игроков."""
    # for name in PLAYERS:
    #     if STATS[name]['training']:
    #         return True
    # else:
    #     return False


def game(zero_turn=False) -> tuple[dict, dict] | None:
    """Обрабатывает игровой процесс."""
    # training = is_first_game()
    # for name in PLAYERS:
    #     if zero_turn:
    #         continue
    #     if name.startswith('bot'):
    #         if training:
    #             'подсказка' -> stdout
    #         bot_turn(name[-1]) -> BOARD
    #     else:
    #         human_turn() -> inp
    #         if inp:
    #             inp -> BOARD
    #         else:
    #             return None
    #     check_win_or_tie() -> win_or_tie
    #     if win_or_tie ...:
    #         return -> ({}, {})


def load() -> bool:
    """Выводит в stdout все сохранённые партии для текущего игрока, запрашивает партию для загрузки, настраивает глобальные переменные и возвращает True/False в зависимости от очерёдности хода."""
    # name = PLAYERS[0]
    # for players, save in SAVES.items():
    #     players -> stdout
    # stdin -> choice
    # SAVES[choice]['turns'] -> BOARD
    # choice -> PLAYERS
    # if turns_amount % 2 == 0:
    #     return False
    # else:
    #     return True


def update_stats(score: tuple[dict, dict]) -> None:
    """Обновляет глобальную переменную статистики в соответствии с результатом завершённой партии."""
    # for i in range(2):
    #     score[i] -> STATS[PLAYERS[i]]


def save_game() -> None:
    """Обновляет глобальную переменную сохранений в соответствии с текущим состоянием глобальных переменных текущих игроков и сделанных ходов."""
    # PLAYERS, BOARD -> SAVES


def save_ini():
    """Записывает конфигурационные файлы, из глобальных переменных статистики и сохранений."""
    # STATS -> players.ini
    # SAVES -> saves.ini


def human_turn():
    """Запрос координат ячейки поля для текущего хода."""


def bot_turn(difficulty_level: str):
    """Расчёт координат ячейки поля для текущего хода."""


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
            # убрать доигранную партию из SAVES
        else:
            print('no saved games for you')

    # elif ... прочие команды

save_ini()
