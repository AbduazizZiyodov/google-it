import telebot

from os import getenv

from dotenv import load_dotenv

from core import googleit


load_dotenv()

TELEGRAM_API_TOKEN: str = getenv("TELEGRAM_API_TOKEN")
bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

blacklist: list = []


def get_search_results(query: telebot.types.InlineQuery) -> str:
    query, results = query.query.lower(), "[🔍Search results🤓]\n\n"
    total: int = 0
    for index, result in enumerate(googleit(term=query)):
        results += f'🔰{index+1}) {result}\n'
        total += 1
    return results


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
