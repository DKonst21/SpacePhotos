import requests
import os

from download_images import download_images
from telegram_bot import take_files


catalog = 'images'
file_path = 'images/50291306296_85b6ff12a2_o.jpg'


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
    response = requests.get(url)
    response.raise_for_status()
    pictures = response.json()['links']['flickr']['original']

    for picture_number, picture in enumerate(pictures):
        name_picture_template = """spaceX{number}.jpg""".format(number=picture_number)
        picture_for_telegram = os.path.join("images", name_picture_template)
        download_images(picture, picture_for_telegram)
        take_files(catalog)


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
