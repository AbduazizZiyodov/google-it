import telebot

from settings import TELEGRAM_API_TOKEN
from utils import get_search_results


bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

blacklist: list = []


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def perform_search(query):
    results: str = get_search_results(query=query)
    if query.query.lower() in blacklist:
        results = "Meni ishga tushurgan ushbu foydalanuvchi yomon so'z aytdi😀"
    content = telebot.types.InlineQueryResultArticle(
        id='1',
        title=f'The search for "{query.query}" is done ✅',
        description='Click me 😊',
        input_message_content=telebot.types.InputTextMessageContent(
                    message_text=results)
    )
    bot.answer_inline_query(query.id, [content])


if __name__ == '__main__':
    bot.infinity_polling()
