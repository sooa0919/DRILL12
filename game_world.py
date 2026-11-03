world = [[], []]

def add_object(o, depth = 0):
    world[depth].append(o)

def update():
    for layer in world:
        for o in layer[:]:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()