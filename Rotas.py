from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Drive_Train import andar, turn, rotate
from consts import Open, close, low, mid, upper, deposit, cancela_esquerda, volta_esquerda, cancela_direita, volta_direita, direita_direto, esquerda_direto


hub = PrimeHub()

# rota 1
#andar(25)
#close()    
#rotate(-90)
#andar(30)


# SAI DA BASE
def route_I():
    andar(25)
    close()
    rotate(-90)
    andar(31)
    
# VAI PARA O TREM
def train_I():
    rotate(-90)
    andar(16.6)
    rotate(91)
    andar(32)
    wait(600)
    cancela_esquerda()
    

#caminho até a caixa verde
def route_II():
    rotate(65)
    andar(58.5)
    wait(100)
    rotate(97)
    wait(300)
    Open()
    wait(100)
    andar(17.5)
    wait(100)
    close()

#Caminho para fazer o trainII 
def route_III():
    andar(-22)
    wait(300)
    rotate(86)
    wait(300)
    direita_direto()
    wait(100)
    andar(-19)
    wait(200)
    rotate(23)
    wait(100)
    esquerda_direto()
    wait(400)
    andar(3)
    

#caminho para depositar a caixa verde
def boxG_azul():

    wait(200)
    rotate(-90)
    andar(16)
    rotate(90)
    wait(200)
    andar(45)
    wait(100)
    rotate(-90)
    wait(100)
    andar(38)
    wait(100)
    rotate(90)
    andar(18.5)
    Open()
    wait(500)
    andar(-14.5)
    rotate(-90)


def boxG_verde():

    wait(200)
    rotate(-90)
    andar(16)
    rotate(90)
    wait(200)
    andar(45)
    wait(100)
    rotate(-90)
    wait(100)
    andar(38)
    wait(100)
    rotate(90)
    andar(18.5)
    Open()
    wait(500)
    andar(-14.5)
    rotate(-90)


def boxG_amarelo():

    wait(400)
    rotate(-90)
    andar(17)
    rotate(90)
    wait(200)
    andar(44)
    wait(100)
    rotate(-90)
    wait(100)
    andar(38)
    wait(100)
    rotate(90)
    andar(18)
    Open()
    wait(500)
    andar(-14.5)
    rotate(-90)


def boxG_cinza():

    cancela_esquerda()
    wait(400)
    rotate(-25)
    andar(20)
    rotate(25)
    wait(200)
    andar(30)
    wait(100)
    rotate(-90)
    wait(100)
    volta_esquerda()
    wait(200)
    andar(45)
    wait(100)
    rotate(90)
    andar(16)
    Open()
    wait(500)
    andar(-17)
    rotate(-90)
    

#caminho até o trainIII
def route_IV():
    close()
    andar(65) 
    wait(100)
    
#fazer trainIII
def train_III():
    rotate(90)
    andar(23)
    upper()
    rotate(-90)
    andar(13)
    cancela_direita()
    andar(4)
    wait(300)
    


#caminho até o trainIV
def route_V():
    rotate(-11)
    andar(32)
    rotate(-79)
    cancela_direita()
    andar(17)

#fazer trainIV
def train_IV():
    rotate(-90)
    andar(18.5)
    


def route_VI_azul():
    rotate(-20)
    andar(48)
    rotate(-66)
    andar(32)
    rotate(-94)
    wait(300)
    andar(-6)
    wait(200)
    Open()
    wait(200)
    andar(7)
    wait(200)
    low()
    andar(-3.5)
    close()

def route_VI_amarelo():
    rotate(-20)
    andar(48)
    rotate(-66)
    andar(32)
    rotate(-94)
    wait(300)
    andar(-6)
    wait(200)
    Open()
    wait(200)
    andar(7)
    wait(200)
    low()
    andar(-3.5)
    close()

def route_VI_verde():
    rotate(-20)
    andar(48)
    rotate(-66)
    andar(32)
    rotate(-94)
    wait(300)
    andar(-6)
    wait(200)
    Open()
    wait(200)
    andar(7)
    wait(200)
    low()
    andar(-3.5)
    close()

def route_VI_cinza():
    rotate(-20)
    andar(48)
    rotate(-66)
    andar(32)
    rotate(-94)
    wait(300)
    andar(-6)
    wait(200)
    Open()
    wait(200)
    andar(7)
    wait(200)
    low()
    andar(-3.5)
    close()


def boxB_():
    rotate(90)
    andar(-41)
    rotate(90)
    andar(-50)
    rotate(90)
    andar(-40.1)
    Open()
    wait(100)
    

    

#estacionar
def park():
    andar(-15.55)
    deposit()
    rotate(-90)
    andar(47)
    