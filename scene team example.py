#Assignment
"""
During this prove milestone and the next prove assignment, you will write a Python program that draws a semi-realistic outdoor scene in a computer window.
Your program can draw any outdoor scene that you like as long as it meets these requirements:

The scene must be outdoor and include part of the sky.
The sky must have clouds.
The scene must include repetitive objects, such as blades of grass, trees, leaves on a tree, birds, flowers, insects, fish, pickets in a fence,
dashed lines on a road, buildings, bales of hay, snowmen, snowflakes, or icicles.
Your program must be divided into functions such as draw_sky, draw_cloud, draw_ground, draw_bird, draw_flower, draw_insect, draw_fish, or draw_snowman. 
Each of the objects in your scene should be drawn in its own function. To draw the shapes in the scene, your program will call functions in a Python library named Draw 2-D.

During this milestone, you will write code that draws the sky, the ground, and clouds in your scene. 
    During the next prove assignment, you will write code that completes your scene. 
As you write your program, write it so that it draws objects in the order of farthest away to nearest. 
    For example, you program should draw the sky first, then clouds, then the ground, then trees, then insects in the trees. Be creative.
"""

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, draw_polygon, \
    draw_rectangle, draw_text, finish_drawing
import random

def main():
    # Width and height of the scene in pixels
    scene_width = random.randint(800, 1900)
    scene_height = random.randint(500, 1000)

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    # Starting at line 31 of your new program, write your functions to draw the sky, ground, and clouds.

    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    

    #calls to your drawing functions.
    wide = random.randint(0, round(scene_width/5))
    for _ in range(random.randint(2, 10)):
        draw_shark(canvas, wide, random.randint(0, round(scene_height/3)))
        wide += 125 + random.randint(0, 10)

    #grid if needed to help
    #draw_grid(canvas, scene_width, scene_height, 50)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, round(scene_height/2), scene_width, scene_height, width=1, outline="black", fill="cyan1")
    draw_stars(canvas,scene_width,scene_height)
    draw_sun(canvas,scene_width,scene_height)
    draw_clouds(canvas, scene_width, scene_height)

def draw_sea(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height/2, width=1, outline="blue3", fill="blue3")
    draw_waves(canvas, scene_width, scene_height)
    draw_pelican(canvas, scene_width, scene_height)

def draw_waves(canvas, scene_width, scene_height):
    draw_arc(canvas, round(100/800*scene_width), round(50/500*scene_height), round(300/800*scene_width), round(75/500*scene_height), start=25, extent=135, outline="white")
    draw_arc(canvas, round(550/800*scene_width), round(70/500*scene_height), round(750/800*scene_width), round(95/500*scene_height), start=25, extent=135, outline="white")
    draw_arc(canvas, round(320/800*scene_width), round(125/500*scene_height), round(420/800*scene_width), round(145/500*scene_height), start=25, extent=135, outline="white")
    draw_arc(canvas, round(0/800*scene_width), round(135/500*scene_height), round(120/800*scene_width), round(155/500*scene_height), start=25, extent=135, outline="white")
    draw_arc(canvas, round(100/800*scene_width), round(200/500*scene_height), round(180/800*scene_width), round(225/500*scene_height), start=25, extent=135, outline="white")
    draw_arc(canvas, round(425/800*scene_width), round(180/500*scene_height), round(505/800*scene_width), round(205/500*scene_height), start=25, extent=135, outline="white")
    draw_arc(canvas, round(650/800*scene_width), round(200/500*scene_height), round(730/800*scene_width), round(225/500*scene_height), start=25, extent=135, outline="white")

def draw_pelican(canvas, scene_width, scene_height):
   draw_arc(canvas, round(425/800*scene_width), round(180/500*scene_height), round(505/800*scene_width), round(205/500*scene_height), start=25, extent=135, outline="black")
   draw_arc(canvas, round(650/800*scene_width), round(200/500*scene_height), round(730/800*scene_width), round(225/500*scene_height), start=25, extent=135, outline="black")


def draw_ground(canvas, scene_width, scene_height):
    draw_sea(canvas, scene_width, scene_height)

def draw_cloud(canvas, scene_width, scene_height):
    draw_oval(canvas, scene_width, scene_height+10, scene_width+170, scene_height+60, outline="gray99", fill="gray99")
    draw_oval(canvas, scene_width+25, scene_height+20, scene_width+170, scene_height+70, outline="gray99", fill="gray99")
    draw_oval(canvas, scene_width+50, scene_height+30, scene_width+170, scene_height+80, outline="gray99", fill="gray99")
    draw_oval(canvas, scene_width+75, scene_height+40, scene_width+170, scene_height+90, outline="gray99", fill="gray99")
    draw_oval(canvas, scene_width+100, scene_height+50, scene_width+170, scene_height+100, outline="gray99", fill="gray99")
    draw_oval(canvas, scene_width+50, scene_height+10, scene_width+200, scene_height+50, outline="gray99", fill="gray99")
    draw_oval(canvas, scene_width+30, scene_height+75, scene_width+150, scene_height, outline="gray99", fill="gray99")
    draw_oval(canvas, scene_width, scene_height+10, scene_width+170, scene_height+60, outline="gray99", fill="gray99")
    draw_oval(canvas, scene_width+25, scene_height+50, scene_width+150, scene_height+100, outline="gray99", fill="gray99")
    draw_oval(canvas, scene_width+10, scene_height+25, scene_width+100, scene_height+80, outline="gray99", fill="gray99")
    draw_oval(canvas, scene_width+100, scene_height+30, scene_width+225, scene_height+80, outline="gray99", fill="gray99")

def draw_shark(canvas, scene_width, scene_height):
    draw_oval(canvas, scene_width, scene_height, scene_width+90, scene_height+25, outline="white", fill="blue2")
    bs = scene_width+20
    be = scene_width+145
    for i in range(50):
        draw_arc(canvas, bs, scene_height-55, be, scene_height+70, start=90, extent=85, outline="seashell3", width=2)
        bs = bs + 1
        be = be - 1
        

def draw_clouds(canvas, scene_width, scene_height):
    for _ in range(random.randint(5, 8)):
        x = random.randint(0, scene_width)
        y = random.randint(round(scene_height/3), scene_height)
        draw_cloud(canvas, x, y)

def draw_stars(canvas,scene_width,scene_height):
    for _ in range(100):
        x = random.randint(0, scene_width)
        y = random.randint(round(scene_height/2), scene_height)
        draw_text(canvas, x, y, "*", fill="gold1")

def draw_sun(canvas,scene_width,scene_height):
        x = random.randint(0, scene_width)
        y = random.randint(round(scene_height/3), scene_height)
        diameter = random.randint(100, 300)
        draw_oval(canvas, x, y, x+diameter, y+diameter, outline="gold1", fill="gold1")

def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)

#    draw_line(canvas, 0, 5, 100, 50, width=10, fill="blue")

# Call the main function so that
# this program will start executing.
main()