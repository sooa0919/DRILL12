from pico2d import*
from grass import Grass

import game_world

def handle_events():
    pass

def reset_world():
    pass

def update_world():
    pass

def render_world():
    pass

running = True

open_canvas()
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)

close_canvas()