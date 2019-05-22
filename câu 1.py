import turtle
window = turtle.screen()
window.bgcolor("lighblack")
painter= turtle.turtle()
painter.fillcolor('yellow')
painter.pencolor('blue')
painter.pensize(3)
def drawsq(t,s):
    for i n range(4):
        t.forward(s)
        t.left(90)