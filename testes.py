from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Drive_Train import andar, rotate, turn
from consts import Open, close, low, mid, deposit, cancela_esquerda, cancela_direita, volta_direita, volta_esquerda

hub = PrimeHub()

# rota 2
#rotate(90)
#andar(61)
#rotate(90)
#andar(14.2)


#low()andar(-15)rotate(90)andar(50)rotate(-90)andar(44)rotate(90)andar(3)Open()
low()
wait(300)
andar(20)
rotate(-90)
andar(32)
