from turtle import *


def draw_star():
    pendown()
    begin_fill()
    for _ in range(5):
        left(144)
        forward(50)
    end_fill()
    penup()


def draw_square():
    pendown()
    begin_fill()
    for _ in range(4):
        forward(50)
        left(90)
    end_fill()
    penup()


def draw_triangle():
    pendown()
    begin_fill()
    for _ in range(3):
        forward(60)
        left(120)
    end_fill()
    penup()


def main():
    bgcolor("MidnightBlue")
    color("WhiteSmoke")

    draw_star()
    forward(100)

    color("Gold")
    draw_square()
    left(120)
    forward(150)

    color("Cyan")
    draw_triangle()

    hideturtle()
    done()


if __name__ == '__main__':
    main()
