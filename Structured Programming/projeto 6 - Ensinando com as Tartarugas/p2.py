from turtle import *


def draw_star(star_size, star_colour):
    color(star_colour)
    pendown()
    begin_fill()
    for _ in range(5):
        left(144)
        forward(star_size)
    end_fill()
    penup()


def draw_planet(planet_size, planet_colour):
    color(planet_colour)
    pendown()
    begin_fill()
    circle(planet_size)
    end_fill()
    penup()


def main():
    bgcolor("MidnightBlue")

    draw_planet(40, "OrangeRed")
    forward(120)

    draw_planet(25, "DeepSkyBlue")
    left(120)
    forward(150)

    draw_star(35, "White")

    hideturtle()
    done()


if __name__ == '__main__':
    main()
