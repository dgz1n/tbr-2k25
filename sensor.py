from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from functions import detect_train_I

hub = PrimeHub()
 colors_dir = cs_dir.color()
 colors_esq = cs_esq.color()
 cs_dir = ColorSensor(Port.E)
 cs_esq = ColorSensor(Port.D)


colors = (Color.GREEN, Color.BLUE, Color.GRAY, Color.YELLOW,)
#andar(15) -> trem cinza
#andar(25) -> trem amarelo
#andar(35) -> trem verde
#andar(45) -> trem azul
#andar(30) -> sair da plataforma(com a regua)

  
def trains_I():
    andar(34)
    cancela_esquerda()
    wait(4000)
    detect