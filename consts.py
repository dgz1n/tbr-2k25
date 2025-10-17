from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Drive_Train import claw, andar, turn, rotate, cancela

hub = PrimeHub()

colors = (Color.GREEN, Color.BLUE, Color.GRAY, Color.YELLOW)
#andar(15) -> trem cinza
#andar(26) -> trem amarelo
#andar(35) -> trem verde
#andar(45) -> trem azul
#andar(30) -> sair da plataforma(com a regua)
#o andar para trás tem que ser sempre -4 do valor que vai para frente
#Ex: andar(20) / andar(-24)


def Open():
    claw.run_target(2000, 40)

def close():
    claw.run_target(2000, 430)

def low():
    claw.run_target(2000, 320)

def mid():
    claw.run_target(2000, 380)

def upper():
    claw.run_target(2000, 560)

def deposit():
    claw.run_target(1800, 770)

def cancela_esquerda():
    cancela.run_angle(1800, 170)

def volta_esquerda():
    cancela.run_angle(1800, -105)

def cancela_direita():
    cancela.run_angle(1800, -180)

def volta_direita():
    cancela.run_angle(1800, 150)

def direita_direto():
    cancela.run_angle(1950, 150)

def esquerda_direto():
    cancela.run_angle(1950, -250)

