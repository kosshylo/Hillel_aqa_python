"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)

def read_last_log_line()->str:
    '''
    function for reading last log line
    :param username:
    :param status:
    :return: last line
    '''


    with open("login_system.log", "r") as f:
        lines = f.readlines()
        if lines:
            last_line = lines[-1]
            # print("last string:", last_line.strip())
            return last_line


def parsed_logLevel_from_logging_line(last_line: str)->str:
    parts = last_line.split("- ")
    log_level = parts[1].strip()
    return log_level


def parsed_status_from_logging_line(last_line: str)->str:
    parts = last_line.split(":")
    status = parts[-1].strip()  # strip - removed
    return status



def parsed_username_from_logging_line(last_line: str)->str:
    parts = last_line.split(": ")
    log_username = parts[1].split(", ")[0]

    return log_username





if __name__ == '__main__':
    username = "Kostia"
    status = "success"
    log_event(status=status,username=username)
    print(parsed_status_from_logging_line(read_last_log_line()))
    print(parsed_logLevel_from_logging_line(read_last_log_line()))
    print(parsed_username_from_logging_line(read_last_log_line()))


