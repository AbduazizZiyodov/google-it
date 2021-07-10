from loguru import logger

from telebot.types import InlineQuery

from core import googleit


bad_words: list = ['bad']


def get_search_results(query: InlineQuery) -> str:
    query, results = query.query.lower(), "[🔍Search results🤓]\n\n"
    for index, result in enumerate(googleit(term=query)):
        results += f'🔰{index+1}) {result}\n'
    return results


def check(query: InlineQuery) -> bool:
    term = query.query.lower()
    for word in bad_words:
        if word in term:
            return False
    return True


class Logging(object):
    def __init__(self, file) -> None:
        self.file = file
        self.__setup_logger()

    def __setup_logger(self) -> None:
        logger.add(self.file, backtrace=True, diagnose=True)

    def log(self, message: str) -> None:
        logger.info(message)


activity = Logging('actions.log')


def save(query: InlineQuery) -> None:
    activity.log(
        f"Search Term **{query.query}** By user -> first_name {query.from_user.first_name} | last_name {query.from_user.last_name} | username @{query.from_user.username} | user_id #{query.from_user.id}")
