from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400,30)
character.draw_now(400,90)


x = 0
y = 0

while (True):
    
    while(x<800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x = x+2
        delay(0.01)

    while(y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y+2
        delay(0.01)

    while(x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x-2
        delay(0.01)

    while(y>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y-2
        delay(0.01)


    x = 400
    y = 30
    r = 300


    a = 400
    b = 300

    for theta in range(0,360):
        x = a+ r* math.cos(math.radians(theta))
        y = b + r*math.sin(math.radians(theta))
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.01)
    


    
    
close_canvas()
