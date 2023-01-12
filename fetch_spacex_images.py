import requests

from download_images import download_images
from telegram_bot import takeFiles


catalog='images'
file_path = 'images/50291306296_85b6ff12a2_o.jpg'
url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
response = requests.get(url)
response.raise_for_status()
Pictures=response.json()['links']['flickr']['original']

def fetch_spacex_last_launch():

    for picture_number, picture in enumerate(Pictures):
        name_picture_template = """images/spaceX{number}.jpg"""
        picture_for_telegram = name_picture_template.format(number=picture_number)
        download_images(picture, picture_for_telegram)
        # takeFiles(catalog)
