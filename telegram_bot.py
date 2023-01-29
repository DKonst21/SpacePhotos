import telegram
import os
import random
import time
import argparse

from dotenv import load_dotenv

time_delay = 4 * 60 * 60


def take_files():
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])
    catalog = "images"
    parser = create_parser()
    namespace = parser.parse_args()
    if namespace.image:
        file = str(os.path.join(str(catalog), namespace.image.split()[0]))
        with open(f"{file}", 'rb') as file:
            bot.send_photo(chat_id=os.environ['TELEGRAM_CHAT_ID'], photo=file)
    else:
        file = os.path.join(str(catalog), random.choice(os.listdir(catalog)))
        with open(f"{file}", 'rb') as file:
            bot.send_photo(chat_id=os.environ['TELEGRAM_CHAT_ID'], photo=file)
            time.sleep(5)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('image', nargs='?')

    return parser


def main():
    load_dotenv()
    take_files()


if __name__ == '__main__':
    main()
