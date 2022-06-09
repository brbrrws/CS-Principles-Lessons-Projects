
"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

 Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

# move turtle over on the left side of the screen
turtle.penup()
turtle.setx(-166)
turtle.sety(0)
turtle.pendown()

# ---  draw a square below ---
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)

# move turtle over a bit to the right
turtle.penup()
turtle.setx(-140)
turtle.sety(15)
turtle.pendown()

# ---  draw a triangle below ---
turtle.right(120)
turtle.forward(30)
turtle.left(120)
turtle.forward(30)
turtle.left(120)
turtle.forward(30)
turtle.right(30)

# move turtle over to the right a bit more
turtle.penup()
turtle.setx(-160)
turtle.sety(60)
turtle.pendown()

# ---  draw an octogon below ---
turtle.forward(30)
turtle.right(45)
turtle.forward(30)
turtle.right(45)
turtle.forward(30)
turtle.right(45)
turtle.forward(30)
turtle.right(45)
turtle.forward(30)
turtle.right(45)
turtle.forward(30)
turtle.right(45)
turtle.forward(30)
turtle.right(45)
turtle.forward(30)
turtle.right(45)

# move turtle over to the right a bit more
turtle.penup()
turtle.setx(-190)
turtle.sety(72)
turtle.pendown()


# ---  draw a hexagon below ---
turtle.forward(60)
turtle.right(45)
turtle.forward(65)
turtle.right(90)
turtle.forward(65)
turtle.right(45)
turtle.forward(60)
turtle.right(45)
turtle.forward(65)
turtle.right(90)
turtle.forward(65)

"""
If you are all finished, try using different colors for different shapes!  

Or, explore the different options you have at:
https://docs.python.org/3/library/turtle.html

"""
