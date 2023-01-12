import requests
import os

from download_images import download_images
from telegram_bot import TakeFiles


catalog = 'APOD'
url = "https://api.nasa.gov/planetary/apod"
payload = {'api_key': os.environ['api_key']}
response = requests.get(url, params=payload)
response = requests.get(url)
response.raise_for_status()
Nasa_pictures_of_the_day = response.json()['url']

def fetch_nasa_pictures_of_the_day():
    for picture_number, picture in enumerate(Nasa_pictures_of_the_day):
        name_picture_template = """APOD/nasa_apod{number}.jpg"""
        picture_for_telegram = name_picture_template.format(number=picture_number)
        download_images(picture, picture_for_telegram)
        TakeFiles(catalog)


fetch_nasa_pictures_of_the_day()
