"""Дополнительный модуль: искусственный интеллект."""

import config
import gameset


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
    return tuple(matrix[row_index])


def cells_column(matrix: config.Matrix, column_index: int) -> tuple:
    """Возвращает кортеж с элементами столбца матрицы по индексу столбца."""
    return tuple(matrix[i][column_index] for i in range(gameset.DIM))


def cells_maindiagonal(matrix: config.Matrix, row_index: int, column_index: int) -> tuple:
    """Возвращает кортеж с элементами главной диагонали матрицы по индексам ряда и столбца."""
    if row_index == column_index:
        return tuple(matrix[i][i] for i in range(gameset.DIM))
    else:
        return tuple()


def cells_antidiagonal(matrix: config.Matrix, row_index: int, column_index: int) -> tuple:
    """Возвращает кортеж с элементами побочной диагонали матрицы по индексам ряда и столбца."""
    if row_index == gameset.DIM - column_index - 1:
        return tuple(matrix[i][gameset.DIM - i - 1] for i in range(gameset.DIM))
    else:
        return tuple()


def sum_matrix(*matrices: config.Matrix) -> config.Matrix:
    """Поэлементно складывает переданные матрицы и возвращает результирующую матрицу."""
    result_matrix = []
    for i in range(gameset.DIM):
        result_matrix += [[]]
        for j in range(gameset.DIM):
            result_matrix[i] += [sum(matrix[i][j] for matrix in matrices)]
    return result_matrix


def indexes_matrix_max(matrix: config.Matrix) -> config.TurnCoords:
    """Находит наибольший элемент в матрице и возвращает индексы этого элемента в виде кортежа."""
    mx, coords = 0, ()
    for i in range(gameset.DIM):
        for j in range(gameset.DIM):
            if mx < matrix[i][j]:
                mx, coords = matrix[i][j], (i, j)
    return coords


def weights_tokens(board: config.Matrix, token_index: int) -> config.Matrix:
    """Конструирует и возвращает матрицу весов занятых ячеек игрового поля."""


def weights_empty(tokens_weights: config.Matrix) -> config.Matrix:
    """Вычисляет и возвращает матрицу весов пустых ячеек игрового поля."""


def weights_clear(empty_weights: config.Matrix) -> config.Matrix:
    """Обрабатывает матрицу принятия решения, приравнивая к нолю элементы, соответствующие занятым на поле клеткам."""


def calc_strategy_matrices() -> None:
    """Вычисляет и заполняет начальные матрицы принятия решений для стратегий 'крестика' и 'нолика'.

    ВНИМАНИЕ: вычисляет корректные матрицы только для нечётных значений размерности игрового поля (gameset.DIM)."""

