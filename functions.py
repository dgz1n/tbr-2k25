from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Drive_Train import claw, andar, turn, rotate

hub = PrimeHub()
#upcs = ColorSensor(Port.C)

#funçoes de detecçao das cores dos trens👍

def azul(): 
    andar(45)
    wait(500)
    andar(-25)
#girar 90° positivo ou negativo(ao final)
def amarelo(): 
    andar(25)
#girar 90° positivo ou negativo(ao final)
def cinza(): 
    andar(15)
#girar 90° positivo ou negativo(ao final)
def verde(): 
    andar(35)
    wait(500)
    andar(-10)
#girar 90° positivo ou negativo(ao final)

acoes = {
    Color.BLUE: azul,
    Color.YELLOW: amarelo,
    Color.RED: cinza,
    Color.GREEN: verde
}
