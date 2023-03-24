import random


class Jugador():
    jugadas = ['piedra', 'papel', 'tijera']
    puntaje = 0
    def __init__ (self, nombre):
        self.nombre = nombre

    def tomar_desicion(self):
        while True:
            desicion = input(f" {self.nombre} ingresa una jugada: (piedra, papel, tijera) ").lower()
            if desicion in self.jugadas:
                print(f'{self.nombre} eligio {desicion}')
                return desicion
            else:
                print("Jugada invalida intentelo de nuevo")

class Computadora():
    jugadas = ['piedra', 'papel', 'tijera']
    nombre = "CiPiu"
    puntaje = 0

    def tomar_desicion(self):
        desicion = random.choice(self.jugadas)
        print(f'{self.nombre} eligio {desicion}')
        return desicion
        

class Juego():
    jugadas = ['piedra', 'papel', 'tijera']
    def __init__ (self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2 
        print(f'Batalla: {self.jugador1.nombre} vs {self.jugador2.nombre}')

    def jugar(self):
        desicion1 = self.jugador1.tomar_desicion()
        desicion2 = self.jugador2.tomar_desicion()
        desiciones = [desicion1, desicion2]

        desicion = {
            "opt1": ["piedra", "tijera"],
            "opt2": ["tijera", "papel"],
            "opt3": ["papel", "piedra"]
        } 

        if desiciones[0] == desiciones[1]:
            print(f"Empate ambos eligieron {desiciones[0]}")
        elif desiciones in desicion.values():
            self.jugador1.puntaje += 1
            print(f"Gana {self.jugador1.nombre} por que eligio {desiciones[0]} y {self.jugador2.nombre} eligio {desiciones[1]}")
        else:
            self.jugador2.puntaje += 1
            print(f"Gana {self.jugador2.nombre} por que eligio {desiciones[1]} y {self.jugador1.nombre} eligio {desiciones[0]}")
