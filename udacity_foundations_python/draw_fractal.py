import turtle
import math

def draw_triangle(a_turtle, length, start_x, start_y):
    a_turtle.penup()
    a_turtle.setx(start_x)
    a_turtle.sety(start_y)
    a_turtle.pendown()
    a_turtle.setheading(0)

    a_turtle.begin_fill()
    a_turtle.right(60)
    a_turtle.forward(length)
    a_turtle.right(120)
    a_turtle.forward(length)
    a_turtle.right(120)
    a_turtle.end_fill()

def draw_triangle_level(level, a_turtle, length, start_x, start_y):
    x_mult = 1/4 * math.pow(2, level-1) 
    y_mult = math.pow(2, level - 2) 

    if level == 1 :
        return draw_triangle(a_turtle, length, start_x, start_y)

    draw_triangle_level(level - 1, a_turtle, length, start_x, start_y)
    draw_triangle_level(level - 1, a_turtle, length, start_x + x_mult * length, start_y + y_mult * length * 0.866)
    draw_triangle_level(level - 1, a_turtle, length, start_x + 2 * x_mult * length, start_y)
    

def draw_fractal_level(level, shape, color, fillcolor, length, speed):
    window = turtle.Screen()
    window.bgcolor("white")

    myturtle = turtle.Turtle()
    myturtle.shape(shape)
    myturtle.color(color)
    myturtle.fillcolor(fillcolor)
    myturtle.speed(speed)

    # place the fractal's centre of mass at the middle of the screen
    x_centre = -math.pow(2, level - 1) * 0.5 * length
    y_centre = -math.pow(2, level - 1) * 0.866 * 1/3 * length

    draw_triangle_level(level, myturtle, length, x_centre, y_centre)

    window.exitonclick()

# main starts here
draw_fractal_level(5, "turtle", "blue", "green", 30, 5)
