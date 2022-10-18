def accounts_info_message(accounts_information: list):
    statistic = ""
    for account in accounts_information:
        statistic += (
            f"Id: {account['id']}\n"
            f"Текущая дата: {account['current_date']}\n"
            f"Сайт: {account['site']}\n"
            f"Логин: {account['login']}\n"
            f"Пароль: {account['password']}\n"
            f"Country: {account['country']}\n"
            f"Patch: {account['patch']}\n"
            f"Number of application: {account['number_of_application']}\n"
            f"Исключить даты: {account['remove_dates']}\n"
            f"Не ранее даты: {account['no_later_than']}\n"
            f"Не менее Х дней: {account['no_less_than']}\n\n"
        )
    statistic = statistic.replace("Пропустить", "не задано")
    return f"Статистика по аккаунтам:\n{statistic}"


START_MESSAGE = (
    "Привет!\nЯ бот который поможет с записью в очередь на визу.\nВыберите действие:"
)
NO_SUCH_COMMAND = "Кажется, вы ввели неккоректную команду.\nПопробуйте еще раз!"


DELETE_START_MESSAGE = "Введите ID аккаунта для удаления:"
ACCOUNT_NOT_FOUND = "Такого аккаунта не существует!"
DELETE_APPROVED = "Аккаунт удален!"

INPUT_SITE = "Выберите сайт:"
INPUT_LOGIN = "Введите логин:"
INPUT_PASSWORD = "Введите пароль:"
INPUT_NO_LATER_THAN = "Не позднее даты:\n\nВведите дату в формате (dd.mm.yyyy) или нажмите на кнопку.\nПример: 23.12.2022"
INPUT_REMOVE_DATES = "Исключить даты:\n\nВведите промежуток в формате (dd.mm.yyyy - dd.mm.yyyy) или нажмите на кнопку.\nПример: 20.12.2022 - 30.12.2022"
INPUT_NO_LESS_THAN = "Не менее Х дней:\n\nВведите число X или нажмите на кнопку."
INPUT_COUNTRY = "Введите country:"
INPUT_PATCH = "Введите patch:"
INPUT_NUMBER_OF_APPLICATION = "Введите number_of_application:"
ADD_APPROVED = "Аккаунт добавлен!"
