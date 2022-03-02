import os
import shutil
from PIL import ImageFont
from PIL import Image, ImageDraw, ImageFont
import random
from colour import color_scale, Color
import numpy
import re
red = Color("red")
blue = Color("blue")
color_list = list(red.range_to(blue, 5))


def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


def choose_random_icon():
    choice = random.choice(os.listdir(f'icons'))
    return f'icons/{choice}'


def get_random_color():
    color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
    return color


def get_random_font(text):
    if has_cyrillic(text):
        language = 'Russian'
    else:
        language = 'English'
    choice = random.choice(os.listdir(f'fonts/{language}'))
    return f'fonts/{language}/{choice}'


def background(im, images, i, width=200, fps=24):
    shapes = ['ellipse', 'rectangle']

    draw = ImageDraw.Draw(im)
    center = width // 2

    shape_choice = random.choice(shapes)

    step_size = center // fps
    del_ = i * step_size

    if shape_choice == 'ellipse':

        draw.ellipse((center - del_, center - del_, center + del_, center + del_), fill=get_random_color())
        images.append(im)

    if shape_choice == 'rectangle':

        draw.ellipse((center - del_, center - del_, center + del_, center + del_), fill=get_random_color())
        images.append(im)


def draw_random_shape(im, images, width=200):
    shapes = ['ellipse', 'rectangle', 'line']
    draw = ImageDraw.Draw(im)

    shape_choice = random.choice(shapes)

    if shape_choice == 'ellipse':
        x_up_left = random.randint(0, width)
        y_up_left = random.randint(0, width)

        x_down_right = random.randint(0, width)
        y_down_right = random.randint(0, width)

        r_dev = random.randint(-5, 5)

        draw.ellipse((x_up_left, y_up_left, x_down_right, y_down_right),
                     outline=get_random_color())
        draw.ellipse((x_up_left + r_dev, y_up_left + r_dev, x_down_right + r_dev, y_down_right + r_dev),
                     outline=get_random_color())

    if shape_choice == 'rectangle':
        x_up_left = random.randint(0, width)
        y_up_left = random.randint(0, width)

        x_down_right = random.randint(0, width)
        y_down_right = random.randint(0, width)

        r_dev = random.randint(-5, 5)
        draw.rectangle((x_up_left, y_up_left, x_down_right, y_down_right),
                       outline=get_random_color())
        draw.rectangle((x_up_left + r_dev, y_up_left + r_dev, x_down_right + r_dev, y_down_right + r_dev),
                       outline=get_random_color())

        images.append(im)

    if shape_choice == 'line':
        x_up_left = random.randint(0, width)
        y_up_left = random.randint(0, width)

        x_down_right = random.randint(0, width)
        y_down_right = random.randint(0, width)

        r_dev = random.randint(-5, 5)
        draw.line((x_up_left, y_up_left, x_down_right, y_down_right))
        draw.line((x_up_left + r_dev, y_up_left + r_dev, x_down_right + r_dev, y_down_right + r_dev),
                  width=random.randint(1, 8))


class Gif:

    def __init__(self, text):

        self.text = text
        self.width = 200

    def method1(self):
        images = []
        font = ImageFont.truetype('OpenSans-Light.ttf', size=24)
        center = self.width // 2
        color_1 = get_random_color()
        color_2 = get_random_color()
        max_radius = int(center * 1.5)
        step = 8

        for i in range(0, max_radius, step):
            im = Image.new('RGB', (self.width, self.width), color_1)
            draw = ImageDraw.Draw(im)
            draw.ellipse((center - i, center - i, center + i, center + i), fill=color_2)
            images.append(im)

            center = random.randint(0, 100)

            draw.text((center + 1, center + 1), self.text, get_random_color(), font=font)
            draw.text((center + 0.5, center + 0.5), self.text, get_random_color(), font=font)
            draw.text((center, center), self.text, get_random_color(), font=font)
            images.append(im)

        for i in range(0, max_radius, step):
            im = Image.new('RGB', (self.width, self.width), color_2)
            draw = ImageDraw.Draw(im)
            draw.ellipse((center - i, center - i, center + i, center + i), fill=color_1)
            images.append(im)

            center = random.randint(0, 100)

            draw.text((center + 1, center + 1), self.text, get_random_color(), font=font)
            draw.text((center + 0.5, center + 0.5), self.text, get_random_color(), font=font)
            draw.text((center, center), self.text, get_random_color(), font=font)
            images.append(im)

        images[0].save('pillow_imagedraw.gif',
                       save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)
        return images

    def method2(self):
        images = []

        font = ImageFont.truetype(get_random_font(self.text), size=32)
        center = self.width // 2

        for i in range(0, 5):
            im = Image.new('RGB', (self.width, self.width), get_random_color())
            draw = ImageDraw.Draw(im)

            background(im, images, i=i)

            draw_random_shape(im=im, images=images)

            random_icon_amount = random.randint(1, 4)
            for j in range(0, random_icon_amount):
                png_choice = choose_random_icon()

                with Image.open(png_choice, 'r') as icon:
                    x = random.randint(0, 200)
                    y = random.randint(0, 200)
                    size = random.randint(12, 25)
                    icon = icon.resize((size, size), Image.ANTIALIAS)
                    im.paste(icon, (x, y), mask=icon)
            center = random.randint(0, 100)
            draw.text((center - 0.5*i, center - 0.5*i), self.text, get_random_color(), font=font)
            draw.text((center - 1*i, center - 1*i), self.text, get_random_color(), font=font)

            images.append(im)
        for i in range(6, 11):
            im = Image.new('RGB', (self.width, self.width), get_random_color())
            draw = ImageDraw.Draw(im)

            background(im, images, i=i)

            draw_random_shape(im=im, images=images)

            random_icon_amount = random.randint(1, 4)
            for j in range(0, random_icon_amount):
                png_choice = choose_random_icon()

                with Image.open(png_choice, 'r') as icon:
                    x = random.randint(0, 200)
                    y = random.randint(0, 200)
                    size = random.randint(12, 25)
                    icon = icon.resize((size, size), Image.ANTIALIAS)
                    im.paste(icon, (x, y), mask=icon)
            center = random.randint(0, 100)
            draw.text((center, center), self.text, get_random_color(), font=font)
            draw.text((center + 0.5*i, center - 0.5*i), self.text, get_random_color(), font=font)
            draw.text((center + 1*i, center - 1*i), self.text, get_random_color(), font=font)

            images.append(im)

        for i in range(12, 17):
            im = Image.new('RGB', (self.width, self.width), get_random_color())
            draw = ImageDraw.Draw(im)

            background(im, images, i=i)

            draw_random_shape(im=im, images=images)

            random_icon_amount = random.randint(12, 25)
            for j in range(0, random_icon_amount):
                png_choice = choose_random_icon()

                with Image.open(png_choice, 'r') as icon:
                    x = random.randint(0, 200)
                    y = random.randint(0, 200)
                    size = random.randint(1, 5)
                    icon = icon.resize((size, size), Image.ANTIALIAS)
                    im.paste(icon, (x, y), mask=icon)
            center = random.randint(0, 100)
            draw.text((center + 0.5*i, center + 0.5), self.text, get_random_color(), font=font)
            draw.text((center + 1, center + 1), self.text, get_random_color(), font=font)

            images.append(im)

        for i in range(18, 23):
            im = Image.new('RGB', (self.width, self.width), get_random_color())
            draw = ImageDraw.Draw(im)

            background(im, images, i=i)

            draw_random_shape(im=im, images=images)

            random_icon_amount = random.randint(12, 25)
            for j in range(0, random_icon_amount):
                png_choice = choose_random_icon()

                with Image.open(png_choice, 'r') as icon:
                    x = random.randint(0, 200)
                    y = random.randint(0, 200)
                    size = random.randint(1, 5)
                    icon = icon.resize((size, size), Image.ANTIALIAS)
                    im.paste(icon, (x, y), mask=icon)

            center = random.randint(0, 100)
            draw.text((center - 0.5*i, center + 0.5*i), self.text, get_random_color(), font=font)
            draw.text((center - 1*i, center + 1*i), self.text, get_random_color(), font=font)

            images.append(im)

        gif_name = 'pillow_imagedraw.gif'
        images[0].save(gif_name,
                       save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)
        return gif_name


if __name__ == '__main__':
    Gif('text').method2()
