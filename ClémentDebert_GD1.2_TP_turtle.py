import turtle 
import random
Turtle5=turtle.Turtle()
Turtle5.pencolor("red")
Turtle5.shape("circle")
Turtle6=turtle.Turtle()
Turtle6.pencolor("blue")
Turtle6.shape("circle")
Turtle7=turtle.Turtle()
Turtle7.pencolor("pink")
Turtle7.shape("circle")

turtle.delay(0.7)

#cercle 

'''''''''
Turtle5=turtle.Turtle()
for i in range(1,360,1):
    Turtle5.left(1)
    Turtle5.forward(1)
input()'''

#carré
''' 
Turtle5.forward(100)
Turtle5.left(90)
Turtle5.left(90)
Turtle5.forward(100)
Turtle5.left(90)
Turtle5.forward(100)

input()'''

#Escargot carré 
'''
for i in range(500):
    Turtle5.speed(100)
    Turtle5.left(90)
    Turtle5.forward(+i*5)
input()'''

#Escargot rond 

'''
r=10
for i in range(300):
    Turtle5.circle(r+i,10)
    #turtle.circle(radius, extent=None, steps=None)
input()'''

#Marche aléatoire avec turtle 
#ligne droite infinie 

'''
a = 5
while a < 200:
    Turtle5.forward(a)
input()'''

#fonction tourner aléatoire 

def positionRandom(tortue):
    X= random.randint(-300, 300)
    Y= random.randint(-300, 300)
    tortue.penup()
    tortue.goto(X, Y)
    tortue.pendown()

positionRandom(Turtle5)
positionRandom(Turtle6)
positionRandom(Turtle7)

def déplacement(tortue):
    a = random.randint(0,2)
    tortue.forward(10)
    if a == 0 :
        tortue.left(90)
    elif a==1 :
        tortue.forward(10)
    else :
        tortue.right(90)

def mangerTortue(tortue):
    if Turtle5.pos==Turtle6.pos :
        Turtle6.hideturtle

while 1: #fonction infinie
    déplacement(Turtle5)
    déplacement(Turtle6)
    déplacement(Turtle7)
    
input()















