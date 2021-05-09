# import colorgram
import turtle as t
import random

# rgb_colors = []
# colors = colorgram.extract("hirst_painting.jpg", 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# Generated from colorgram module and removed white color
color_list = [(225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85)]

# 10 x 10 dots
# dot radius 20 and space apart by 50
TURTLE_SIZE = 20
tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
t.speed(0)
t.penup()
t.hideturtle()

# Since default starting position is (0, 0), so we need to move to (-x, -y) to start
# With 50 steps each means we need to start with (-250, -250) because 50X5 = 250 (split 5 at -ve side and 5 at +ve side)
for y in range(-250, 250, 50):  # y coordinate
    for x in range(-250, 250, 50):  # x coordinate
        t.goto(x, y)
        t.dot(20, random.choice(color_list))

# Extra exercise:
# width = int(screen.window_width() / 2)
# height = int(screen.window_height() / 2)

# Note: Maximize the pop up windows to view
# Default starting point is (0, 0) at center of window,
#   so we need to move to turtle to left of the coordinate which needs to add a -ve
# for y in range(-height, height, 50):  # y coordinate
#     for x in range(-width, width, 50):  # x coordinate
#         t.penup()
#         t.goto(x, y)
#         t.pendown()
#         t.dot(20, random.choice(color_list))

screen.exitonclick()
