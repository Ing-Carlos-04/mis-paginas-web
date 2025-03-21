import turtle

t = turtle.Turtle()
t.pensize(4)

turtle.bgcolor("black")

def go(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
t.pencolor("#006400")
t.fillcolor("#9ACD32")

go(94.85, -121.007) 
t.begin_fill()
t.seth(126.77)
t.circle(66.84, 109.32)
t.seth(307.27)
t.circle(67.25, 108.33)
t.end_fill()

go(-14.16, -123.79)
t.seth(16.41)
t.circle(-163.40, 29.01)

go(-6.78, -130.23)
t.begin_fill()
t.seth(81.81)
t.circle(62.22, 123.09)
t.seth(257.18)
t.circle(59.80, 132.25)
t.end_fill()

t.seth(124.58)
t.circle(106.79, 32.98)

go(-14.16, -16.05) 
t.begin_fill()
t.seth(263.79)
t.circle(652.34,21.75)
t.seth(45)
t.forward(20.19)
t.seth(101.81)
t.circle(-973.65,13.61)
t.end_fill()

t.pencolor("#A0522D")
t.fillcolor("#A0522D")

go(107.5,82) 
t.begin_fill()
t.seth(90)
t.circle(101)
t.end_fill()

t.pencolor("white")
t.fillcolor("white")

go(73, 77)
t.begin_fill()
t.seth(12.26)
t.forward(13.34)
t.seth(81.54)
t.circle(71.42, 98.46)
t.seth(344.59)
t.circle(-79.07,80.79)
t.end_fill()

t.pencolor("#641E16")
t.fillcolor("#641E16")

go(46.60, 93.85)
t.seth(217.77)
t.forward(22.62)
t.seth(330.02)
t.forward(24.44)

go(10.53, 70.67)
t.seth(270)
t.circle(-7.89, 180)

go(-33.95, 85.70)
t.begin_fill()
t.seth(90)
t.circle(8)
t.end_fill()

t.pencolor("gold")
t.fillcolor("yellow")

def petalo(angulo):
    t.begin_fill()
    t.seth(angulo)
    t.circle(62.19, 119.89)
    t.seth(angulo-209.77)
    t.circle(66.45, 102.89)
    t.seth(angulo-31.91)
    t.circle(-100.68, 40.36)
    t.end_fill()
    
go(0, -18.04)
petalo(248.33)
go(100.30, 44.78)
petalo(320.33)
go(71.55, 159.59)
petalo(32.33)
go(-46.52, 167.72)
petalo(104.33)
go(-90.74, 57.94)
petalo(176.33)
go(-57.71, 5.21)
petalo(212.33)
go(60.36, -2.93)
petalo(284.33)
go(104.58, 106.85)
petalo(356.33)
go(13.83, 182.83)
petalo(68.33)
go(-86.47, 120.01)
petalo(140.33)

t.color("yellow")
t.penup()
t.goto(310,-300)
t.pendown()
t.write("TE QUIERO MUCHO MEJA", False,
        "right", ("Arial ", 50, "bold"))

t.hideturtle()
turtle.done()