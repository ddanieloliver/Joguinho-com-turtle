# Daniel Vítor Oliveira Nascimento
# 535840 

import turtle
import random

janela = turtle.Screen()
janela.tracer(0) 
janela.bgpic("background.gif")

velocidade = 10

tartaruga = turtle.Turtle()
tartaruga.speed(0)
tartaruga.up()
janela.addshape("Tartaruga.gif")
tartaruga.shape("Tartaruga.gif")



vida1 = turtle.Turtle()
vida1.up()
vida1.setposition(-235, 265)
janela.addshape("Vida2.gif")
vida1.shape("Vida2.gif")

vida2 = turtle.Turtle()
vida2.up()
vida2.setposition(-205, 265)
janela.addshape("Vida2.gif")
vida2.shape("Vida2.gif")


vida3 = turtle.Turtle()
vida3.up()
vida3.setposition(-175, 265)
janela.addshape("Vida2.gif")
vida3.shape("Vida2.gif")


vidas = 3

placar = turtle.Turtle()
placar.up()
placar.setposition(238,255)
placar.shapesize(50)
placar.hideturtle()
placar.write("0", font=('Times New Roman', 20, 'bold'))

x = 250
y = 250

def desenharArena ():
    caneta = turtle.Turtle()
    caneta.color
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
    if tartaruga.xcor() < 210:
        tartaruga.forward(10)

andarDireita()

def andarCima():
    tartaruga.setheading(90)
    if tartaruga.ycor() < 218:
        tartaruga.forward(10)

andarCima()

def andarEsquerda():
    tartaruga.setheading(180)
    if tartaruga.xcor() > -210:
        tartaruga.forward(10)

andarEsquerda()

def andarBaixo():
    tartaruga.setheading(270)
    if tartaruga.ycor() > -220:
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
janela.addshape("VenenoVenenoso.gif")
veneno.shape("VenenoVenenoso.gif")

def venenoVenenoso():
    veneno.forward(10)
    if veneno.xcor() > 220:
        veneno.setx(220)
        veneno.setheading(random.randint(0, 360))
    if veneno.xcor() < -230:
        veneno.setx(-230)
        veneno.setheading(random.randint(0, 360))
    if veneno.ycor() > 220:
        veneno.sety(220)
        veneno.setheading(random.randint(0, 360))
    if veneno.ycor() < -220:
        veneno.sety(-220)
        veneno.setheading(random.randint(0, 360))
    
    turtle.ontimer(venenoVenenoso, 1000//36)

comida = turtle.Turtle()
comida.up()
comida.goto(100, 100)
comida.color("green")
janela.addshape("ComidaComidinha.gif")
comida.shape("ComidaComidinha.gif")

def comidinha():
    comida.forward(10)
    comida.up()
    if comida.xcor() > 220:
        comida.setx(220)
        comida.setheading(random.randint(0, 360))
    if comida.xcor() < -220:
        comida.setx(-220)
        comida.setheading(random.randint(0, 360))
    if comida.ycor() > 220:
        comida.sety(220)
        comida.setheading(random.randint(0, 360))
    if comida.ycor() < -215:
        comida.sety(-210)
        comida.setheading(random.randint(0, 360))
    turtle.ontimer(comidinha, 1000//36)

contarPlacar = 0

def colisao():
    def colisaoComida():
        global contarPlacar
        if comida.xcor() + 25 >= tartaruga.xcor() - 25 and comida.xcor() - 25 <= tartaruga.xcor() + 25 and comida.ycor() + 25 >= tartaruga.ycor() - 25 and comida.ycor() - 25 <= tartaruga.ycor() + 25:
            comida.goto(random.randint(0, 240), random.randint(0, 240))
            contarPlacar += 1
            placar.clear()
            placar.write(f"{contarPlacar}", font=('Times New Roman', 20, 'bold'))
    colisaoComida()

    def colisaoVeneno():
        global vidas
        global contarPlacar
        if veneno.xcor() + 20 >= tartaruga.xcor() - 20 and veneno.xcor() - 20 <= tartaruga.xcor() + 20 and veneno.ycor() + 20 >= tartaruga.ycor() - 20 and veneno.ycor() - 20 <= tartaruga.ycor() + 20:
            veneno.goto(random.randint(0, 240), random.randint(0, 240))
            vidas -= 1
            if vidas == 2:
                vida3.hideturtle()
            if vidas == 1:
                vida2.hideturtle()
            if vidas == 0:
                vida1.hideturtle()
                vidas = 3
                vida1.showturtle()
                vida2.showturtle()
                vida3.showturtle()
                contarPlacar = 0
                placar.clear()
                placar.write(f"{contarPlacar}", font=('Times New Roman', 20, 'bold'))
    colisaoVeneno()
    
    turtle.ontimer(colisao, 1000//36)


record = turtle.Turtle()
record.hideturtle()



desenharArena()
venenoVenenoso()
comidinha()
colisao()
while True:
    janela.update()
    