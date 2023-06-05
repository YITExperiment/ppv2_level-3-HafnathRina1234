import turtle


from itertools import cycle
colors = cycle(['blue','lawngreen','goldenrod','lightblue','hotpink',
                'thistle'])


def draw_circle(size,angle,shift):
    turtle.bgcolor(next(colors))
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+5, angle+1,shift+1)

turtle.bgcolor('navy')
turtle.speed('fast')
turtle.pensize(50)
draw_circle(35,0,2)
