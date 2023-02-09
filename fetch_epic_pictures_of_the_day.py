import requests
import os
import datetime

from datetime import datetime
from download_images import download_images
from urllib.parse import urlparse
from dotenv import load_dotenv


def fetch_epic_pictures_of_the_day(api_key_foto):
    nasa_url = "https://api.nasa.gov/EPIC/api/natural/images"
    epic_pictures = get_url(nasa_url).json()

    url_foto_earth = "https://api.nasa.gov/EPIC/archive/natural/2019/05/30/png/epic_1b_20190530011359.png"
    url_foto_earth_split = get_url(url_foto_earth).url.split('/')

    for index_number, index in enumerate(epic_pictures):
        massiv_image = index['image']
        massiv_date = datetime.fromisoformat(index['date'])
        year = massiv_date.strftime("%Y")
        month = massiv_date.strftime("%m")
        day = massiv_date.strftime("%d")
        url_foto_earth_split[6:9] = [year, month, day]
        print(massiv_image)
        disassembled_url = urlparse(url_foto_earth)
        path = disassembled_url.path.split('/')
        path[4:7] = [year, month, day]

        url_foto_earth_split[10] = massiv_image
        print(url_foto_earth_split)
        # url_actual_foto = f"{'/'.join(url_foto_earth_split)}.{url_foto_earth_split[9]}"
        # responce_url_actual_foto = requests.get(url_actual_foto, params=api_key_foto)
        # responce_url_actual_foto.raise_for_status()
        # name_epic_picture_template = os.path.join("epic", """{name}.png""".format(name=massiv_image))
        # download_images(responce_url_actual_foto.url, name_epic_picture_template)


def get_url(url):
    response = requests.get(url, params=input_payload())
    response.raise_for_status()
    return response


def input_payload():
    epic_api_token = 'DEMO_KEY'
    if input() != epic_api_token:
        print("Введите токен:".replace("\r", ""))
        return {"api_key": input()}
    else:
        return {"api_key": epic_api_token}


def main():
    load_dotenv()
    api_key_foto = {'api_key': os.environ['NASA_API_KEY']}
    fetch_epic_pictures_of_the_day(api_key_foto)


if __name__ == '__main__':
    main()
