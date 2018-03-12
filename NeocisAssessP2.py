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
    # this function is used to draw 20*20 grey points
    for i in range(0, x):
        for j in range(0, y):
            topLeftX = width * (i + 1)
            topLeftY = width * (j + 1)
            bottomRightX = topLeftX + point_size
            bottomRightY = topLeftY + point_size
            c.create_oval(topLeftX, topLeftY, bottomRightX, bottomRightY, fill="grey", state="normal", tag='dot')


def toggle_color(event):
    # this function is used to toggle between blue and grey
    # in the meanwhile, it will update dot_list in real-time in order to generate a circle
    click_dot = event.widget.find_closest(event.x, event.y)
    color = c.itemcget(click_dot, "fill")
    dot_coords = c.coords(click_dot)
    dot_x = dot_coords[0]
    dot_y = dot_coords[1]
    # print (dot_x, dot_y)
    if color == "grey":
        c.itemconfig(click_dot, fill="blue")
        dot_list.append((dot_x + point_size / 2, dot_y + point_size / 2))
    elif color == "blue":
        c.itemconfig(click_dot, fill="grey")
        dot_list.remove((dot_x + point_size / 2, dot_y + point_size / 2))
    # print (dot_list)


def generate_circle(event):
    x = event.x
    l = len(dot_list)
    # calculate circle center
    sumx = 0
    sumy = 0
    for i in range(0, l):
        sumx = sumx + dot_list[i][0]
        sumy = sumy + dot_list[i][1]
    centerX = sumx/l
    centerY = sumy/l
    # print (centerX, centerY)
    # calculate radius
    # rsqrt_list = []
    sumr = 0
    for i in range(0, l):
        r = math.sqrt((centerX - dot_list[i][0])**2 + (centerY - dot_list[i][1])**2)
        # rsqrt_list.append(math.sqrt((centerX - dot_list[i][0])**2 + (centerY - dot_list[i][1])**2))
        sumr = sumr + r
    rad = sumr/l
    c.create_oval(centerX - rad, centerY - rad, centerX + rad, centerY + rad, width=4, outline='blue')
    # print (l, rad)

# initialization for GUI window
root = tkinter.Tk()
root.title("Yuqi Cao")
winW = 470  # set window's width
winH = 470  # draw window's height

# initiate the dot list used to generate circle
dot_list = []

# initiate parameter used to create 20*20 points list
x = 20
y = 20
width = 22  # width between each point
point_size = 6  # size of each point

# use canvas to draw
c = tkinter.Canvas(height=winW, width=winW)
# cir = c.create_oval(50, 50, 400, 400, outline='blue', width=5, state="hidden")
# c.itemconfig(cir, state="normal")

# call function draw_grid to draw 20*20 points using
draw_grid()
# call function toggle_color as long as mouse hit points
c.tag_bind("dot", "<Button-1>", toggle_color)

c.pack()


# generate button
button = tkinter.Button(root, text="generate")
button.bind("<Button-1>", generate_circle)
button.pack(side="bottom")


root.mainloop()
