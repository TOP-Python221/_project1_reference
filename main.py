"""Модуль верхнего уровня для учебного проекта 1: Крестики-Нолики"""

# импорт дополнительных модулей проекта
import config
import help
import commands
import gameset
import game


# начало отработки Этапов работы приложения согласно Архитектуре

# 1. Загрузка файлов настроек
if config.read_ini():
    # 2. ЕСЛИ первый запуск приложения:
    #         вывод раздела помощи
    help.show_help()

# 3. Запрос имени игрока
gameset.get_player_name()

# суперцикл
while True:
    # 4. Ожидание ввода пользовательских команд
    command = input(' > ').lower()

    if command in ('quit', 'exit', 'q', 'e'):
        break

    elif command in ('new', 'n'):
        # 5. Запрос режима игры
        #    6. Запрос символа для игры
        gameset.game_mode()
        # 8. Партия
        #    7. ЕСЛИ первая партия для любого из игроков
        result = game.game()
        if result is None:
            # 9. ЕСЛИ партия закончена досрочно:
            #         сохранение данных о партии
            game.save_game()
        else:
            # 10. Внесение изменений в статистику игрока(-ов)
            game.update_stats(result)

    elif command in ('load', 'l'):
        if flag := commands.load():
            game.game(flag)
            # убрать доигранную партию из SAVES
        else:
            print('no saved games for you')

    # elif ... прочие команды

config.save_ini()
