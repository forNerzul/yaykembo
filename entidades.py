import random


class Jugador():
    jugadas = ['piedra', 'papel', 'tijera']
    def __init__ (self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje

    def tomar_desicion(self):
        desicion = input(f" {self.nombre} ingresa una jugada: (piedra, papel, tijera) ").lower()
        while (desicion not in self.jugadas):
            print("Jugada invalida intentelo de nuevo")
            desicion = input(f" {self.nombre} ingresa una jugada: (piedra, papel, tijera) ").lower()
        print(f'{self.nombre} eligio {desicion}')
        return desicion

class Computadora():
    jugadas = ['piedra', 'papel', 'tijera']
    nombre = "CiPiu"
    def __init__ (self, puntaje):
        self.puntaje = puntaje

    def tomar_desicion(self):
        desicion = random.choice(self.jugadas)
        print(f'{self.nombre} eligio {desicion}')
        return desicion
        

class Juego():
    jugadas = ['piedra', 'papel', 'tijera']
    def __init__ (self, oportunidades, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2 
        self.oportunidades = oportunidades
        print(f'Batalla: {self.jugador1.nombre} vs {self.jugador2.nombre}')

    def jugar(self):
        desicion1 = self.jugador1.tomar_desicion()
        desicion2 = self.jugador2.tomar_desicion()
        desiciones = [desicion1, desicion2]

        if desiciones[0] == desiciones[1]:
            print("Empate")
        elif (desiciones[0] == "piedra" and desiciones[1] == "tijera") or (desiciones[0] == "tijera" and desiciones[1] == "papel") or (desiciones[0] == "papel" and desiciones[1] == "piedra"):
            print(f"Gana {self.jugador1.nombre} por que eligio {desiciones[0]} y {self.jugador2.nombre} eligio {desiciones[1]}")
        else:
            print(f"Gana {self.jugador2.nombre} por que eligio {desiciones[1]} y {self.jugador1.nombre} eligio {desiciones[0]}")

        # Esta logica es simpicatica pero no se si da demasiado pete ya es 
        # if (desiciones[0] == "piedra" and desiciones[1] == "tijera"):
        #     print("Gana jugador 1")
        # elif (desiciones[0] == "tijera" and desiciones[1] == "papel"):
        #     print("Gana jugador 1")
        # elif (desiciones[0] == "papel" and desiciones[1] == "piedra"):
        #     print("Gana jugador 1")
        # elif (desiciones[0] == desiciones[1]):
        #     print("Empate")
        # else:
        #     print("Gana jugador 2")
