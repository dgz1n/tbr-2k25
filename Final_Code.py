from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from consts import Open, close, low, mid, deposit, cancela_esquerda, cancela_direita, volta_direita, volta_esquerda
from Drive_Train import claw, andar, turn, rotate, cancela
from functions import detect_train_I, detect_train_II, detect_train_III, detect_train_IV
from Rotas import route_I, route_II, route_III, route_IV, train_I, train_III, train_IV, boxG, boxB, park

hub = PrimeHub()
#linhas 25;26;27 não fazem parte de uma rota

route_I()
train_I()
detect_train_I()
route_II()
low()
route_III()
detect_train_II()
boxG()
route_IV()
boxB()
train_III()
cancela_esquerda()
rotate(-90)
volta_esquerda()
detect_train_IV()
park()