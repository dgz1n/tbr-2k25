from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Drive_Train import claw, andar, cs1, cs2, turn, rotate

 hub = PrimeHub()
colors = (Color.GREEN, Color.BLUE, Color.GRAY, Color.YELLOW)
cs1.detectable_colors(colors)
cs2.detectable_colors(colors)

#funçoes de detecçao das cores dos trens👍

def azul(): andar(45)
def amarelo(): andar(25)
def cinza(): andar(15)
def verde(): andar(35)

acoes = {
    Color.BLUE: azul,
    Color.YELLOW: amarelo,
    Color.RED: cinza,
    Color.GREEN: verde
}

def detectar_cor():
    while True:
    detected_color = cs1.color()
    
    if detected_color == Color.BLUE:
        print("Blue detected!")
        hub.light.on(Color.BLUE)

    elif detected_color == Color.GREEN:
        print("Green detected!")
        hub.light.on(Color.GREEN)
        
    else:
        hub.light.off()
        print("Waiting for blue or green...")

    wait(200)

#segue linha
