#!/usr/bin/env python3
# coding: utf-8

import turtle
import math

def triangle(g,l,debug=False):
    turtle.penup()
    turtle.goto(g)
    turtle.pendown()

    if debug: turtle.pencolor("red")
    turtle.setheading(90)
    turtle.forward(l*(math.sqrt(3)/2)*2/3)

    if debug: turtle.pencolor("black")
    turtle.pendown()
    turtle.setheading(-120)
    turtle.forward(l)
    turtle.setheading(0)
    turtle.forward(l)
    turtle.setheading(120)
    turtle.forward(l)

def carre(g,l,debug=False):
    turtle.penup()
    turtle.goto(g)
    turtle.pendown()

    if debug: turtle.pencolor("red")
    turtle.pensize(1)
    turtle.setheading(-135)
    turtle.forward(l*(math.sqrt(2)/2))

    if debug: turtle.pencolor("black")
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(l)
    turtle.setheading(90)
    turtle.forward(l)
    turtle.setheading(180)
    turtle.forward(l)
    turtle.setheading(270)
    turtle.forward(l)

def cercle(g,l,debug=False):
    turtle.penup()
    turtle.goto(g)
    turtle.pendown()

    if debug: turtle.pencolor("red")
    turtle.pensize(1)
    turtle.setheading(-90)
    turtle.forward(l/2)

    if debug: turtle.pencolor("black")
    turtle.pendown()
    turtle.setheading(0)
    turtle.circle(l/2)

def main():
    turtle.Screen()
    turtle.Screen().setup(640, 480, 100, 100)

    try:
        # turtle.reset()
        triangle(g=(50,50),l=100,debug=True)
        cercle(g=(-50,-50),l=100,debug=True)
        carre(g=(-50,-50),l=100,debug=True)
        triangle(g=(-50,-50),l=100,debug=True)
    finally:
        # turtle.exitonclick()
        pass

if __name__ == "__main__":
    main()
