"""Дополнительный модуль: обработка игрового процесса."""

import gameset


# глобальные переменные модуля game
BOARD = [[' '] * gameset.DIM for _ in range(gameset.DIM)]

# переменные типов для аннотации
Row = list[str] | tuple[str, ...]
Matrix = tuple[Row, ...] | list[Row]


def print_board(board: Matrix, *boards, right: bool = False) -> None:
    """Выводит в stdout игровое поле с ходами либо другими символами."""


def human_turn():
    """Запрос координат ячейки поля для текущего хода."""


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


def update_stats(score: tuple[dict, dict]) -> None:
    """Обновляет глобальную переменную статистики в соответствии с результатом завершённой партии."""
    # for i in range(2):
    #     score[i] -> STATS[PLAYERS[i]]


def save_game() -> None:
    """Обновляет глобальную переменную сохранений в соответствии с текущим состоянием глобальных переменных текущих игроков и сделанных ходов."""
    # PLAYERS, BOARD -> SAVES
