def start_message():
    return "Привет!\nЯ бот который поможет с записью в очередь на визу.\nВыберите действие:"


def no_such_command():
    return "Кажется, вы ввели неккоректную команду.\nПопробуйте еще раз!"


def accounts_info_message(accounts_information: list):
    statistic = ""
    for account in accounts_information:
        statistic += (
            f"Id: {account['id']}\n"
            f"Сайт: {account['site']}\n"
            f"Логин: {account['login']}\n"
            f"Пароль: {account['password']}\n"
            f"Текущая дата: {account['current_date']}\n\n"
        )
    return f"Статистика по аккаунтам:\n{statistic}"
