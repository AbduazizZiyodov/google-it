from os import getenv
from dotenv import load_dotenv

load_dotenv()

config: dict = {
    "BOT_TOKEN": getenv("TELEGRAM_API_TOKEN"),

    "GOOGLE_API_KEY": getenv('GOOGLE_API_KEY'),
    "CSE_ID": getenv('CSE_ID'),

    "GROUP_CHAT_ID": getenv("GROUP_CHAT_ID"),
}
