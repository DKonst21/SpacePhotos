import requests
import os

from download_images import download_images
from urllib.parse import urlparse
from telegram_bot import TakeFiles


catalog = 'epic'
url_nasa = "https://api.nasa.gov/EPIC/api/natural/images"
payload = {'api_key': os.environ['api_key']}
response = requests.get(url_nasa, params=payload)
response.raise_for_status()
Epic_pictures = response.json()

url_foto_earth = "https://api.nasa.gov/EPIC/archive/natural/2019/05/30/png/epic_1b_20190530011359.png?api_key=DEMO_KEY"
url_foto_earth_split = url_foto_earth.split('/')


def fetch_epic_pictures_of_the_day():
        
    for index in range(len(Epic_pictures)): 
        massiv_image = Epic_pictures[index]['image']
        massiv_date = Epic_pictures[index]['date']
 
        url_foto_earth_split[6] = massiv_date.split('-')[0]
        url_foto_earth_split[7] = massiv_date.split('-')[1]
        value_day = massiv_date.split('-')[2]
        url_foto_earth_split[8] = value_day.split(' ')[0]
        disassembled_url = urlparse(url_foto_earth)
        path = disassembled_url.path.split('/')
        path[4:7] = url_foto_earth_split[6:9]
           
        url_foto_earth_split[10] = massiv_image
        url_actual_foto = '/'.join(url_foto_earth_split)+'.'+url_foto_earth_split[9] + "?api_key=DEMO_KEY"
        name_epic_picture_template = """epic/{name}.png""".format(name=massiv_image)
        download_images(url_actual_foto, name_epic_picture_template)
        TakeFiles(catalog)


fetch_epic_pictures_of_the_day()
