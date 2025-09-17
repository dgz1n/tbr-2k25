from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Drive_Train import claw, andar, turn, rotate, cs_dir, cs_esq
from consts import cancela_direita, cancela_esquerda, volta_direita, volta_esquerda


hub = PrimeHub()
colors_dir = cs_dir.color()
colors_esq = cs_esq.color()


#funçoes de detecçao das cores dos trens👍

def azul(): 
    cancela_esquerda()
    andar(45)
    wait(500)
    andar(-25)
    volta_esquerda()
#girar 90° positivo ou negativo(ao final)
def amarelo(): 
    cancela_esquerda()
    andar(22)
#girar 90° positivo ou negativo(ao final)
def cinza(): 
    cancela_esquerda()
    andar(13)
#girar 90° positivo ou negativo(ao final)
def verde(): 
    cancela_esquerda()
    andar(34)
#girar 90° positivo ou negativo(ao final)
def find_color2():
    sensor_cor2.color()
    cor = {
    Color.BLUE: azul,
    Color.YELLOW: amarelo,
    Color.RED: cinza,
    Color.GREEN: verde, 
}     

cor = {
    Color.BLUE: azul,
    Color.YELLOW: amarelo,
    Color.RED: cinza,
    Color.GREEN: verde,
}



def azul(): 
    cancela_direita()
    andar(45)
    wait(500)
    andar(-25)
    volta_direita()
#girar 90° positivo ou negativo(ao final)
def amarelo(): 
    cancela_direita()
    andar(22)
#girar 90° positivo ou negativo(ao final)
def cinza(): 
    cancela_direita()
    andar(13)
#girar 90° positivo ou negativo(ao final)
def verde(): 
    cancela_direita()
    andar(34)
    volta_direita()
    wait(100)
    
#girar 90° positivo ou negativo(ao final)
  

cor_dir = {
    Color.BLUE: azul,
    Color.YELLOW: amarelo,
    Color.RED: cinza,
    Color.GREEN: verde,
}

cor_dir[colors_dir]()