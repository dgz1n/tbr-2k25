from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Drive_Train import claw, andar, upcs, turn, rotate

hub = PrimeHub()
detect = upcs.color()
upcs = ColorSensor(Port.C)

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

cor = upcs.color()
acoes[cor]()
