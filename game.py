"""Дополнительный модуль: обработка игрового процесса."""

from shutil import get_terminal_size as gts

import gameset


# глобальные переменные модуля game
BOARD = [[' '] * gameset.DIM for _ in range(gameset.DIM)]

# переменные типов для аннотации
Row = list[str] | tuple[str, ...]
Matrix = tuple[Row, ...] | list[Row]


def print_board(board: Matrix, *boards, right: bool = False) -> None:
    """Выводит в stdout игровое поле с ходами либо другими символами."""
    # объединяет все переданные игровые поля (матрицы) в общий кортеж
    boards = (board, ) + boards
    num_of_boards = len(boards)
    # формирует кортеж с шириной ячейки (в символах) для каждого переданного игрового поля
    width_cells = ()
    for board in boards:
        # в каждом ряду отдельного поля находит максимальную ширину строки
        max_width_for_rows = ()
        for row in board:
            max_width_for_rows += (max(len(cell) for cell in row), )
        # для каждого поля находит максимальную ширину среди вычисленных для рядов
        # добавляет отступ в один пробел слева и справа от обеих вертикальных границ ячейки поля
        width_cells += (1 + max(max_width_for_rows) + 1, )
    # для каждого поля вычисляет полную ширину поля - количество символов для горизонтальной разделительной линии
    width_boards = ()
    for i in range(num_of_boards):
        width_boards += (width_cells[i]*gameset.DIM + gameset.DIM - 1, )
    # получает текущую ширину окна терминала (в символах)
    width_terminal = get_terminal_size()[0] - 1
    # пробел между выводимыми полями
    pad = 5
    # вычисляет отступ от левого края окна терминала для выравнивания вправо
    if right:
        margin = width_terminal - sum(width_boards) - pad*(num_of_boards-1)
    else:
        margin = 1
    # формирует кортеж строк для вывода, содержащих значения ячеек в переданных игровых полях
    # каждая строка состоит из отступа margin и соответствующих рядов всех переданных полей, объединённых с помощью пробелов pad
    value_lines = ()
    # количество строк в кортеже равно размерности всех полей
    for i in range(gameset.DIM):
        values_of_all_boards = ()
        for j in range(num_of_boards):
            values_of_one_board = ()
            for cell in boards[j][i]:
                # к значению из каждой ячейки добавляется соответствующий данному полю отступ от обеих вертикальных границ - в результате значение ячейки выравнивается по центру относительного вертикальных границ
                values_of_one_board += (cell.center(width_cells[j]), )
            # полученные строки объединяются с использованием вертикального разделителя - это строка со значениями одного игрового поля
            values_of_all_boards += ('|'.join(values_of_one_board), )
        # строки со значениями одного игрового поля объединяются с использованием пробелов pad
        padded_values = (' '*pad).join(values_of_all_boards)
        # к полученной строке слева добавляется отступ margin
        value_lines += (' '*margin + padded_values, )
    # формирует горизонтальную линию разделитель на основе данных о полной ширине всех полей, добавляя между линиями пробелы pad и отступ margin
    horiz_line = ' '*margin + (' '*pad).join('—'*wd for wd in width_boards)
    # заканчивает формирование горизонтальных разделителей добавляя символы конца строк
    # выводит строки со значениями, объединяя их с горизонтальными разделителями
    print(('\n' + horiz_line + '\n').join(value_lines))


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
