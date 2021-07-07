from telebot import TeleBot

from telebot.types import InlineQuery
from telebot.types import InlineQueryResultArticle
from telebot.types import InputTextMessageContent

from utils import check
from utils import get_search_results

from settings import TELEGRAM_API_TOKEN


bot = TeleBot(TELEGRAM_API_TOKEN)


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def perform_search(query: InlineQuery):
    if check(query):
        results: str = get_search_results(query)
    else:
        results: str = '💥'
    content = InlineQueryResultArticle(
        id='1',
        title='The search for "{}" is done ✅'.format(query.query),
        description='Click me if you want to see results😊',
        input_message_content=InputTextMessageContent(
            message_text=results)
    )
    bot.answer_inline_query(query.id, [content])


if __name__ == '__main__':
    bot.infinity_polling()
