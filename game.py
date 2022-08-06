"""Дополнительный модуль: обработка игрового процесса."""

from shutil import get_terminal_size as gts

import config
import gameset


# глобальные переменные модуля game
BOARD = [[''] * gameset.DIM for _ in range(gameset.DIM)]

# переменные типов для аннотации
Row = list[str | int | float] | tuple[str | int | float, ...]
Matrix = tuple[Row, ...] | list[Row]
TurnCoords = tuple[int, int]
Score = tuple[dict, dict]


def print_board(board: Matrix, *boards: Matrix, right: bool = False) -> None:
    """Выводит в stdout игровое поле с ходами либо другими символами."""
    boards = (board, ) + boards
    num_of_boards = len(boards)
    width_cells = tuple(max(max(len(cell) for cell in row) for row in board) + 2
                        for board in boards)
    width_boards = tuple(width_cells[i]*gameset.DIM + gameset.DIM - 1
                         for i in range(num_of_boards))
    pad = 5
    margin = (1, gts()[0]-1 - sum(width_boards) - pad*(num_of_boards-1))[right]
    value_lines = ()
    for i in range(gameset.DIM):
        values = ('|'.join(f"{cell:^{width_cells[j]}s}" for cell in boards[j][i])
                  for j in range(num_of_boards))
        value_lines += (' '*margin + (' '*pad).join(values), )
    horiz_line = ' '*margin + (' '*pad).join('—'*wd for wd in width_boards)
    print(f'\n{horiz_line}\n'.join(value_lines))


def human_turn():
    """Запрос координат ячейки поля для текущего хода."""


def game(zero_turn=False) -> Score | None:
    """Обрабатывает игровой процесс."""
    # training = is_first_game()
    # for name in gameset.PLAYERS:
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


def update_stats(score: Score) -> None:
    """Обновляет глобальную переменную статистики в соответствии с результатом завершённой партии."""
    # for i in range(2):
    #     score[i] -> config.STATS[gameset.PLAYERS[i]]


def save_game() -> None:
    """Обновляет глобальную переменную сохранений в соответствии с текущим состоянием глобальных переменных текущих игроков и сделанных ходов."""
    # gameset.PLAYERS, BOARD -> config.SAVES
