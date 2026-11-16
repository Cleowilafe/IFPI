from turtle import *
from random import randint, choice


def move_to_random_location():
    penup()
    setpos(randint(-380, 380), randint(-320, 320))
    pendown()


def draw_starburst(points, size, colour):
    color(colour)
    angle = 180 - (180 / points)
    pendown()
    begin_fill()
    for _ in range(points):
        forward(size)
        left(angle)
    end_fill()
    penup()


def main():
    speed(11)
    bgcolor("DarkGreen")

    colours = [
        "#20E0D0",  # Turquesa
        "#B565E8",  # Lilás
        "#D6E5E3",  # Cinza-claro
        "#E05A8D",  # Rosa
        "#FFD147",  # Amarelo
        "#A30041",  # Vinho
        "#8A3FFC",  # Roxo
    ]

    # Desenha 55 formas estreladas de tamanhos, pontas e cores variadas
    for _ in range(55):
        move_to_random_location()
        points = choice([9, 11, 13, 15])
        size = randint(15, 65)
        draw_starburst(points, size, choice(colours))

    hideturtle()
    done()


if __name__ == '__main__':
    main()
