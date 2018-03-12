try:
    # Python2
    import Tkinter as tkinter
except ImportError:
    # Python3
    import tkinter
import math
'''
This python file is designed for Neocis Inc Assessment
@author Yuqi Cao
@date Feb 22nd, 2018
interpreter: Python 3.6.1
originally written in PyCharm

'''


def draw_grid():
    for i in range(0, x):
        for j in range(0, y):
            topLeftX = width * (i + 1)
            topLeftY = width * (j + 1)
            bottomRightX = topLeftX + point_size
            bottomRightY = topLeftY + point_size
            c.create_oval(topLeftX, topLeftY, bottomRightX, bottomRightY, fill="grey", state="disabled")


def get_center(event):
    # function get_center is triggered by mouse's left button
    # this function gets the position of mouse when click and set it as circle's center: global centerX, centerY
    global centerX
    centerX = event.x
    global centerY
    centerY = event.y


def draw_circle(event):
    # function draw_circle is used to draw real-time circle when user presses down mouse's left button and drags mouse
    rad = math.sqrt((event.x - centerX) ** 2 + (event.y - centerY) ** 2)
    c.delete('all')
    # draw 20*20 points list
    draw_grid()
    c.create_oval(centerX-rad, centerY-rad, centerX+rad, centerY+rad, width=4, outline='blue')


def mouse_release(event):
    # function mouse_release is used to generate the final blue circle and the two additional circle
    # this function is triggered when left button released

    # offset is used to determine if the point is correspond to the circle drawn by user
    offset = 7
    # final radius for the circle drawn by user
    radFinal = math.sqrt((event.x - centerX) ** 2 + (event.y - centerY) ** 2)
    # initialization for drawing two additional circles
    mindis = radFinal
    maxdis = radFinal

    # create 20*20 points list with grey and blue
    for i in range(0, x):
        for j in range(0, y):
            topLeftX = width * (i + 1)
            topLeftY = width * (j + 1)
            bottomRightX = topLeftX + point_size
            bottomRightY = topLeftY + point_size
            dis = math.sqrt((centerX - topLeftX - point_size/2) ** 2 + (centerY - topLeftY - point_size/2) ** 2)
            if (radFinal-offset) < dis < (radFinal+offset):
                c.create_oval(topLeftX, topLeftY, bottomRightX, bottomRightY, outline="blue", fill="blue")
                if dis > maxdis:
                    maxdis = dis
                elif dis < mindis:
                    mindis = dis
            else:
                c.create_oval(topLeftX, topLeftY, bottomRightX, bottomRightY, fill="grey")

    # draw two additional circles
    c.create_oval(centerX-maxdis, centerY-maxdis, centerX+maxdis, centerY+maxdis, outline="red")
    c.create_oval(centerX-mindis, centerY-mindis, centerX+mindis, centerY+mindis, outline="red")


# initialization for GUI
root = tkinter.Tk()
root.title("Yuqi Cao")
winW = 470  # set window's width
winH = 470  # draw window's height
# initialization for circle's center
centerX = 0
centerY = 0

# use canvas to draw circle
c = tkinter.Canvas(height=winW, width=winW)

# create 20*20 points list
x = 20
y = 20
width = 22  # width between each point
point_size = 6  # size of each point
# call the function draw_grid to draw the 20*20 points
draw_grid()

# bind mouse's actions to functions, click mouse's left button and drag to draw circles
c.bind('<Button-1>', get_center)
c.bind('<B1-Motion>', draw_circle)
c.bind('<ButtonRelease-1>', mouse_release)
c.pack()

root.mainloop()
