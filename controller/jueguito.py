from entidades import Jugador, Computadora, Juego


jugador1 = Jugador("Pepe")
jugador2 = Computadora()
jugador3 = Computadora()
jugador4 = Jugador("Juan")
jugador5 = Jugador("Pablo")   

nuevo_juego = Juego(jugador1, jugador2)
nuevo_juego.jugar()