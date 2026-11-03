from pico2d import*
import boy
from grass import Grass
from boy import Boy

import game_world
import grass

def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)

def reset_world():
    global boy

    grass1 = Grass()
    game_world.add_object(grass1, 0)

    grass2 = Grass()
    game_world.add_object(grass2, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

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