from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Drive_Train import claw, andar, cs2, turn, rotate

hub = PrimeHub()
colors = (Color.GREEN, Color.BLUE, Color.GRAY, Color.YELLOW)
cs2.detectable_colors(colors)
cs2 = ColorSensor(Port.C)

#funçoes de detecçao das cores dos trens👍

def azul(): andar(45)
def amarelo(): andar(25)
def cinza(): andar(15)
def verde(): andar(35)

acoes = {
    Color.BLUE: azul,
    Color.YELLOW: amarelo,
    Color.RED: cinza,
    Color.GREEN: verde
}


#segue linha
while True:
    cor_detectada = cs2.color()

    if cor_detectada == Color.RED:
        print("🔴 Vermelho detectado!")
    elif cor_detectada == Color.BLUE:
        print("🔵 Azul detectado!")
    elif cor_detectada == Color.GREEN:
        print("🟢 Verde detectado!")
    elif cor_detectada == Color.YELLOW:
        print("🟡 Amarelo detectado!")
    elif cor_detectada == Color.BLACK:
        print("⚫ Preto detectado!")
    elif cor_detectada == Color.WHITE:
        print("⚪ Branco detectado!")
    else:
        print("❓ Cor desconhecida")

    wait(500)  # Espera meio segundo antes de verificar novamente
