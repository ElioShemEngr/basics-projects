print("E P I C    🪨  📄 ✂️  🦎 🖖   B A T T L E --- Versión 2.0")
print()

#Scores de Jugadores
scoreJugador1: int = 0
scoreJugador2: int = 0

#Contador de ronda
round: int = 1

while True:
  if scoreJugador1 == 3 or scoreJugador2 == 3:
    break
  else:
    print()
    print("Ronda ", round)
    print()
    print("Score actual:")
    print("Jugador 1 = ", scoreJugador1, " puntos")
    print("Jugador 2 = ", scoreJugador2, " puntos")
    print()
    print("Selecciona tu movimiento (R, P, T, L o S)")
    print()
    jugador_1 = input("Jugador 1 > ")
    print()
    jugador_2 = input("Jugador 2 > ")
    print()
    round += 1
    #Si Jugador 1 elige Roca(R)
    if jugador_1=="R":
      if jugador_2=="R":
        print("Es un empate")
      elif jugador_2=="P":
        print("Papel cubre Roca, Gana Jugador 2")
        scoreJugador2 += 1
      elif jugador_2=="T":
        print("Roca rompe tijeras, Gana Jugador 1")
        scoreJugador1 += 1
      elif jugador_2=="L":
        print("Roca mata lagarto, Gana Jugador 1")
        scoreJugador1 += 1
      elif jugador_2=="S":
        print("Spock vaporiza Roca, Gana Jugador 2")
        scoreJugador2 += 1
      else:
        print("Elección de Jugador 2, Invalida")
    #Si Jugador 1 elige Papel(P)
    elif jugador_1=="P":
      if jugador_2=="P":
        print("Es un empate")
      elif jugador_2=="R":
        print("Papel cubre Roca, Gana Jugador 1")
        scoreJugador1 += 1
      elif jugador_2=="T":
        print("Tijeras cortan Papel, Gana Jugador 2")
        scoreJugador2 += 1
      elif jugador_2=="L":
        print("Lagarto come papel, Gana Jugador 2")
        scoreJugador2 += 1
      elif jugador_2=="S":
        print("Papel desautoriza Spock, Gana Jugador 1")
        scoreJugador1 += 1
      else:
        print("Elección de Jugador 2, Invalida")
    #Si Jugador 1 elige Tijeras(T)
    elif jugador_1=="T":
      if jugador_2=="T":
        print("Es un empate")
      elif jugador_2=="R":
        print("Roca rompe tijeras, Gana Jugador 2")
        scoreJugador2 += 1
      elif jugador_2=="P":
        print("Tijeras cortan Papel, Gana Jugador 1")
        scoreJugador1 += 1
      elif jugador_2=="L":
        print("Tijeras decapitan lagarto, Gana Jugador 1")
        scoreJugador1 += 1
      elif jugador_2=="S":
        print("Spock rompe tijeras, Gana Jugador 2")
        scoreJugador2 += 1
      else:
        print("Elección de Jugador 2, Invalida")
    #Si Jugador 1 elige Lagarto(L)
    elif jugador_1=="L":
      if jugador_2=="L":
        print("Es un empate")
      elif jugador_2=="R":
        print("Roca aplasta lagarto, Gana Jugador 2")
        scoreJugador2 += 1
      elif jugador_2=="P":
        print("Lagarto come papel, Gana Jugador 1")
        scoreJugador1 += 1
      elif jugador_2=="T":
        print("Tijeras decapitan lagarto, Gana Jugador 2")
        scoreJugador2 += 1
      elif jugador_2=="S":
        print("Lagarto envenena a Spock, Gana Jugador 1")
        scoreJugador1 += 1
      else:
        print("Elección de Jugador 2, Invalida")
    #Si Jugador 1 elige Spock(S)
    elif jugador_1=="S":
      if jugador_2=="S":
        print("Es un empate")
      elif jugador_2=="R":
        print("Spock vaporiza roca, Gana Jugador 1")
        scoreJugador1 += 1
      elif jugador_2=="P":
        print("Papel desautoriza Spock, Gana Jugador 2")
        scoreJugador2 += 1
      elif jugador_2=="T":
        print("Spock rompe tijeras, Gana Jugador 1")
        scoreJugador1 += 1
      elif jugador_2=="L":
        print("Lagarto envenena Spock, Gana Jugador 2")
        scoreJugador2 += 1
      else:
        print("Elección de Jugador 2, Invalida")
    #Si Jugador 1 elige Mal
    else:
      print("Elección de Jugador 1, Invalida")
