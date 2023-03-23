from entidades import Jugador, Computadora, Juego


jugador1 = Jugador("Pepe", 0)
jugador2 = Computadora(0)
jugador3 = Computadora(0)
jugador4 = Jugador("Juan", 0)    

nuevo_juego = Juego(3, jugador1, jugador4)
nuevo_juego.jugar()

# escoger una jugada al azar


# si son iguales, es un empate

# piedra > tijera
# tijera > papel
# papel > piedra

    