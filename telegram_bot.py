import telegram
import os

from dotenv import load_dotenv

load_dotenv()

bot = telegram.Bot(token=os.environ['NASA_TOKEN'])
time_delay = 240


def take_files(catalog):
    global file, name
    filesindir = os.listdir(catalog)
    for filesindirs in filesindir:
        path = os.path.join(filesindirs)
        file = os.path.join(str(catalog), path)

        with open(f"{file}", 'rb') as file:
            bot.send_photo(chat_id=os.environ['CHAT_ID'], photo=file)
