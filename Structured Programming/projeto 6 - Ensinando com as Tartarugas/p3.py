from turtle import *
from random import randint, choice


def move_to(x, y):
    penup()
    setpos(x, y)
    pendown()


def draw_square(size, colour):
    color(colour)
    pendown()
    begin_fill()
    for _ in range(4):
        forward(size)
        left(90)
    end_fill()
    penup()


def draw_triangle(size, colour):
    color(colour)
    pendown()
    begin_fill()
    for _ in range(3):
        forward(size)
        left(120)
    end_fill()
    penup()


def draw_house(x, y, size, wall_colour, roof_colour):
    move_to(x, y)
    draw_square(size, wall_colour)
    move_to(x, y + size)
    draw_triangle(size, roof_colour)


def draw_cloud(x, y, radius):
    color("White")
    offsets = [(0, 0), (radius, 0), (radius * 2, 0), (radius * 0.5, radius * 0.7), (radius * 1.5, radius * 0.7)]
    for dx, dy in offsets:
        move_to(x + dx, y + dy)
        pendown()
        begin_fill()
        circle(radius)
        end_fill()
        penup()


def draw_bird(x, y, size):
    color("DimGray")
    move_to(x, y)
    setheading(315)
    forward(size)
    setheading(45)
    forward(size)
    setheading(0)
    penup()


def main():
    speed(11)
    bgcolor("SkyBlue")

    # Desenha nuvens no céu
    for _ in range(5):
        draw_cloud(randint(-350, 300), randint(80, 250), randint(15, 25))

    # Desenha pássaros aleatórios
    for _ in range(12):
        draw_bird(randint(-350, 350), randint(50, 300), randint(6, 12))

    # Desenha uma fileira de casas de tamanhos e cores diferentes
    wall_colours = ["LightYellow", "PeachPuff", "Lavender", "MistyRose"]
    roof_colours = ["Firebrick", "SaddleBrown", "DarkSlateGray", "Maroon"]

    for i in range(4):
        pos_x = -300 + i * 170
        size = randint(70, 110)
        draw_house(pos_x, -200, size, choice(wall_colours), choice(roof_colours))

    hideturtle()
    done()


if __name__ == '__main__':
    main()
