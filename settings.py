from os import getenv
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_TOKEN: str = getenv("TELEGRAM_API_TOKEN")

GOOGLE_API_KEY: str = getenv('GOOGLE_API_KEY')
CSE_ID: str = getenv('CSE_ID')
