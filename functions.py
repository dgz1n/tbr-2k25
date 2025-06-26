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

def get_train_color:
    lastColor = cs2.color()

def find_train_color:
    andar()
    get_train_color()

def make_train(Lado):
    lado = Lado
    match lado:
        case 1:
            lado*1
        case 2:
            lado*-1
    
def delivery_train:
    match lastColor:
        case Color.GRAY:
            andar(10*lado)
        case Color.YELLOW:
            andar(20*lado)
        case Color.GREEN:
            andar(30*lado)
        case Color.BLUE:
            andar(50*lado)    