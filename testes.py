from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Drive_Train import andar, rotate, turn
from consts import Open, close, low, mid, deposit
from functions import acoes

hub = PrimeHub()

# rota 1

# SAI DA BASE
andar(25)
close()
rotate(-90)
andar(30)

# VAI PARA O TREM
rotate(-90)
andar(16)
rotate(90)
andar(18)