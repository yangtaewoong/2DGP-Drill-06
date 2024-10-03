from pico2d import *
from random import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

def arrow_events():
    global ax,ay
    ax = randint(10,TUK_WIDTH - 50 )
    ay = randint(10, TUK_HEIGHT - 50)

def move_character():
    global x,y,arrow_x, arrow_y
    speed = 0.1
    if x < arrow_x:
        x += min(speed, arrow_x - x)
    elif x > arrow_x:
        x -= min(speed, x - arrow_x)

    if y < arrow_y:
        y += min(speed, arrow_y - y)
    elif y > arrow_y:
        y -= min(speed, y - arrow_y)

    if x == arrow_x and y == arrow_y:
        delay(0.5)
        arrow_events()
        arrow_x, arrow_y = ax, ay



running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
arrow_x, arrow_y = x, y
frame = 0
ax, ay =0, 0
arrow_events()
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if x<= arrow_x:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif x> arrow_x:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    arrow.draw(ax, ay)
    update_canvas()
    frame = (frame + 1) % 8
    move_character()

close_canvas()




