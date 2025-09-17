from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
claw = Motor(Port.F, Direction.CLOCKWISE)
claw.brake
me = Motor(Port.A, Direction.COUNTERCLOCKWISE)
md = Motor(Port.B)
cancela = Motor(Port.C)
cs_dir = ColorSensor(Port.E)
cs_esq = ColorSensor(Port.D)

drive_base = DriveBase(me, md, 54, 115) 
drive_base.use_gyro(True)

def andar(dist):
    drive_base.settings(350, 350, 220, 220)
    drive_base.straight(dist*10)

def turn(radius, angle):
    drive_base.settings(200, 200, 200, 200)
    drive_base.curve(radius, angle)

def rotate(graus):
    drive_base.settings(220, 220, 220, 220)
    drive_base.turn(graus)
