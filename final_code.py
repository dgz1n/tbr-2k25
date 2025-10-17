from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from consts import Open, close, low, mid, deposit, cancela_esquerda, cancela_direita, volta_direita, volta_esquerda, direita_direto,esquerda_direto
from Drive_Train import claw, andar, turn, rotate, cancela
from functions import detect_train_I, detect_train_II, detect_train_III, detect_train_IV
from Rotas import route_I, route_II, route_III, route_IV, route_V, train_I, train_III, park, boxB_


hub = PrimeHub()


#linhas 25;26;27 não fazem parte de uma rota


route_I()
wait(400)
train_I()
detect_train_I()

route_II()
wait(300)

route_III()
wait(400)
detect_train_II()

route_IV() 

train_III()
detect_train_III()
route_V()
detect_train_IV()
boxB_()
park()



#cancela_esquerda()
#rotate(-90)
#volta_esquerda()
#detect_train_IV()
