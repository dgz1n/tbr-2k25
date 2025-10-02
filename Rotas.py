from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from consts import Open, close, low, mid, deposit, cancela_esquerda, cancela_direita, volta_direita, volta_esquerda
from Drive_Train import claw, andar, turn, rotate, cancela

hub = PrimeHub()


# SAI DA BASE
def route_I():
    andar(25)
    close()
    rotate(-90)
    andar(30)

# VAI PARA O TREM
def train_I():
    rotate(-90)
    andar(16)
    rotate(90)
    andar(18)

#caminho até a caixa verde
def route_II():
    rotate(90)
    andar(45)
    rotate(90)
    andar(20)


def route_III():
    andar(-40)
    rotate(90)
    cancela_direita()

#caminho para depositar a caixa verde
def boxG():
    rotate(-90)
    andar(30)
    rotate(90)
    andar(5)

#caminho até a caixa azul
def route_IV():
    andar(-30)
    rotate(-90)
    andar(60)
    rotate(-90)

#caixa azul
def boxB():
    andar(15)
    low()
    andar(-15)
    rotate(90)
    Open()

def train_III():
    rotate(90)
    andar(20)
    rotate(90)
    cancela_direita()

def train_IV():
    rotate(-90)
    andar(20)

#estacionar
def park():
    rotate(-90)
    andar(65)
    rotate(90)
    andar(-5)
    deposit()

