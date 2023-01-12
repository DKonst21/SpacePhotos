import requests


def download_images(url, file_path):

    response = requests.get(url)
    response.raise_for_status()
    
    with open(file_path, 'wb') as file:
        return file.write(response.content)

# def file_extension(url):
#     parse_name = urllib.parse.urlparse(url)
#     extension = path.splitext(parse_name.path)[1]
#     return extension
