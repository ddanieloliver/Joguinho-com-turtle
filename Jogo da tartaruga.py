# Daniel Vítor Oliveira Nascimento
# 535840 

import turtle
import random

janela = turtle.Screen()
janela.tracer(0) 
velocidade = 10

tartaruga = turtle.Turtle()
tartaruga.speed(0)
tartaruga.up()
tartaruga.shape('turtle')
tartaruga.color('green')

vida1 = turtle.Turtle()
vida1.up()
vida1.setposition(-250, 260)
vida2 = turtle.Turtle()
vida2.up()
vida2.setposition(-230, 260)
vida3 = turtle.Turtle()
vida3.up()
vida3.setposition(-210, 260)

vidas = 3

placar = turtle.Turtle()
placar.up()
placar.setposition(250,260)
placar.hideturtle()
placar.write("0", font=('Times New Roman', 15, 'bold'))


x = 250
y = 250

def desenharArena ():
    caneta = turtle.Turtle()
    caneta.up()
    caneta.goto(-x,-y)
    caneta.down()
    caneta.color()
    caneta.speed(0)
    for i in range(4):
        caneta.forward(2*x)
        caneta.left(90)
    caneta.hideturtle()


def andarDireita():
    tartaruga.setheading(0)
    if tartaruga.xcor() < 240:
        tartaruga.forward(10)
andarDireita()
def andarCima():
    tartaruga.setheading(90)
    if tartaruga.ycor() < 240:
        tartaruga.forward(10)
andarCima()
def andarEsquerda():
    tartaruga.setheading(180)
    if tartaruga.xcor() > -240:
        tartaruga.forward(10)
andarEsquerda()
def andarBaixo():
    tartaruga.setheading(270)
    if tartaruga.ycor() > -240:
        tartaruga.forward(10)
andarBaixo()


turtle.listen()
turtle.onkeypress(andarCima,'Up')
turtle.onkeypress(andarBaixo,'Down')
turtle.onkeypress(andarEsquerda,'Left')
turtle.onkeypress(andarDireita,'Right') 
     



veneno = turtle.Turtle()
veneno.speed(0)
veneno.up()
veneno.goto(50, 50)
veneno.color('red')
veneno.shape('circle')




def venenoVenenoso():
    veneno.forward(10)
    if veneno.xcor() > 240:
        veneno.setx(240)
        veneno.setheading(random.randint(0, 360))
    if veneno.xcor() < -240:
        veneno.setx(-240)
        veneno.setheading(random.randint(0, 360))
    if veneno.ycor() > 240:
        veneno.sety(240)
        veneno.setheading(random.randint(0, 360))
    if veneno.ycor() < -240:
        veneno.sety(-240)
        veneno.setheading(random.randint(0, 360))
    
    turtle.ontimer(venenoVenenoso, 1000//36)

comida = turtle.Turtle()
comida.shape("circle")
comida.color("green")
comida.up()

def comidinha():
    comida.forward(10)
    comida.up()
    if comida.xcor() > 240:
        comida.setx(240)
        comida.setheading(random.randint(0, 360))
    if comida.xcor() < -240:
        comida.setx(-240)
        comida.setheading(random.randint(0, 360))
    if comida.ycor() > 240:
        comida.sety(240)
        comida.setheading(random.randint(0, 360))
    if comida.ycor() < -240:
        comida.sety(-240)
        comida.setheading(random.randint(0, 360))
    
    turtle.ontimer(comidinha, 1000//36)
contarPlacar = 0
def colisao():
    def colisaoComida():
        global contarPlacar
        if comida.xcor() + 10 >= tartaruga.xcor() - 10 and comida.xcor() - 10 <= tartaruga.xcor() + 10 and comida.ycor() + 10 >= tartaruga.ycor() - 10 and comida.ycor() - 10 <= tartaruga.ycor() + 10:
            comida.goto(random.randint(0, 360), random.randint(0, 360))
            contarPlacar += 1
            placar.clear()
            placar.write('{}'.format(contarPlacar), font=('Verdana', 15, 'bold'))
    colisaoComida()

    def colisaoVeneno():
        global vidas
        if veneno.xcor() + 10 >= tartaruga.xcor() - 10 and veneno.xcor() - 10 <= tartaruga.xcor() + 10 and veneno.ycor() + 10 >= tartaruga.ycor() - 10 and veneno.ycor() - 10 <= tartaruga.ycor() + 10:
            veneno.goto(random.randint(0, 360), random.randint(0, 360))
            vidas -= 1
            if vidas == 2:
                vida3.hideturtle()
            elif vidas == 1:
                vida2.hideturtle()
            else:
                vida1.hideturtle()
                vidas = 3
                vida1.showturtle()
                vida2.showturtle()
                vida3.showturtle()

    colisaoVeneno()
    
    turtle.ontimer(colisao, 1000//36)

    '''
    distX = tartaruga.xcor() - comida.xcor()
    distY = tartaruga.ycor() - comida.ycor()
    if distX > -20 and distX < 20 and distY > -20 and distY < 20:
        comida.hideturtle
    '''
desenharArena()
venenoVenenoso()
comidinha()
colisao()
while True:
    janela.update()
















    