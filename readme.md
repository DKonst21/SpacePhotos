# Космический Телеграм
Программа по скачиванию с сайтов и загрузки в телеграм-канал картинок космоса 

## Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.

## Конфигурация проекта
Для работы с API NASA потребуется:

- получить API Key на сайте https://api.nasa.gov/ , пройдя регистрацию;
- получить Token.
- Прописать в файле .env следующие ключи:

NASA_TOKEN=полученный с сайта NASA токен;
NASA_API_KEY=ключ, полученный при регистрации;
CHAT_ID=ID телеграм-канала, в который будут загружатся фотографии.

### [fetch_epic_pictures_of_the_day.py](fetch_epic_pictures_of_the_day.py)
С помощью этого файла можно скачать и загрузить файлы в телеграм канал с сайта NASA (https://api.nasa.gov/) с эпическими изображениями нашей планеты. Запустить скрипт можно в терминале с помощью команды:
```
python fetch_epic_pictures_of_the_day.py
```
### [fetch_nasa_pictures_of_the_day.py](fetch_nasa_pictures_of_the_day.py)
С помощью этого файла можно скачать и загрузить файлы в телеграм-канал с сайта NASA (https://api.nasa.gov/) лучшие картинки дня. Запустить скрипт можно в терминале с помощью команды:
```
python fetch_nasa_pictures_of_the_day.py
```
### [fetch_spacex_images.py](fetch_spacex_images.py)
С помощью этого файла можно скачать и загрузить файлы в телеграм-канал с сайта SpaceX (https://www.spacex.com/) с фотографиями последнего запуска космического корабля. Запустить скрипт можно в терминале с помощью команды:
```
python fetch_spacex_images.py
```
### [main.py](main.py)
С помощью этого файла можно скачать и загрузить файлы в телеграм-канал, которые хранятся в проекте, либо были загружены ранее.
```
python main.py
```
### [download_images.py](download_images.py)
Содержит общую функцию по скачиванию картинок по url-адресу.

### [telegram_bot.py](telegram_bot.py)
В файле содержится настойка частоты скачивания картинок time_delay. По умолчанию - 4 часа.
Выполните команду
```
python telegram_bot.py
```
и программа отправит рандомную картинку в телеграм канал. Если добавить к команде название конкретной картинки, то в канал выгрузиться именно она.
