import os
import sys
import re
from PIL import Image, ImageDraw
from datetime import datetime

base_dir = os.path.dirname(__file__)
base_image_path = os.path.join(base_dir, "img", "base.png")
result_image_path = os.path.join(base_dir, "img", "result.png")


def draw_unit(unit, xs, y, size, accent_color="#FF2536"):
    print(unit)
    dots = bin(int(unit))[2:].zfill(len(xs))
    print(dots)
    for dot, x in zip(dots, xs):
        color = accent_color if dot == "1" else "#807675"
        draw.rectangle((x, y, x + size, y + size), fill=color)


time = datetime.now().strftime("%I:%M:%p")
hour, minute, am_pm = time.split(":")
am_pm = am_pm == "PM"

accent_color = "#FF2536"
args = sys.argv[1:]
if len(args) != 0:
    try:
        if args[0] == "--color":
            accent_color = args[1]
    except IndexError:
        print('error: Invalid command line arguments, using default color value')

hour_xs = [543, 733, 940, 1133]
hour_y = 292

minute_xs = [586, 802, 1003, 1177, 1344, 1509]
minute_y = 627

size = 100

im = Image.open(base_image_path)
draw = ImageDraw.Draw(im)

draw_unit(hour, hour_xs, hour_y, size, accent_color)
draw_unit(minute, minute_xs, minute_y, size, accent_color)
draw_unit(am_pm, [1560], 157, size, accent_color)

im.save(result_image_path, quality=95)
