import turtle
import time
import random
from pygame import mixer


#Python Turtle Graphics es un modulo de programacion grafica para Python
#utilizado como metodo para ensenar programacion a traves de coordenadas
#relativas. El objeto a programar recibe el nombre de tortuga


posponer = 0.1

#Estaclecemos la funcion para que me empiece con un sonido cuando tire la funcion
def comienzo_sound():
    mixer.init()
    mixer.music.load("intro.mp3")
    mixer.music.play()


#Marcador en 0
puntaje = 0
max_puntaje = 0
#nivel
nivel = 1
#lista de obstaculos
todos_obstaculos = []


#Generamos la ventana con los parametros necesarios como tamano en pixeles
#color de fondo e imagen de fondo
#Configuracion de la ventana
ventana = turtle.Screen()
ventana.title("Juego Snake Proyecto UdeA")
ventana.bgcolor("black")
ventana.bgpic("fondo.png")
ventana.setup(width = 1300, height = 1100)
ventana.tracer(0)

#Apenas se cree la pantalla le tiramos la funcion
comienzo_sound()

#Creamos letrero con su color, tipo de fuente y tamano con un tiempo de espera
#de un segundo
presentacion = turtle.Turtle()
presentacion.speed(0)
presentacion.color("yellow")
presentacion.penup()
presentacion.hideturtle()
presentacion.goto(-600,0)
presentacion.write("Juego Snake por Jhon Rodriguez", font =("Courier", 50, "normal"))
presentacion.clear()
time.sleep(1)

presentacion2 = turtle.Turtle()
presentacion2.speed(0)
presentacion2.color("yellow")
presentacion2.penup()
presentacion2.hideturtle()
presentacion2.goto(-480,0)
presentacion2.write("Universidad de Antioquia", font =("Courier", 50, "normal"))
presentacion2.clear()
time.sleep(1)

presentacion3 = turtle.Turtle()
presentacion3.speed(0)
presentacion3.color("yellow")
presentacion3.penup()
presentacion3.hideturtle()
presentacion3.goto(-20,-30)
presentacion3.write("3", font =("Courier", 50, "normal"))
presentacion3.clear()
time.sleep(1)

presentacion4 = turtle.Turtle()
presentacion4.speed(0)
presentacion4.color("yellow")
presentacion4.penup()
presentacion4.hideturtle()
presentacion4.goto(-20,-30)
presentacion4.write("2", font =("Courier", 50, "normal"))
presentacion4.clear()
time.sleep(1)

presentacion5 = turtle.Turtle()
presentacion5.speed(0)
presentacion5.color("yellow")
presentacion5.penup()
presentacion5.hideturtle()
presentacion5.goto(-20,-30)
presentacion5.write("1", font =("Courier", 50, "normal"))
presentacion5.clear()
time.sleep(1)


#definimos para que nos empiece tirando hacia abajo y le definimos su forma
#color, la corrdenada en la cual queremos que aparezca y la velicidad de aparicion
#Cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "down"

#Seguimos definiendo objetos con sus caracteristicas...
#con el random generamos cordenadas aleatorias para la aparicion de la comida
#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("yellow")
comida.penup()
x = random.randint(-630,630)
y = random.randint(-330,280)
comida.goto(x,y)

#Segmentos o cuerpo de la serpiente, aqui cuardaremos los segmentos que de generen
#cuando coma la serpiente
segmentos = []

#Texto superior
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,310)
texto.write("Puntaje: 0     Maximo Puntaje: 0   Nivel: 1", align = "center",
font =("Courier", 18, "normal"))

#Linea
linea = turtle.Turtle()
linea.speed(0)
linea.color("white")
linea.penup()
linea.hideturtle()
linea.goto(0,300)
linea.write("_________________________________________________________________________________________",
align = "center", font =("Courier", 18, "normal"))

#Funciones
def morder_sound():
    mixer.init()
    mixer.music.load("morder1.mp3")
    mixer.music.play()

def perder_sound():
    mixer.init()
    mixer.music.load("game_overs.mp3")
    mixer.music.play()

def ganar_sound():
    mixer.init()
    mixer.music.load("ganar.mp3")
    mixer.music.play()

def limpiar_obstaculos():
    #Esconder los obstaculos
    for j in todos_obstaculos:
        j.goto(1000,1000)
    #Limpiar lista de obstaculos
    todos_obstaculos.clear()

def ganaste():
    GA = turtle.Turtle()
    GA.speed(0)
    GA.color("yellow")
    GA.penup()
    GA.hideturtle()
    GA.goto(-250,230)
    GA.write("¡GANASTE!", font =("Courier", 50, "normal"))
    GA.clear()
    time.sleep(1)

    GA = turtle.Turtle()
    GA.speed(0)
    GA.color("yellow")
    GA.penup()
    GA.hideturtle()
    GA.goto(-250,230)
    GA.write("FIN DEL JUEGO", font =("Courier", 50, "normal"))
    GA.clear()
    time.sleep(1)

def game_over():
    perder_sound()
    #Esconder los obstaculos
    for i in todos_obstaculos:
        i.goto(1000,1000)
    #Limpiar lista de obstaculos
    todos_obstaculos.clear()
    #Esconder los Segmentos
    for segmento in segmentos:
        segmento.goto(1000,1000)
    #Limpiar lista de Segmentos
    segmentos.clear()
    ventana.bgpic("game_overi.png")
    GO = turtle.Turtle()
    GO.speed(0)
    GO.color("white")
    GO.penup()
    GO.hideturtle()
    GO.goto(-180,0)
    GO.write("", font =("Courier", 50, "normal"))
    GO.clear()
    time.sleep(2)
    ventana.bgpic("fondo.png")
    cabeza.goto(0,0)
    cabeza.direction = "stop"
    global puntaje
    global nivel
    #Resetear Marcador
    puntaje = 0
    nivel = 1
    texto.clear()
    texto.write("Puntaje: {}     Maximo Puntaje: {}   Nivel: {}".format(puntaje,
     max_puntaje, nivel), align = "center", font =("Courier", 18, "normal"))

def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"


#Esta nos define las direcciones de x,y de la cabeza y cuanta distancia vamos a
#recorrer, en este caso el numero 20 equivale a 20 pixeles
#Los numeros negativos son porque en turtle, la pantalla esta basada o coincide
#con el plano cartesiano
def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#Esta funcion nos ahorra muchas lineas y mucho tiempo
#al tener como parametro la posicion de cada obstaculo creado el cual lo retornara
def crear_obstaculo(posicion):
    obstaculo = turtle.Turtle()
    obstaculo.speed(0)
    obstaculo.shape("square")
    obstaculo.shapesize(1,1)
    obstaculo.color("blue")
    obstaculo.penup()
    obstaculo.goto(posicion['x'], posicion['y'])
    return obstaculo

#Teclado
#Estara pendiente a las teclas que apretemos para empezar a correr
ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(derecha, "Right")
ventana.onkeypress(izquierda, "Left")

#establecemos una bandera verdadera antes del ciclo para poder romperlo cuando
#la bandera sea falsa
jugando = True

while(jugando):
    #ventana.update va a refrescarse cada ciclo
    ventana.update()

    #Colisiones paredes
    if cabeza.xcor() > 650 or cabeza.xcor() < -650 or cabeza.ycor() > 300 or cabeza.ycor() < -350:
        #Game over
        game_over()

    #Colisiones de comida
    #Cuando la distancia de la cabeza con respecto a la comida sea menor a 20
    #la funcion del morder sonido sonara y nos tirara un numero random que
    #luego se lo asignaremos a la comida
    if cabeza.distance(comida) < 20:
        morder_sound()
        is_good = True
        ultimo_obstaculo_revisado = 0

        x = random.randint(-630,630)
        y = random.randint(-330,280)
        #Con este while nos aseguraremos que la comida no se genere en la
        #misma corrdenada que el obstaculo y le pasamos una ditancia donde si es
        #menor a 40, lo genere en otro lado.
        #Empieza siendo verdadero
        while(is_good):
            for i,obstaculo in enumerate(todos_obstaculos):
                if (obstaculo.distance((x, y)) < 40):
                    x = random.randint(-630,630)
                    y = random.randint(-330,280)
                    break
                ultimo_obstaculo_revisado = i+1
            #si el ultimo ultimo_obstaculo_revisado es igual a la longitud de
            #todos los obstaculos, la bandera is_good se pone falsa y rompe
            #el ciclo
            if(ultimo_obstaculo_revisado == len(todos_obstaculos)):
                is_good = False
        #aca finalmente es cuando se genera la comida en la posicion x,
        comida.goto(x,y)

        #Estos son los pedazos cuerpo que se agregan cuando la serpiente come
        #la manzana y se agrega a la lista de segmentos
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("white")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        #Aumenta Marcador en 10
        puntaje += 10

        #con este if nos asesuramos que el marcador global sea superado solo si
        #el marcador actual supera al global que se establecio previamente
        if puntaje > max_puntaje:
            max_puntaje = puntaje
        #Se actualiza el tablero
        texto.clear()
        texto.write("Puntaje: {}     Maximo Puntaje: {}   Nivel: {}".format(puntaje, max_puntaje, nivel),
                    align = "center", font =("Courier", 18, "normal"))

    #Mover el cuerpo de la serpiente
    #Aca voy a saber cuantos segmentos tengo en la lista y ese dato lo
    #guardaremos en total_seg
    total_seg = len(segmentos)

    #aca lo qque hago es iterar sobre total_seg para que el ultimo segmento
    #siga al penultimo, el penultimo al antepenultimo etc.
    #por eso lo comienzo para que me itere al reves con -1. Para que no me
    #coja el indice el ultimo digito el otro -1, y el 0 para que tampoco me
    #coja el 0
    for index in range(total_seg -1, 0, -1):
        #le damos xcor y ycor posicion basados en la lista segmentos y por cada
        #ciclo index tendra un valor menor y finalmente, le daremos posicion
        #a cada segmento para que siga al anterior
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)

    #si total_seg tiene al menos 1 segmento, le damos las coordenadas de la
    #cabeza.
    if total_seg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        #Luego a segmentos al primer elemento [o] lo movemos a la coordenada
        #donde esta la cabeza
        segmentos[0].goto(x,y)

    mov()

    #Colisiones con el cuerpo
    #si algun segmento con respecto a la distancia de la cabeza es menor a 20
    #se pierde el juego.
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            #Game over
            game_over()

################## Nivel 2 #####################################################
    #Con es if defino el puntaje para el cual se pasa al seiguien nivel y si
    #no es el mismo nivel para que no haya errores
    if puntaje == 40 and not nivel == 2:
        #nivel sube 1
        nivel += 1
        texto.clear()
        texto.write("Puntaje: {}     Maximo Puntaje: {}   Nivel: {}".format(puntaje, max_puntaje, nivel),
                align = "center", font =("Courier", 18, "normal"))
        nivel = 2
        letrero_n2 = turtle.Turtle()
        letrero_n2.speed(0)
        letrero_n2.color("white")
        letrero_n2.penup()
        letrero_n2.hideturtle()
        letrero_n2.goto(-180,0)
        letrero_n2.write("NIVEL 2", font =("Courier", 50, "normal"))
        letrero_n2.clear()
        #cabeza al centro
        cabeza.goto(0,0)
        #cabeza quieta
        cabeza.direction = "stop"
        time.sleep(2)


        #Esconder los Segmentos
        #los mando a pa posicion 1000,1000 para que no se vean (fuera de la ventana)
        for segmento in segmentos:
            segmento.goto(1000,1000)


        #Limpiar lista de Segmentos
        #para que comience pequena la serpiente
        segmentos.clear()


        #La funcion crear_obstaculo me permite no tener que crear un objeto con
        #todas sus caracteristicas cada que vaya a crear uno.

        #Obstaculos
        #Pared arriba
        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-450, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-430, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-410, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-390, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-370, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-350, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-330, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-290, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-270, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-250, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-230, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-210, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-190, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-170, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-150, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-130, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-110, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-90, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-70, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-50, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-30, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-10, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':10, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':30, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':50, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':70, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':90, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':110, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':130, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':150, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':170, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':190, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':210, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':230, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':250, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':270, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':290, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':330, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':350, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':370, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':390, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':410, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':430, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':450, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':150}))

        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-450, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-410, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-390, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-370, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-430, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-350, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-330, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-290, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-270, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-250, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-230, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-210, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-190, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-170, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-150, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-130, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-110, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-90, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-70, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-50, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-30, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':-10, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':10, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':30, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':50, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':70, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':90, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':110, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':130, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':150, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':170, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':190, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':210, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':230, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':250, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':270, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':290, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':330, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':350, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':370, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':390, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':410, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':430, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':450, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':170}))

        #Pared abajo
        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-450, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-430, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-410, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-390, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-370, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-350, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-330, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-290, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-270, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-250, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-230, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-210, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-190, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-170, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-150, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-130, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-110, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-90, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-70, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-50, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-30, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-10, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':10, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':30, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':50, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':70, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':90, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':110, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':130, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':150, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':170, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':190, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':210, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':230, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':250, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':270, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':290, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':330, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':350, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':370, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':390, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':410, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':430, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':450, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':-150}))

        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-450, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-430, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-410, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-390, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-370, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-350, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-330, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-290, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-270, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-250, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-230, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-210, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-190, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-170, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-150, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-130, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-110, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-90, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-70, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-50, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-30, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-10, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':10, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':30, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':50, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':70, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':90, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':110, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':130, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':150, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':170, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':190, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':210, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':230, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':250, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':270, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':290, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':330, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':350, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':370, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':390, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':410, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':430, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':450, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':-170}))

    #Este for nos recorre toda la lista todos_obstaculos y revisa que si
    #la distancia de la cabeza es menor a 20pix y ademas es nivel 2, pierdo el juego
    for cada_obstaculo in todos_obstaculos:
        if (cabeza.distance(cada_obstaculo)) < 20 and nivel == 2:
            #Game over
            game_over()


#### Los mismos procedimientos se repiten en cada nivel, asi que la funcion
#    es la misma y los comentarios serian los mismos.



##################       Nivel 3      ##########################################

    if puntaje == 60 and not nivel == 3:
        nivel = 3
        texto.clear()
        texto.write("Puntaje: {}     Maximo Puntaje: {}   Nivel: {}".format(puntaje, max_puntaje, nivel),
                align = "center", font =("Courier", 18, "normal"))

        letrero_n3 = turtle.Turtle()
        letrero_n3.speed(0)
        letrero_n3.color("white")
        letrero_n3.penup()
        letrero_n3.hideturtle()
        letrero_n3.goto(-180,0)
        letrero_n3.write("NIVEL 3", font =("Courier", 50, "normal"))
        letrero_n3.clear()
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        time.sleep(2)


        #Esconder los Segmentos
        for segmento in segmentos:
            segmento.goto(1000,1000)

        #Limpiar lista de Segmentos
        segmentos.clear()

        #Limpiar obstaculos
        limpiar_obstaculos()

        #Obstaculos
        #Pared arriba izquierda
        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-450, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-430, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-410, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-390, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-370, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-350, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-330, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':130}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':130}))
        todos_obstaculos.append(crear_obstaculo({'x':-450, 'y':130}))
        todos_obstaculos.append(crear_obstaculo({'x':-430, 'y':130}))
        todos_obstaculos.append(crear_obstaculo({'x':-410, 'y':130}))
        todos_obstaculos.append(crear_obstaculo({'x':-390, 'y':130}))
        todos_obstaculos.append(crear_obstaculo({'x':-370, 'y':130}))
        todos_obstaculos.append(crear_obstaculo({'x':-350, 'y':130}))
        todos_obstaculos.append(crear_obstaculo({'x':-330, 'y':130}))
        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':110}))
        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':90}))
        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':70}))
        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':50}))
        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':30}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':110}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':90}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':70}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':50}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':30}))

        #Pared arriba derecha
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':450, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':430, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':410, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':390, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':370, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':350, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':330, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':130}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':130}))
        todos_obstaculos.append(crear_obstaculo({'x':450, 'y':130}))
        todos_obstaculos.append(crear_obstaculo({'x':430, 'y':130}))
        todos_obstaculos.append(crear_obstaculo({'x':410, 'y':130}))
        todos_obstaculos.append(crear_obstaculo({'x':390, 'y':130}))
        todos_obstaculos.append(crear_obstaculo({'x':370, 'y':130}))
        todos_obstaculos.append(crear_obstaculo({'x':350, 'y':130}))
        todos_obstaculos.append(crear_obstaculo({'x':330, 'y':130}))
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':110}))
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':90}))
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':70}))
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':50}))
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':30}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':110}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':90}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':70}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':50}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':30}))


        #Pared abajo izquierda
        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-450, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-430, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-410, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-390, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-370, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-350, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-330, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':-130}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':-130}))
        todos_obstaculos.append(crear_obstaculo({'x':-450, 'y':-130}))
        todos_obstaculos.append(crear_obstaculo({'x':-430, 'y':-130}))
        todos_obstaculos.append(crear_obstaculo({'x':-410, 'y':-130}))
        todos_obstaculos.append(crear_obstaculo({'x':-390, 'y':-130}))
        todos_obstaculos.append(crear_obstaculo({'x':-370, 'y':-130}))
        todos_obstaculos.append(crear_obstaculo({'x':-350, 'y':-130}))
        todos_obstaculos.append(crear_obstaculo({'x':-330, 'y':-130}))
        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':-110}))
        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':-90}))
        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':-70}))
        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':-50}))
        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':-30}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':-110}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':-90}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':-70}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':-50}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':-30}))


        #Pared abajo derecha
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':450, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':430, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':410, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':390, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':370, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':350, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':330, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':-130}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':-130}))
        todos_obstaculos.append(crear_obstaculo({'x':450, 'y':-130}))
        todos_obstaculos.append(crear_obstaculo({'x':430, 'y':-130}))
        todos_obstaculos.append(crear_obstaculo({'x':410, 'y':-130}))
        todos_obstaculos.append(crear_obstaculo({'x':390, 'y':-130}))
        todos_obstaculos.append(crear_obstaculo({'x':370, 'y':-130}))
        todos_obstaculos.append(crear_obstaculo({'x':350, 'y':-130}))
        todos_obstaculos.append(crear_obstaculo({'x':330, 'y':-130}))
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':-110}))
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':-90}))
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':-70}))
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':-50}))
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':-30}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':-110}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':-90}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':-70}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':-50}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':-30}))

        #Pared centro
        todos_obstaculos.append(crear_obstaculo({'x':-410, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':-390, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':-370, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':-350, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':-330, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':-290, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':-270, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':-250, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':-230, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':-210, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':-190, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':-170, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':-150, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':-130, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':-110, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':-90, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':-70, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':-50, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':50, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':70, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':90, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':110, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':130, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':150, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':170, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':190, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':210, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':230, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':250, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':270, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':290, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':330, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':350, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':370, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':390, 'y':0}))
        todos_obstaculos.append(crear_obstaculo({'x':410, 'y':0}))


    for cada_obstaculo in todos_obstaculos:
        if (cabeza.distance(cada_obstaculo)) < 20 and nivel == 3:
            #Game over
            game_over()


##################        Nivel 4      #########################################

    if puntaje == 80 and not nivel == 4:
        nivel = 4
        texto.clear()
        texto.write("Puntaje: {}     Maximo Puntaje: {}   Nivel: {}".format(puntaje, max_puntaje, nivel),
                align = "center", font =("Courier", 18, "normal"))

        letrero_n4 = turtle.Turtle()
        letrero_n4.speed(0)
        letrero_n4.color("white")
        letrero_n4.penup()
        letrero_n4.hideturtle()
        letrero_n4.goto(-180,0)
        letrero_n4.write("NIVEL 4", font =("Courier", 50, "normal"))
        letrero_n4.clear()
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        time.sleep(2)


        #Esconder los Segmentos
        for segmento in segmentos:
            segmento.goto(1000,1000)

        #Limpiar lista de Segmentos
        segmentos.clear()

        #Limpiar los obstaculos
        limpiar_obstaculos()

        #Obstaculos
        #Pared arriba
        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-450, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-430, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-410, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-390, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-370, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-350, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-330, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-290, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-270, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-250, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-230, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-210, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-190, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-170, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-150, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-130, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-110, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-90, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-70, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-50, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-30, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-10, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':10, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':30, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':50, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':70, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':90, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':110, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':130, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':150, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':170, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':190, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':210, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':230, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':250, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':270, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':290, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':330, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':350, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':370, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':390, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':410, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':430, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':450, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':190}))

        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-450, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-410, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-390, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-370, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-430, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-350, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-330, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-290, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-270, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-250, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-230, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-210, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-190, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-170, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-150, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-130, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-110, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-90, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-70, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-50, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-30, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':-10, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':10, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':30, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':50, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':70, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':90, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':110, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':130, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':150, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':170, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':190, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':210, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':230, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':250, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':270, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':290, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':330, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':350, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':370, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':390, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':410, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':430, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':450, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':210}))
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':210}))


        #Pared abajo
        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-450, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-430, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-410, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-390, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-370, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-350, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-330, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-290, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-270, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-250, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-230, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-210, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-190, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-170, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-150, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-130, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-110, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-90, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-70, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-50, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-30, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-10, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':10, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':30, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':50, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':70, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':90, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':110, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':130, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':150, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':170, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':190, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':210, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':230, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':250, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':270, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':290, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':330, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':350, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':370, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':390, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':410, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':430, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':450, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':-190}))

        todos_obstaculos.append(crear_obstaculo({'x':-490, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-470, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-450, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-410, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-390, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-370, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-430, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-350, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-330, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-290, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-270, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-250, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-230, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-210, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-190, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-170, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-150, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-130, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-110, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-90, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-70, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-50, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-30, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-10, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':10, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':30, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':50, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':70, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':90, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':110, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':130, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':150, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':170, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':190, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':210, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':230, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':250, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':270, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':290, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':330, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':350, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':370, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':390, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':410, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':430, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':450, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':470, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':490, 'y':-210}))

        #muro centro
        todos_obstaculos.append(crear_obstaculo({'x':0, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':0, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':0, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':0, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':0, 'y':-130}))
        todos_obstaculos.append(crear_obstaculo({'x':0, 'y':-110}))
        todos_obstaculos.append(crear_obstaculo({'x':0, 'y':-90}))
        todos_obstaculos.append(crear_obstaculo({'x':0, 'y':-70}))
        todos_obstaculos.append(crear_obstaculo({'x':0, 'y':-50}))
        todos_obstaculos.append(crear_obstaculo({'x':0, 'y':50}))
        todos_obstaculos.append(crear_obstaculo({'x':0, 'y':70}))
        todos_obstaculos.append(crear_obstaculo({'x':0, 'y':90}))
        todos_obstaculos.append(crear_obstaculo({'x':0, 'y':110}))
        todos_obstaculos.append(crear_obstaculo({'x':0, 'y':130}))
        todos_obstaculos.append(crear_obstaculo({'x':0, 'y':150}))
        todos_obstaculos.append(crear_obstaculo({'x':0, 'y':170}))
        todos_obstaculos.append(crear_obstaculo({'x':0, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':0, 'y':210}))

        #muro izquierdo
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':-130}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':-110}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':-90}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':-70}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':-50}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':-30}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':-10}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':10}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':30}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':50}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':70}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':90}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':-310, 'y':210}))

        #muro derecho
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':-210}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':-190}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':-170}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':-150}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':-130}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':-110}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':-90}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':-70}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':-50}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':-30}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':-10}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':10}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':30}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':50}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':70}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':90}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':190}))
        todos_obstaculos.append(crear_obstaculo({'x':310, 'y':210}))

    for cada_obstaculo in todos_obstaculos:
        if (cabeza.distance(cada_obstaculo)) < 20 and nivel == 4:
            #Game over
            game_over()
            limpiar_obstaculos()

    if puntaje == 100:

        ganar_sound()
        limpiar_obstaculos()
        comida.hideturtle()
        cabeza.hideturtle()
        cabeza.goto(1000,1000)
        for segmento in segmentos:
            segmento.goto(1000,1000)

        ventana = turtle.Screen()
        ventana.title("Juego Snake Proyecto UdeA")
        ventana.bgcolor("black")
        #Activar el fondo
        ventana.bgpic("you_win.gif")
        ventana.setup(width = 1300, height = 1100)
        ventana.tracer(0)

        time.sleep(5)
        jugando = False

    time.sleep(posponer)
