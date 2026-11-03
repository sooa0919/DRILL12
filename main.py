from pico2d import*
import boy
from grass import Grass1
from grass import Grass2
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

    grass1 = Grass1()
    game_world.add_object(grass1, 0)

    grass2 = Grass2()
    game_world.add_object(grass2, 1)

    boy = Boy()
    game_world.add_object(boy, 0)

def update_world():
    game_world.update()

def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()

running = True

open_canvas()
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)

close_canvas()