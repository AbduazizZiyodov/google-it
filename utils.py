from telebot import TeleBot

from random import choice

from telebot.types import InlineQuery
from telebot.types import InputTextMessageContent
from telebot.types import InlineQueryResultArticle

from core import googleit

from settings import GROUP_CHAT_ID as chat_id
from settings import CHANNEL_NAME as channel
from settings import SUPER_USER_ID as su_id


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


def format_info(query: InlineQuery) -> str:
    term, user = query.query, query.from_user
    return "🔎Search-term: {}\n💂‍♂️User-INFO:\n- ⚜User ID: #{}\n- 🔰Username: @{}\n- ➡First Name: {}\n- ➡Last Name: {}\n- 👀is_bot: {}\n"\
        .format(
            term.lower(), user.id,
            user.username, user.first_name,
            user.last_name, user.is_bot
        )


def save(query: InlineQuery, bot: TeleBot) -> None:
    bot.send_message(int(su_id), format_info(query))


def get_random_meme() -> str:
    return "meme_{}.jpg".format(choice(range(1, 7)))
