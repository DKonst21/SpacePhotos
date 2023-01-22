import requests
import os

from download_images import download_images
from urllib.parse import urlparse
from telegram_bot import take_files


def fetch_epic_pictures_of_the_day():
    catalog = 'epic'
    url_nasa = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {'api_key': os.environ['NASA_API_KEY']}
    response = requests.get(url_nasa, params=payload)
    response.raise_for_status()
    epic_pictures = response.json()

    url_foto_earth = "https://api.nasa.gov/EPIC/archive/natural/2019/05/30/png/epic_1b_20190530011359.png?api_key=DEMO_KEY"
    url_foto_earth_split = url_foto_earth.split('/')

    for index in range(len(epic_pictures)):
        massiv_image = epic_pictures[index]['image']
        massiv_date = epic_pictures[index]['date']

        url_foto_earth_split[6] = massiv_date.split('-')[0]
        url_foto_earth_split[7] = massiv_date.split('-')[1]
        value_day = massiv_date.split('-')[2]
        url_foto_earth_split[8] = value_day.split(' ')[0]
        disassembled_url = urlparse(url_foto_earth)
        path = disassembled_url.path.split('/')
        path[4:7] = url_foto_earth_split[6:9]

        url_foto_earth_split[10] = massiv_image
        api_key_foto = {'api_key': 'DEMO_KEY'}
        url_actual_foto = f"{'/'.join(url_foto_earth_split)}.{url_foto_earth_split[9]}"
        responce_url_actual_foto = requests.get(url_actual_foto, params=api_key_foto)
        responce_url_actual_foto.raise_for_status()
        name_epic_picture_template = os.path.join("epic", """{name}.png""".format(name=massiv_image))
        download_images(responce_url_actual_foto.url, name_epic_picture_template)
        take_files(catalog)


def main():
    fetch_epic_pictures_of_the_day()


if __name__ == '__main__':
    main()
