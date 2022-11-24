import random
from pico2d import *
import game_world
import game_framework
import server

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, server.background.image.w - 1), random.randint(0, server.background.image.h - 1), 0

    def get_bb(self):
        # fill here
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x - server.background.window_left, self.y - server.background.window_bottom)

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

    def stop(self):
        self.fall_speed = 0

    def handle_collision(self, other, group):
        game_world.remove_object(self)
