import turtle
import random
import math



"""
for i in range(4):
    turtle.forward(50)
    turtle.left(90)

input()
"""
"""
turtle.circle(50)

input()
"""
"""
var = 10
while True: 
    turtle.forward(var)
    turtle.left(90)
    var += 1
"""
"""
var = 1
tortue.speed(0)
while True:
    tortue.forward(var/10000)
    tortue.left(1)
    var+=1
"""
"""
tortue.speed(1)
while True:
    tortue.forward(20)
    a = random.randint(-180, 180)
    tortue.left(a)
    tortue1.forward(20)
    b = random.randint(-180, 180)
    tortue1.left(b)
    tortue2.forward(20)
    c = random.randint(-180,180)
    tortue2.left(c)
"""

n=10
tortues=[]

maTortue = turtle.Turtle()


def f():
    maTortue.forward(20)

def b():
    maTortue.backward(20)

def l():
    maTortue.left(20)

def r():
    maTortue.right(20)

turtle.onkey(f, "Up")
turtle.onkey(b, "Down")
turtle.onkey(r, "Right")
turtle.onkey(l, "Left")

turtle.listen()


for i in range(n):
    shape = random.randint(1,4)
    x = random.randint(-500,500)
    y = random.randint(-500,500)
    var = turtle.Turtle()
    var.penup()
    tortues.append(var)
    var.speed(0)
    var.color(random.random(),random.random(),random.random())
    var.shape('circle')
    var.shapesize(shape,shape)
    var.setposition(x,y)
    
"""
while True:
    for i in tortues:
        i.forward(20)
        angle = random.randint(-180, 180)
        i.left(angle)
"""
def distance(t1,t2):
    math.sqrt((t1.pos()[0]-t2.pos()[0])**2 + (t1.pos()[1]-t2.pos()[1])**2)

def manger(i,j):
    i.shapesize(tortues[j].shapesize()[0]+i.shapesize()[0],tortues[j].shapesize()[0]+i.shapesize()[0])
    tortues[j].ht()
    tortues.remove(tortues[j])

while True:
    for i in tortues:
        i.forward(10)
        """
        if i.pos()[0] > 500:
            #bouge vers la gauche
        elif i.pos()[1] > 500:
            #bouge vers la bas
        elif i.pos()[0] <- 500:
            #bouge vers la droite
        elif i.pos()[1] < - 500:
            #bouge vers la haut
        else :
"""
        i.left(random.randint(-180,180))
        j=-1
        while j < n-1:
            j+=1
            if i != tortues[j] :
    
                if i.distance(tortues[j]) < (i.shapesize()[0]+tortues[j].shapesize()[0])*5:
                    if (i.shapesize()[0] > tortues[j].shapesize()[0]):
                        manger(i,j)
                            
                        n-=1
