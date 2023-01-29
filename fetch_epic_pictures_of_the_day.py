import requests
import os

from datetime import datetime
from download_images import download_images
from urllib.parse import urlparse


def fetch_epic_pictures_of_the_day():
    url_nasa = "https://api.nasa.gov/EPIC/api/natural/images"
    epic_pictures = get_url(url_nasa).json()

    url_foto_earth = "https://api.nasa.gov/EPIC/archive/natural/2019/05/30/png/epic_1b_20190530011359.png"
    url_foto_earth_split = get_url(url_foto_earth).url.split('/')

    for index_number, index in enumerate(epic_pictures):
        massiv_image = index['image']
        massiv_date = (datetime.fromisoformat(index['date']))
        url_foto_earth_split[6] = str(massiv_date.year)
        url_foto_earth_split[7] = str(massiv_date.month)
        url_foto_earth_split[8] = str(massiv_date.day)
        disassembled_url = urlparse(url_foto_earth)
        path = disassembled_url.path.split('/')
        path[4:7] = url_foto_earth_split[6:9]

        url_foto_earth_split[10] = massiv_image
        api_key_foto = {'api_key': os.environ['NASA_API_KEY']}
        url_actual_foto = f"{'/'.join(url_foto_earth_split)}.{url_foto_earth_split[9]}"
        responce_url_actual_foto = requests.get(url_actual_foto, params=api_key_foto)
        responce_url_actual_foto.raise_for_status()
        name_epic_picture_template = os.path.join("images", """{name}.png""".format(name=massiv_image))
        download_images(responce_url_actual_foto.url, name_epic_picture_template)

def get_url(url):
    payload = {"api_key": 'DEMO_KEY'}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response

def main():
    fetch_epic_pictures_of_the_day()


if __name__ == '__main__':
    main()
