"""Дополнительный модуль: раздел помощи и режим обучения."""

from shutil import get_terminal_size as gts
from math import ceil, floor


# глобальные переменные модуля help
HELP = """Раздел помощи:
...
..."""


def show_help() -> None:
    """Выводит в stdout раздел помощи."""
    print(HELP)


def show_title(title: str, *,
               padding_vertical: bool = False,
               center: bool = True,
               uppercase: bool = True) -> None:
    """Выводит в stdout заголовок в рамке."""
    terminal_width = gts()[0] - 1
    if center:
        padding_left = ceil((terminal_width - len(title) - 2) / 2)
        padding_right = floor((terminal_width - len(title) - 2) / 2)
    else:
        padding_left = 1
        padding_right = terminal_width - len(title) - padding_left - 2
    title = (title.capitalize(), title.upper())[uppercase]
    frame_char = ('+', '#')[padding_vertical]
    empty_line = (' '*(terminal_width - 2)).join(frame_char*2) + '\n'
    print(f'\n{frame_char*terminal_width}')
    print(('', empty_line)[padding_vertical], end='')
    print((' '*padding_left + title + ' '*padding_right).join(frame_char*2))
    print(('', empty_line)[padding_vertical], end='')
    print(f'{frame_char*terminal_width}\n')
