import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
screen = turtle.Screen()
screen.setup(700,650)
screen.bgcolor('lightcyan')

def move(x,y,angle = 0):
    t.penup()
    t.goto(x,y)
    t.setheading(angle)
    t.pendown()

def leaf(x,y,angle):
    move(x,y,angle)
    t.color('green','lightgreen')
    t.begin_fill()
    t.circle(65,65)
    t.left(115)
    t.circle(65,65)
    t.end_fill()



move(0,50,-90)

t.color('green')
t.pensize(8)
t.circle(380,38)
t.pensize(2)
leaf(24,-75,145)
leaf(62,-137,-30)

colors = ['pink','hotpink','lightpink']
for i in range(12):
    move(0,50,i*30)
    t.color('deeppink',colors[i%3])
    t.begin_fill()
    t.circle(90,60)
    t.left(120)
    t.circle(90,60)
    t.left(120)
    t.end_fill()

move(0,20)
t.color('orange','yellow')
t.begin_fill()
t.circle(30)
t.end_fill()
move(-10,55)
t.dot(7,'black')
move(10,55)
t.dot(7,"black")

move(-12,43,-60)
t.color('black')
t.circle(14,120)
t.hideturtle()

turtle.done()