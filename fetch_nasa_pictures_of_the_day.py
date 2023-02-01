import requests
import os

from download_images import download_images
from dotenv import load_dotenv


def fetch_nasa_pictures_of_the_day():
    url = "https://api.nasa.gov/planetary/apod"
    nasa_pictures_of_the_day = get_url(url).json()

    for picture_number in enumerate(nasa_pictures_of_the_day):
        name_picture_template = """nasa_apod{number}.jpg""".format(number=picture_number)
        picture_for_telegram = os.path.join("APOD", name_picture_template)
        download_images(nasa_pictures_of_the_day['url'], picture_for_telegram)


def get_url(url):
    payload = {'api_key': os.environ['NASA_API_KEY']}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response


def main():
    load_dotenv()
    fetch_nasa_pictures_of_the_day()


if __name__ == '__main__':
    main()
