import requests
import os
import argparse

from download_images import download_images
from urllib.parse import urlparse


catalog = 'images'
file_path = 'images/50291306296_85b6ff12a2_o.jpg'


def fetch_spacex_last_launch():

    for picture_number, picture in enumerate(create_response()):
        name_picture_template = """spaceX{number}.jpg""".format(number=picture_number)
        picture_for_telegram = os.path.join("images", name_picture_template)
        download_images(picture, picture_for_telegram)


def create_response():
    url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
    path_url = urlparse(url).path.split('/')
    launch_id = get_launch_id()
    if launch_id == path_url[3]:
        response = requests.get(f"""https://api.spacexdata.com/v5/launches/{launch_id}""".format(path=path_url))
    else:
        response = requests.get(f"""https://api.spacexdata.com/v5/launches/{input()}""".format(path=input()))
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def get_launch_id():
    parser = argparse.ArgumentParser()
    parser.add_argument('launch_id', default="5eb87d47ffd86e000604b38a",
                        help="Введите lauch_id. Например: 5eb87d47ffd86e000604b38a")
    args = parser.parse_args()
    return args.launch_id


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
