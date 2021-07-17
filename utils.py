from telebot import TeleBot

from random import choice
from loguru import logger

from telebot.types import InlineQuery
from telebot.types import InputTextMessageContent
from telebot.types import InlineQueryResultArticle

from core import googleit

from settings import BOT_TOKEN as token
from settings import GROUP_CHAT_ID as chat_id
from settings import CHANNEL_NAME as channel


url = f"https://api.telegram.org/bot{token}/getChatMember"


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
        "Search Term ** {} ** By user -> first_name {} | last_name {} | username @{} | user_id #{}".format(
            term, user.first_name, user.last_name, user.username, user.id))


bad_words: list = ['bad']


def check(query: InlineQuery) -> bool:
    """Function: checking message for bad words..."""
    term = query.query.lower()
    for word in bad_words:
        if word in term:
            return False
    return True


numbers = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']


def get_search_results(query: InlineQuery) -> str:
    """Function for formatting search results"""
    term = query.query.lower()
    results = "🔍Search results: {}🤓\n".format(term)

    search_results = googleit(term=term)

    if len(search_results) > 1:
        for index, result in enumerate(search_results):
            results += '{} {}\n👉Link {}\n\n'.format(
                numbers[index],
                result['title'],
                result['link']
            )
        return str(results)
    else:
        results += "🙄"


def make_query_result(results: str, query: InlineQuery) -> InlineQueryResultArticle:
    """Making result for default inline query"""
    return InlineQueryResultArticle(
        id='1',
        title='The search for "{}" is done ✅'.format(query.query),
        description='Click me if you want to see results😊',
        input_message_content=InputTextMessageContent(
            message_text=results)
    )


def make_chat_member_result() -> InlineQueryResultArticle:
    """
    Query result for if user is not spec. group member
    p.s only for group members allowed to use this bot !
    """
    return InlineQueryResultArticle(
        id='1',
        title='Error while using a bot 🤔',
        description="For using this bot, you need to be a member of the {} group 😃(click me)".format(
            chat_id),
        input_message_content=InputTextMessageContent(
            message_text="It would be nice if you join {} channel.".format(channel))
    )


def check_group_member(bot: TeleBot, user_id: int) -> bool:
    return True \
        if bot.get_chat_member(chat_id, user_id).status == "member" else False


def get_random_meme() -> str:
    return "meme_{}.jpg".format(choice(range(1, 7)))
