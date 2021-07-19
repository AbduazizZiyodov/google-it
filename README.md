# 🔥Google-it Telegram Bot

> `Google Search` from telegram bot 😀 (bot works inline)

For using this bot you need to place your group id in your environment. Bot checks its users for a member of your group. Users have to be members of your group for using the bot's functionality! If the user is not a member of your group, the bot automatically sends a message to the user about it.

## **Setup**

Clone this repo:

```bash
$ git clone https://github.com/AbduazizZiyodov/google-it.git
$ cd google-it/
```

Activate virtual enviroment:

```bash
$ python -m venv env
$ source env/bin/activate
```

Install all requirements from file:

```
$ pip install -r requirements.txt
```

On `.env`(dotenv file) write your keys:

```bash
# Telegram bot token

TELEGRAM_API_TOKEN = ""

# Search Engine Keys
GOOGLE_API_KEY = ""
CSE_ID = ""

# Your Group ID : integer or string
GROUP_CHAT_ID = ""

# Your Channel ID (OPTIONAL): integer or string

CHANNEL_ID = ""
```

## **Running**

```bash
$ python bot.py
```

Bot Usage:

After the username of your bot, write some search terms:

![BOT_USAGE_1](screenshots/1.PNG)

If search is done , you can see an inline message from the bot. Then you should click it and search results will be sent in your chat.

![BOT_USAGE_2](screenshots/2.PNG)

Abduaziz Ziyodov🎯
