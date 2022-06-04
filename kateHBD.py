import os
import random

from color import get_random_color, get_random_font
from handlers.imports import *


def draw_card(text1, text2, text3):

    width = 800
    images = []

    center = width // 2

    color_1 = get_random_color()
    color_2 = get_random_color()

    im = Image.new('RGB', (width, width), color_1)
    draw = ImageDraw.Draw(im)

    center = random.randint(0, 100)

    with Image.open("background.jpg", 'r').convert("RGBA") as photo:
        photo = photo.resize((800, 800), Image.ANTIALIAS)
    mask = Image.new("L", im.size, 128)
    im = Image.composite(im, photo, mask)

    with Image.open("IMG_2431.jpg", 'r').convert("RGBA") as photo:
        photo = photo.resize((400, 400), Image.ANTIALIAS)
        im.paste(photo, (45, 30), mask=photo)

    for icon in os.listdir("icons/kozusha"):
        if str(icon) != ".DS_Store":
            with Image.open(f"icons/kozusha/{icon}", 'r').convert("RGBA") as icon:
                n = random.randint(1, 3)

                for i in range(0, n):
                    size = random.randint(50, 230)
                    pos = (random.randint(100, 700), random.randint(100, 700))

                    icon = icon.resize((size, size), Image.ANTIALIAS)
                    im.paste(icon, pos, icon)

    font = ImageFont.truetype(get_random_font(text1), size=38)
    draw.text((250, 150), text1, get_random_color(), font=font)
    draw.text((252, 152), text1, get_random_color(), font=font)
    draw.text((254, 154), text1, get_random_color(), font=font)

    font = ImageFont.truetype(get_random_font(text1), size=56)
    draw.text((120, 400), text2, get_random_color(), font=font)
    draw.text((126, 406), text2, get_random_color(), font=font)
    draw.text((132, 412), text2, get_random_color(), font=font)

    font = ImageFont.truetype(get_random_font(text1), size=48)
    draw.text((450, 654), text3, get_random_color(), font=font)
    draw.text((452, 654), text3, get_random_color(), font=font)
    draw.text((454, 654), text3, get_random_color(), font=font)



    im.show()


if __name__ == '__main__':
    draw_card('С днем рождения', "логистический бык", "22 годика")
