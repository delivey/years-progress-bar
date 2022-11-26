import datetime
import calendar
import math
from PIL import Image

WIDTH = 1080
HEIGHT = 1080

MARGIN_LEFT = 100
MARGIN_RIGHT = WIDTH - MARGIN_LEFT

MARGIN_TOP = 500
MARGIN_BOTTOM = HEIGHT - MARGIN_TOP

IMAGE_PATH = "./image.png"


def days_in_year():
    year = datetime.datetime.now().year
    return 365 + calendar.isleap(year)


def progress():
    days = days_in_year()
    current_day = int(datetime.datetime.now().strftime('%j'))
    return math.floor(current_day / days * 100)


def generate_image():
    img = Image.new('RGB', (WIDTH, HEIGHT))
    data = img.load()
    percentage = progress()

    percentage_break_off = (WIDTH-MARGIN_LEFT) * percentage/100
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            data[x, y] = (255, 255, 255)
            if MARGIN_RIGHT > x > MARGIN_LEFT and MARGIN_BOTTOM > y > MARGIN_TOP:
                data[x, y] = (0, 255, 0)
                if x > percentage_break_off:
                    data[x, y] = (0, 0, 0)
    img.save(IMAGE_PATH)


generate_image()
