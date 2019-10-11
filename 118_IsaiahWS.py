import turtle as trtl
import random as rdn

color_list = ["Red","Orange","Yellow","Green","Blue","Purple","Violet"]

loader = trtl.Turtle()
#config for turtle
loader.speed(8)
loader.pensize(5)
loader.pencolor("Blue")
loader.fillcolor("Aqua")
loader.penup()
loader.hideturtle()
#Make the box for the loading box
loader.goto(-400,100)
loader.begin_fill()
loader.pendown()
loader.goto(400,100)
loader.goto(400,50)
loader.goto(-400,50)
loader.goto(-400,100)
loader.end_fill()
#Start making the loading bar
loader.penup()
loader.goto(-380,75)
loader.pendown()
loader.pensize(35)
loader.pencolor(rdn.choice(color_list))
repeat = 0
load_bar = 0
while True:
    if load_bar < 1:
        loader.penup()
        loader.goto(-380,75)
        loader.pencolor(rdn.choice(color_list))
        loader.pendown()
        loader.forward(750)
        load_bar += 1
    if load_bar > 0:
        loader.penup()
        loader.goto(-380,75)
        loader.pencolor("White")
        loader.pendown()
        loader.forward(750)
        load_bar -=1
        





wn = trtl.Screen()
wn.mainloop()