from fetch_spacex_images import fetch_spacex_last_launch
from fetch_nasa_pictures_of_the_day import fetch_nasa_pictures_of_the_day
from fetch_epic_pictures_of_the_day import fetch_epic_pictures_of_the_day

def main():
    fetch_spacex_last_launch()
    fetch_nasa_pictures_of_the_day()
    fetch_epic_pictures_of_the_day()


if __name__ == '__main__':
    main()
