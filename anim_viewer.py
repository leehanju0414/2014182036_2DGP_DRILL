import os
os.chdir('c:/2014182036_2DGP_DRILL')

from pico2d import *
open_canvas(500, 500)
character = load_image('cookie_run.png')

def anime_draw(f, left, bottom, width, height, x, y):
        clear_canvas()
        character.clip_draw(f * left, bottom, width, height, x, y)
        update_canvas()
        delay(0.08)
        get_events()

frame = 0

while True:
    #sprite_1st_line
    for i in range(0, 12):
        anime_draw(frame, 366, 3285, 365, 365, 250, 300)
        frame = (frame + 1) % 13

    # sprite_2nd_line
    for i in range(0, 7):
        anime_draw(frame, 366, 2920, 365, 365, 250, 300)
        frame = (frame + 1) % 8

    # sprite_3rd_line
    for i in range(0, 8):
        anime_draw(frame, 366, 2555, 365, 365, 250, 300)
        frame = (frame + 1) % 9

    # sprite_4th_line
    for i in range(0, 14):
        anime_draw(frame, 366, 2190, 365, 365, 250, 300)
        frame = (frame + 1) % 15

    # sprite_5th_line
    for i in range(0, 9):
        anime_draw(frame, 366, 1825, 365, 365, 250, 300)
        frame = (frame + 1) % 10

    # sprite_6th_line
    for i in range(0, 9):
        anime_draw(frame, 366, 1460, 365, 365, 250, 300)
        frame = (frame + 1) % 10

    # sprite_7th_line
    for i in range(0, 7):
        anime_draw(frame, 366, 1095, 365, 365, 250, 300)
        frame = (frame + 1) % 8

    # sprite_8th_line
    for i in range(0, 7):
        anime_draw(frame, 366, 730, 365, 365, 250, 300)
        frame = (frame + 1) % 8

    # sprite_9th_line
    for i in range(0, 15):
        anime_draw(frame, 366, 365, 365, 365, 250, 300)
        frame = (frame + 1) % 16

    # sprite_10th_line
    for i in range(0, 7):
        anime_draw(frame, 366, 0, 365, 365, 250, 300)
        frame = (frame + 1) % 4
