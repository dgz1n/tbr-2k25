from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Drive_Train import andar, rotate, turn
from consts import Open, close, upper, low, mid, deposit, cancela_esquerda, cancela_direita, volta_direita, volta_esquerda, direita_direto, esquerda_direto
from functions import detect_train_I, detect_train_II, detect_train_III, detect_train_IV
from Rotas import route_VI_amarelo, route_VI_azul, route_VI_cinza, route_VI_verde, 
from Rotas import route_V, park


hub = PrimeHub()

#cancela_direita()
#andar(2)
#wait(500)
#detect_train_II()

#upper()
#wait(500)
#cancela_direita()
#wait(300)
#andar(3.4)
#detect_train_IV()
#boxB()
#boxG_cinza():

    #rotate(-25)
    #andar(60)
   # rotate(-65)
    #wait(200)
#    andar(27)
 #   wait(100)
  #  rotate(90)
   # wait(100)
    #andar(8)
 #   wait(100)
  #  Open()
  #  wait(500)
   # andar(-17)
   # rotate(-90)
#detect_train_III()

while True:
    battery_voltage = hub.battery.voltage()
    print("Nivel da bateria", battery_voltage / 1000, "V")
    wait(1000) 
