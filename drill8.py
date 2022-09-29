from pico2d import *

open_canvas(1280, 1024)
ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running
    global xdir, ydir
    global cdir #character_dir__1=right,0=left

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                xdir += 1
                cdir = 1
            elif event.key == SDLK_LEFT:
                xdir -= 1
                cdir = 0
            elif event.key == SDLK_UP:
                ydir += 1
            elif event.key == SDLK_DOWN:
                ydir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                xdir -= 1
            elif event.key == SDLK_LEFT:
                xdir += 1
            elif event.key == SDLK_UP:
                ydir -= 1
            elif event.key == SDLK_DOWN:
                ydir += 1


def animation_draw(left, bottom, width, height, x, y, imgcnt):
    global frame
    clear_canvas()
    ground.draw(640,512)
    character.clip_draw(frame * left, bottom, width, height, x, y)
    frame = (frame + 1) % imgcnt
    update_canvas()
    delay(0.05)


running = True
x = 1280 // 2
y = 1024 // 2
frame = 0
xdir = 0
ydir = 0
cdir = 0

while running:
    #left_move_x-axis
    if (cdir == 0 and xdir < 0):
        animation_draw(100, 0, 100, 100, x, y, 8)
        handle_events()
        if (0 < x-10 < 1280):
            x += xdir * 10

    #right_move_x-axis
    elif (cdir == 1 and xdir > 0):
        animation_draw(100, 100, 100, 100, x, y, 8)
        handle_events()
        if (0 < x+10 < 1280):
            x += xdir * 10

    #left_idle
    elif(cdir == 0 and xdir == 0 and ydir == 0):
        animation_draw(100, 200, 100, 100, x, y, 8)
        handle_events()

    #right_idle
    elif(cdir == 1 and xdir == 0 and ydir == 0):
        animation_draw(100, 300, 100, 100, x, y, 8)
        handle_events()

    #left_move_y-axis
    elif (cdir == 0 and ydir != 0):
        animation_draw(100, 0, 100, 100, x, y, 8)
        handle_events()
        if ydir > 0 and (0 < y+10 < 1024):
            y += ydir * 10
        elif ydir < 0 and (0 < y-10 < 1024):
            y += ydir * 10

    #right_move_y-axis
    elif (cdir == 1 and ydir != 0):
        animation_draw(100, 100, 100, 100, x, y, 8)
        handle_events()
        if ydir > 0 and (0 < y+10 < 1024):
            y += ydir * 10
        elif ydir < 0 and (0 < y-10 < 1024):
            y += ydir * 10




