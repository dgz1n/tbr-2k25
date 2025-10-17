from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Drive_Train import claw, andar, turn, rotate, cs_dir, cs_esq
from consts import cancela_direita, cancela_esquerda, volta_direita, volta_esquerda, deposit
from Rotas import boxG_amarelo, boxG_azul, boxG_cinza, boxG_verde, route_VI_amarelo, route_VI_azul, route_VI_cinza, route_VI_verde,route_I

hub = PrimeHub()
colors_dir = cs_dir.color()
colors_esq = cs_esq.color()



        

def azul_TI(): 
   
    deposit()
    andar(46)
    wait(500)
    andar(-50)
    volta_esquerda()
    

def amarelo_TI(): 
   
    andar(25)
    andar(-29)
    volta_esquerda()

def cinza_TI(): 
   
    andar(15)
    andar(-19)
    volta_esquerda()

def verde_TI(): 
   
    andar(35)
    andar(-39)
    volta_esquerda()

train_I = {
    
    Color.BLUE: azul_TI,
    Color.YELLOW: amarelo_TI,  
    Color.RED: cinza_TI, 
    Color.GREEN: verde_TI,
    Color.WHITE: cinza_TI,
}


def azul_TII(): 
    
    andar(45)
    wait(500)
    andar(-47)
    volta_direita()
    boxG_azul()


def amarelo_TII(): 
   
    andar(24)
    wait(300)
    andar(-26)
    wait(200)
    volta_direita()
    boxG_amarelo()

def cinza_TII(): 
   
    andar(13)
    wait(100)
    andar(-15)
    wait(100)
    volta_direita()
    boxG_cinza()

def verde_TII(): 
   
    andar(34)
    andar(-36)
    volta_direita()
    boxG_verde()

train_II = {
   
    Color.BLUE: azul_TII,
    Color.YELLOW:amarelo_TII,
    Color.RED: cinza_TII,
    Color.GREEN: verde_TII,
    Color.WHITE: cinza_TII
}


def azul_TIII(): 
    
    andar(42.5)
    wait(500)
    andar(-44.5)
    volta_direita()

def amarelo_TIII(): 
   
    andar(25)
    andar(-27)
    volta_direita()

def cinza_TIII(): 
   
    andar(15)
    andar(-17)
    volta_direita()

def verde_TIII(): 
    
    andar(35)
    andar(-37)
    volta_direita()

train_III = {
    
    Color.BLUE: azul_TIII,
    Color.YELLOW: amarelo_TIII,
    Color.RED: cinza_TIII,
    Color.GREEN: verde_TIII,
    Color.WHITE: cinza_TIII
}


def azul_TIV(): 
    
    andar(45)
    wait(500)
    andar(-47)
    volta_direita()
    wait(200)
    route_VI_azul()

def amarelo_TIV(): 
    
    andar(25)
    andar(-27)
    volta_direita()
    wait(200)
    route_VI_amarelo()

def cinza_TIV(): 
    
    andar(15)
    andar(-17)
    volta_direita()
    wait(200)
    route_VI_cinza()

def verde_TIV(): 
   
    andar(35)
    andar(-37)
    volta_direita()
    wait(200)
    route_VI_verde()

train_IV = {
   
    Color.BLUE: azul_TIV,
    Color.YELLOW: amarelo_TIV,
    Color.RED: cinza_TIV,
    Color.GREEN: verde_TIV,
    Color.WHITE: cinza_TIV
}

def detect_train_I():
    while cs_dir.color() == Color.NONE and cs_esq.color() == Color.NONE:
        andar(0.5)
    colors_dir = cs_dir.color()
    colors_esq = cs_esq.color()
    
    train_I[colors_esq]()

def detect_train_II():
    while cs_dir.color() == Color.NONE and cs_esq.color() == Color.NONE:
        andar(0.5)
    colors_dir = cs_dir.color()
    colors_esq = cs_esq.color()

    train_II[colors_dir]()

def detect_train_III():
    while cs_dir.color() == Color.NONE and cs_esq.color() == Color.NONE:
        andar(0.5)
    colors_dir = cs_dir.color()
    colors_esq = cs_esq.color()
    train_III[colors_dir]()

def detect_train_IV():
    while cs_dir.color() == Color.NONE and cs_esq.color() == Color.NONE:
        andar(0.5)
    colors_dir = cs_dir.color()
    colors_esq = cs_esq.color()
    train_IV[colors_dir]()

