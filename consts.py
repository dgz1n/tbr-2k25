from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Drive_Train import claw, andar, turn, rotate, cs1, cs2

hub = PrimeHub()

colors = (Color.GREEN, Color.BLUE, Color.GRAY, Color.YELLOW)


def Open():
  claw.run_target(2000, 0)

def close():
    claw.run_target(2000, -20)

def mid():
    claw.run_target(2000, -200)

def deposit():
    claw.run_target(1800, -400)

def indo():
    wait(200)
    if 
    cs2.color() == Color.GREEN
    deposit()

    else
    andar(10)
    Stop()
    wait(200)