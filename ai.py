"""Дополнительный модуль: искусственный интеллект."""

import config


# глобальные переменные модуля ai
BOT_NAME_EASY = 'bot1'
BOT_NAME_HARD = 'bot2'


def bot_turn() -> config.TurnCoords:
    """Возвращает координаты ячейки поля для текущего хода бота в зависимости от сложности."""


def easy_mode() -> config.TurnCoords:
    """Рассчитывает координат ячейки поля для текущего хода бота для низкого уровня сложности."""


def hard_mode(token_index: int) -> config.TurnCoords:
    """Рассчитывает координат ячейки поля для текущего хода для высокого уровня сложности."""


def cells_row(matrix: config.Matrix, row_index: int) -> tuple:
    """Возвращает кортеж с элементами ряда матрицы по индексу ряда."""


def cells_column(matrix: config.Matrix, column_index: int) -> tuple:
    """Возвращает кортеж с элементами столбца матрицы по индексу столбца."""


def cells_maindiagonal(matrix: config.Matrix, row_index: int, column_index: int) -> tuple:
    """Возвращает кортеж с элементами главной диагонали матрицы по индексам ряда и столбца."""


def cells_antidiagonal(matrix: config.Matrix, row_index: int, column_index: int) -> tuple:
    """Возвращает кортеж с элементами побочной диагонали матрицы по индексам ряда и столбца."""


def sum_matrix(*matrices: config.Matrix) -> config.Matrix:
    """Поэлементно складывает переданные матрицы и возвращает результирующую матрицу."""


def indexes_matrix_max(matrix: config.Matrix) -> config.TurnCoords:
    """Находит наибольший элемент в матрице и возвращает индексы этого элемента в виде кортежа."""


def weights_tokens(board: config.Matrix, token_index: int) -> config.Matrix:
    """Конструирует и возвращает матрицу весов занятых ячеек игрового поля."""


def weights_empty(tokens_weights: config.Matrix) -> config.Matrix:
    """Вычисляет и возвращает матрицу весов пустых ячеек игрового поля."""


def weights_clear(empty_weights: config.Matrix) -> config.Matrix:
    """Обрабатывает матрицу принятия решения, приравнивая к нолю элементы, соответствующие занятым на поле клеткам."""


def calc_strategy_matrices() -> None:
    """Вычисляет и заполняет начальные матрицы принятия решений для стратегий 'крестика' и 'нолика'.

    ВНИМАНИЕ: вычисляет корректные матрицы только для нечётных значений размерности игрового поля (gameset.DIM)."""

