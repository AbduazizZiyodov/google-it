from time import sleep
from telebot import TeleBot

from telebot.types import InlineQuery

from utils import save
from utils import check
from utils import activity
from utils import get_search_results
from utils import make_query_result
from utils import make_chat_member_result
from utils import check_group_member

from settings import config


bot = TeleBot(config["BOT_TOKEN"])

activity.log('Bot works!')


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def perform_search(query: InlineQuery):
    print(check_group_member(query.from_user.id))
    if check_group_member(query.from_user.id):
        sleep(3)
        results: str = get_search_results(query) if check(query) else '💥'
        save(query)
        bot.answer_inline_query(query.id, [make_query_result(results, query)])
    else:
        save(query)
        bot.answer_inline_query(
            query.id, [make_chat_member_result(config["GROUP_CHAT_ID"])])


if __name__ == '__main__':
    bot.infinity_polling()
