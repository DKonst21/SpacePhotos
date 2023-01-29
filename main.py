import telegram
import os
from telegram_bot import take_files


def main():
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])
    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']
    take_files(bot, telegram_chat_id)


if __name__ == '__main__':
    main()
