import requests
from lxml import html
from os import path, makedirs
from pathlib import Path
import threading


def download_images(letter: str):
    url = f"http://www.desaparecidos.org/arg/victimas/{letter}/todos/"
    response = requests.get(url)
    try:
        tree = html.fromstring(response.content)
    except: # Empty document
        return

    images = []
    tr_elements = tree.xpath('//tr')

    for tr in tr_elements[3:]:
        
        try:
            text = tr[1].text_content()
            if str(text).endswith('.jpg'):
                images.append(f'{url}{str(text)}')
                response = requests.get(f'{url}{str(text)}')
                if not path.exists(f'images/{letter}'):
                    makedirs(f'images/{letter}')
                with open(f'images/{letter}/{text}', 'wb') as file:
                    file.write(response.content)
        except(IndexError):
            pass


    

    print(images)


for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
    thread = threading.Thread(target=download_images, args=[letter])
    thread.start()

