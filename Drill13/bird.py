from pico2d import *
import game_framework
import random


PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class Bird:

    def __init__(self):
        self.x, self.y = random.randint(100,300), random.randint(300, 400)
        self.frame = 0
        self.dir = 1
        self.face_dir = 1
        self.image = load_image('bird_animation.png')

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 1600)
        if self.x == 1600:
            self.dir = -1
        elif self.x == 0:
            self.dir = 1

    def draw(self):
        if self.dir == -1:
            self.image.clip_composite_draw(int(self.frame) * 182, 340, 182, 160,
                                           0, 'h', self.x, self.y, 100, 100)
        else:
            self.image.clip_composite_draw(int(self.frame) * 182, 340, 182, 160,
                                           0, '', self.x, self.y, 100, 100)
