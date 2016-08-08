### Author: Roderick Hodgson
### Description: Jeff Goldblum is staring at you
### Category: Creative
### License: MIT

import ugfx, pyb, buttons
from imu import IMU

ugfx.init()
imu=IMU()
ugfx.clear()
buttons.init()
ugfx.set_default_font(ugfx.FONT_NAME)
ugfx.display_image(0, 0, "apps/roderickhodgson~goldblum/goldblum.gif")

EYES = ((119, 85), (207, 86))
WHITES = 20
PUPIL = 5
GRAVITY = -1 #1 = googley eyes, -1 = staring into your soul
MAX_ACC = 10

def clamp(val, minmax):
    if val < -minmax:
        val = -minmax
    if val > minmax:
        val = minmax
    return val

while True:
    pyb.wfi()
    ival = imu.get_acceleration()
    xoff = clamp(int(ival['x']*10*GRAVITY), MAX_ACC)
    yoff = clamp(int(ival['y']*10*GRAVITY), MAX_ACC)
    for i in EYES:
        ugfx.fill_circle(i[0], i[1], WHITES, ugfx.WHITE)
        ugfx.fill_circle(i[0]+xoff, i[1]+yoff, PUPIL, ugfx.BLACK)

    if buttons.is_triggered("BTN_MENU") or buttons.is_triggered("BTN_A") or buttons.is_triggered("BTN_B") or buttons.is_triggered("JOY_CENTER"):
        break;

    pyb.delay(100)

ugfx.clear()



