import telegram
import time
import schedule
import os

from dotenv import load_dotenv

load_dotenv()

bot = telegram.Bot(token=os.environ['token'])
time_delay = 240
# print(bot.get_me())

# bot.send_message(chat_id='@space_photos_test', text="Здесь будут появляться картинки космоса")


def TakeFiles(catalog):
    global file, name
    filesindir = os.listdir(catalog)
    for filesindirs in filesindir:
        path = os.path.join(filesindirs)
        file = os.path.join(str(catalog), path)
        while True:
            schedule.run_pending()
            schedule.every(time_delay).minutes.do(bot.send_photo(chat_id=os.environ['chat_id'],
                                                                 photo=open(f"{file}", 'rb')))
            time.sleep(5)

# random.shuffle(lst)
# request = f"https://api.telegram.org/bot{token}/{picture_for_telegram}"
