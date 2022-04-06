import os
from PIL import Image, ImageDraw
from datetime import datetime

base_dir = os.path.dirname(__file__)
base_image_path = os.path.join(base_dir, "base.png")
result_image_path = os.path.join(base_dir, "result.png")


def draw_unit(unit, xs, y, size):
    print(unit)
    dots = bin(int(unit))[2:].zfill(len(xs))
    print(dots)
    for dot, x in zip(dots, xs):
        color = "#FF2536" if dot == "1" else "#807675"
        draw.rectangle((x, y, x + size, y + size), fill=color)


time = datetime.now().strftime("%I:%M:%p")
hour, minute, am_pm = time.split(":")
am_pm = am_pm == "PM"


hour_xs = [543, 733, 940, 1133]
hour_y = 292

minute_xs = [586, 802, 1003, 1177, 1344, 1509]
minute_y = 627

size = 100

im = Image.open(base_image_path)
draw = ImageDraw.Draw(im)

draw_unit(hour, hour_xs, hour_y, size)
draw_unit(minute, minute_xs, minute_y, size)
draw_unit(am_pm, [1560], 157, size)

im.save(result_image_path, quality=95)
