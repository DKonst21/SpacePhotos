import requests
import os

from download_images import download_images, create_directory
from dotenv import load_dotenv


def fetch_nasa_pictures_of_the_day(response):

    nasa_pictures_of_the_day = response.json()
    name_picture_template = """nasa_apod{number}.jpg""".format(number=str(nasa_pictures_of_the_day['date']))
    picture_for_telegram = os.path.join("APOD", name_picture_template)
    download_images(nasa_pictures_of_the_day['url'], picture_for_telegram)


def get_response():
    url = "https://api.nasa.gov/planetary/apod"
    payload = {'api_key': os.environ['NASA_API_KEY']}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response

def main():
    load_dotenv()
    create_directory("APOD")
    fetch_nasa_pictures_of_the_day(get_response())


if __name__ == '__main__':
    main()
