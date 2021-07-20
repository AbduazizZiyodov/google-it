from time import sleep

from sentry_sdk import init

from telebot import TeleBot
from telebot.types import Message
from telebot.types import InlineQuery

from settings import BOT_TOKEN as token
from settings import SENTRY_DSN

from utils import save
from utils import check
from utils import get_random_meme
from utils import make_query_result
from utils import get_search_results
from utils import check_group_member
from utils import make_chat_member_result


bot = TeleBot(token)
init(SENTRY_DSN)

print('Bot is started!')


@bot.message_handler(['start'])
def welcome(message: Message) -> None:
    image = open('images/{}'.format(get_random_meme()), 'rb')
    bot.send_photo(chat_id=message.chat.id, photo=image,
                   caption="Learn to search from Google🙂\n#random_meme")
    image.close()


@bot.inline_handler(lambda query: len(query.query) > 5)
def perform_search(query: InlineQuery) -> None:
    save(query, bot)
    if check_group_member(bot, query.from_user.id):
        sleep(3)
        results: str = get_search_results(query) if check(query) else '💥'
        bot.answer_inline_query(query.id, [make_query_result(results, query)])
    else:
        bot.answer_inline_query(
            query.id, [make_chat_member_result()])


if __name__ == '__main__':
    bot.infinity_polling()

