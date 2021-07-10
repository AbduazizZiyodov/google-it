from loguru import logger

from telebot.types import InlineQuery
from telebot.types import InlineQueryResultArticle
from telebot.types import InputTextMessageContent

from json import dumps
from requests import request

from core import googleit

from settings import config

bad_words: list = ['bad']


def get_search_results(query: InlineQuery) -> str:
    """Function for formatting search results"""
    query, results = query.query.lower(), "[🔍Search results🤓]\n\n"
    for index, result in enumerate(googleit(term=query)):
        results += f'🔰{index+1}) {result}\n'
    return results


def make_query_result(results: str, query: InlineQuery) -> InlineQueryResultArticle:
    """Function: making result for inline query"""
    return InlineQueryResultArticle(
        id='1',
        title='The search for "{}" is done ✅'.format(query.query),
        description='Click me if you want to see results😊',
        input_message_content=InputTextMessageContent(
            message_text=results)
    )


def make_chat_member_result(group_name: str) -> InlineQueryResultArticle:
    """
    Message for if user is not group member
    p.s only for group members allowed to use this bot
    """
    return InlineQueryResultArticle(
        id='1',
        title='Error when using bot 🤔',
        description="""For using this bot, you need to be a member of the {} group 😃""".format(
            group_name)
        .format(group_name),
        input_message_content=InputTextMessageContent(
            message_text=f'{group_name}')
    )


def check(query: InlineQuery) -> bool:
    """Function: checking message for bad words..."""
    term = query.query.lower()
    for word in bad_words:
        if word in term:
            return False
    return True


class Logging(object):
    """Simple logging object with one private and public method"""

    def __init__(self, file) -> None:
        self.file = file
        self.__setup_logger()

    def __setup_logger(self) -> None:
        logger.add(self.file, backtrace=True, diagnose=True)

    def log(self, message: str) -> None:
        logger.info(message)


activity = Logging('actions.log')


def save(query: InlineQuery) -> None:
    """Logging message format"""
    term, user = query.query.encode("utf-8"), query.from_user
    activity.log(
        f"Search Term ** {term} ** By user -> first_name {user.first_name} | last_name {user.last_name} | username @{user.username} | user_id #{user.id}")


def check_group_member(user_id: int) -> bool:
    """
    Check user for group member. 
    Solution: with telegram API
    """
    bot_token, chat_id = config['BOT_TOKEN'], config["GROUP_CHAT_ID"]

    url = f"https://api.telegram.org/bot{bot_token}/getChatMember"

    request_body = dumps({
        "chat_id": chat_id,
        "user_id": int(user_id)
    })

    response = request(
        "POST", url, headers={
            'Content-Type': 'application/json'
        }, data=request_body)
    print(request_body)
    return True if response.status_code == 200 else False
