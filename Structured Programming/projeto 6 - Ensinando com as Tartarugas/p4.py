from turtle import *
from random import randint, choice


def move_to_random_location():
    penup()
    setpos(randint(-400, 400), randint(-400, 400))
    pendown()


def draw_star(star_size, star_colour):
    color(star_colour)
    pendown()
    begin_fill()
    for _ in range(5):
        left(144)
        forward(star_size)
    end_fill()
    penup()


def draw_galaxy(number_of_stars):
    star_colours = ["#058396", "#0275A6", "#827E01"]
    move_to_random_location()

    for _ in range(number_of_stars):
        penup()
        left(randint(-180, 180))
        forward(randint(5, 20))
        pendown()
        draw_star(2, choice(star_colours))


def draw_constellation(number_of_stars):
    move_to_random_location()

    for _ in range(number_of_stars - 1):
        draw_star(randint(7, 15), "White")
        pendown()
        left(randint(-90, 90))
        forward(randint(30, 70))

    draw_star(randint(7, 15), "White")


def main():
    speed(11)
    bgcolor("MidnightBlue")

    # Desenha 30 estrelas brancas de tamanhos e posições aleatórias
    for _ in range(30):
        move_to_random_location()
        draw_star(randint(5, 25), "White")

    # Desenha 3 pequenas galáxias com 40 estrelas cada
    for _ in range(3):
        draw_galaxy(40)

    # Desenha 2 constelações com quantidade aleatória de estrelas
    for _ in range(2):
        draw_constellation(randint(4, 7))

    hideturtle()
    done()


if __name__ == '__main__':
    main()
