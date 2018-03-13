NeocisAssessP1.py and NeocisAssessP2.py are presented for the assessment for Neocis Inc.
Author: Yuqi Cao
Time: Feb. 21st, 2018

//improve introduction: March 12th, 2018
It is written in Pycharm, Python 3.6.1 on Windows
Python 2.* can also be used to compile it as well.

NeocisAssessP1.py is designed for Part 1.
Two modules are imported: tkinter and math.
A blue circle is drawed when user presses and drags mouse's left button.

Circle's center is right at where user presses left button.
Circle's radius equals the distance between circle's center and where user releases mouse's button.
Points correspond to the drawn circle will change blue.
Two additional red circles are generated according to the points correspond to the drawn blue circle.

NeocisAssessP2.py is designed for Part 2.
User presses dots to toggle color between blue and grey.
In the meanwhile, the chosen points (blue ones) are updated in real-time.
When user hits generate button, a circle will be generated according to blue dots.
Points could be deselected when toggle from blue back to grey.
Circle center is the center of gravity of these dots.
Radius is the avarage distance of these dots to circle center.
