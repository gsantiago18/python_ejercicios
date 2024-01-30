import random

print("**********")
print("Bienvenidos al buscaminas")
print("*********")

bandera = 0
while bandera == 0:
    bandera = 1
    tablero_size = int(input("De qué tamaño quieres el tablero?: "))
    num_minas = int(input("¿Cuántas minas deseas?: "))

    # Crear tablero del jugador y tablero del programa
    tablero_jugador = ["_" for _ in range(tablero_size**2)]
    tablero_programa = ["_" for _ in range(tablero_size**2)]
    minas_idx = random.sample(range(tablero_size**2), num_minas)

    # Ubicar las minas en el tablero del programa
    for idx in minas_idx:
        tablero_programa[idx] = "o"

    while True:
        
        print(tablero_jugador)

        # Turno del jugador 1
        print("Jugador #1 seleccionado ")
        x = int(input("Digite casilla: "))
        
        if tablero_programa[x] == "_":
            tablero_jugador[x] = "x"
            print(tablero_jugador)
            

        elif tablero_programa[x] == "o":
            print("Perdiste")
            bandera = 0
            break

        # Verificar si todas las casillas vacías han sido descubiertas
        if "_" not in tablero_jugador:
            print("¡Ganaste!")
            bandera = 0
            break

        # Turno del jugador 2
        print("Jugador #2 seleccionado ")
        x = int(input("Digite casilla: "))

        if tablero_programa[x] == "_":
            tablero_jugador[x] = "x"
            print(tablero_jugador)
        
        elif tablero_programa[x] == "o":
            print("Perdiste")
            bandera = 0
            break

        # Verificar si todas las casillas vacías han sido descubiertas
        if "_" not in tablero_jugador:
            print("¡Ganaste!")
            bandera = 0
            break

# Mostrar las ubicaciones de las minas al final del juego
    print("Ubicaciones de las minas:")
    for idx in minas_idx:
        print(idx, end=" ")

