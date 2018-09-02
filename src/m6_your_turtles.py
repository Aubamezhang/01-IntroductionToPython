"""w
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Jake Zhang
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('midnight blue', 3)
blue_turtle.speed = 20

size = 200

for k in range(12):
    blue_turtle.draw_circle(size)
    blue_turtle.pen_up()
    blue_turtle.right(10)
    blue_turtle.forward(5)
    blue_turtle.left(10)
    blue_turtle.pen_down()
    size = size - 10


red_turtle = rg.SimpleTurtle('turtle')
red_turtle.pen = rg.Pen('red', 1)
red_turtle.speed = 15

size = 100



for r in range(10):
    red_turtle.draw_square(size)
    red_turtle.pen_up()
    red_turtle.left(10)
    red_turtle.forward(5)
    red_turtle.right(10)
    red_turtle.pen_down()
    size = size - 10



window.close_on_mouse_click()
