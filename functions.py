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


def azul_TI(): 
    andar(45)
    wait(500)
    andar(-25)
    volta_esquerda()

def amarelo_TI(): 
    andar(22)
    volta_esquerda()

def cinza_TI(): 
    andar(13)
    volta_esquerda()

def verde_TI(): 
    andar(34)
    volta_esquerda()

train_I = {
    Color.BLUE: azul_TI,
    Color.YELLOW: amarelo_TI,
    Color.RED: cinza_TI,
    Color.GREEN: verde_TI
}


def azul_TII(): 
    andar(45)
    wait(500)
    andar(-25)
    volta_direita()

def amarelo_TII(): 
    andar(22)
    volta_direita()

def cinza_TII(): 
    andar(13)
    volta_direita()

def verde_TII(): 
    andar(34)
    volta_direita()

train_II = {
    Color.BLUE: azul_TII,
    Color.YELLOW: amarelo_TII,
    Color.RED: cinza_TII,
    Color.GREEN: verde_TII
}


def azul_TIII(): 
    andar(45)
    wait(500)
    andar(-25)
    volta_direita()

def amarelo_TIII(): 
    andar(22)
    volta_direita()

def cinza_TIII(): 
    andar(13)
    volta_direita()

def verde_TIII(): 
    andar(34)
    volta_direita()

train_III = {
    Color.BLUE: azul_TIII,
    Color.YELLOW: amarelo_TIII,
    Color.RED: cinza_TIII,
    Color.GREEN: verde_TIII
}


def azul_TIV(): 
    andar(45)
    wait(500)
    andar(-25)
    volta_direita()

def amarelo_TIV(): 
    andar(22)
    volta_direita()

def cinza_TIV(): 
    andar(13)
    volta_direita()

def verde_TIV(): 
    andar(34)
    volta_direita()

train_IV = {
    Color.BLUE: azul_TIV,
    Color.YELLOW: amarelo_TIV,
    Color.RED: cinza_TIV,
    Color.GREEN: verde_TIV
}


def detect_train_I():
    train_I[colors_esq]()

def detect_train_II():
    train_II[colors_dir]()

def detect_train_III():
    train_III[colors_dir]()

def detect_train_IV():
    train_IV[colors_dir]()
    