from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv("TELEGRAM_API_TOKEN")
GROUP_CHAT_ID = getenv("GROUP_CHAT_ID")
CHANNEL_NAME = getenv("CHANNEL_NAME")

GOOGLE_API_KEY = getenv('GOOGLE_API_KEY')
CSE_ID = getenv('CSE_ID')
