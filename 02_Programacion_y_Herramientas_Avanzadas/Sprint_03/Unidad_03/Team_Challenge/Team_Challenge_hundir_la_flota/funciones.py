import numpy as np
import variables as vars

def obtener_tupla():
    while True:
        entrada = input("Por favor, introduce una tupla de dos números enteros entre 0 y 9 separados por coma (por ejemplo, 1,2): ")
        try:
            # Dividir la entrada por comas
            partes = entrada.split(',')
            for elem in partes:
                if (int(elem.strip()) > 9) or (int(elem.strip()) < 0):
                    raise ValueError("Los números de la tupla tienen que estar entre el 0 y 9.")

            if len(partes) != 2:
                raise ValueError("Debes introducir exactamente dos números.")

            if (0 > int(partes[0].strip()) > 9) or (0 > int(partes[1].strip()) > 9):
                raise ValueError("Los números de la tupla tienen que estar entre el 0 y 9.")
            
            # Convertir las partes en enteros
            tupla = (int(partes[0].strip()), int(partes[1].strip()))
            return tupla
        except ValueError as e:
            print(f"Entrada inválida: {e}. Inténtalo de nuevo.")
    

def introducir_input():
    datos_erroneos = True
    while datos_erroneos:
        try:
            pos_inicial = obtener_tupla()

            tam = int(input("Tamaño que va a tener el barco:"))
            if tam not in vars.tam_barcos:
                raise ValueError ("No puedes introducir un barco de este tamaño, los posibles tamaños de barcos que quedan son:", vars.tam_barcos)
            
            orientacion = input("Orientación del barco (N, S, E, O):")
            if not orientacion.lower() in vars.p_cardinales:
                raise ValueError("La orientación tiene que ser N, S, E, O.")
            datos_erroneos = False
        except Exception as e:
            print("No se han introducido bien los datos", e)
    return  pos_inicial, tam, orientacion

# función que comprueba si el input es de la forma (0,0),3,N
def comprobar_barco(barco):
    ok = True
    if ((isinstance(barco, tuple)) and (len(barco) == 3)):
        for elem in barco[0]: # comprobamos que el primer valor es una tupla de números positivos
            if not isinstance(elem, int) or (0 > elem > 9):
                print("El primer valor no es una tupla de enteros.")
                ok = False
                break
        if not (isinstance(barco[1], int) or (barco[1] in vars.tam_barcos)):
            print("El segundo valor no es un tamaño válido de barco.")
            ok = False
        if not (isinstance(barco[2], str) or (barco[2].lower() in ["n", "s", "e", "o"])):
            print("El tercer valor tiene que ser una letra de las siguientes: N, S, E, O")
            ok = False

    else:
        print("Introduzca una tupla de tres valores \
              (posición inicial, tamaño del barco, orientaión). P.e: ((0,0),3,N)")
        ok = False

    return ok


# comprueba si las coordenadas no son negativas
def check_coord(tablero, tupla_coord):
    # rango 0,9
    cond_1 = tupla_coord[0] < 0 or tupla_coord[0] > 9
    cond_2 = tupla_coord[1] < 0 or tupla_coord[1] > 9
    if (cond_1) or (cond_2):
        print("El barco se sale del tablero")
        return False
    elif (tablero[tupla_coord] != " "):
        print("Hay una posición que ya está ocupada por otro barco")
        return False
    else:
        return True


def random_boat_constructor(board, boat, length_boat, card_point):
    card_point = card_point.lower()
    print(f"Construyendo el barco desde {boat[0]} con longitud {length_boat} y orientación '{card_point}'")
    if card_point == "n":
        for i in range(1,length_boat):
            if boat[0][0] != 0:
                boat.append((int(boat[0][0])-i, int(boat[0][1])))
            else:
                print("No se puede construir, te vas a salir del tablero")
    elif card_point == "s":
        for i in range(1,length_boat):
            if boat[0][0] != board.shape[0]-1: # ancho de la matriz
                boat.append((int(boat[0][0])+i, int(boat[0][1])))
            else:
                print("No se puede construir, te vas a salir del tablero")
    elif card_point == "e":
        for i in range(1,length_boat):
            if boat[0][1] != 0: # ancho de la matriz board.shape[1]-1
                boat.append((int(boat[0][0]), int(boat[0][1])+i))
            else:
                print("No se puede construir, te vas a salir del tablero")
    elif card_point == "o":
         for i in range(1,length_boat):
            if boat[0][1] != board.shape[1]-1: # ancho de la matriz board.shape[1]-1
                boat.append((int(boat[0][0]), int(boat[0][1])-i))
            else:
                print("No se puede construir, te vas a salir del tablero")
    else:
            print("Ese punto cardinal no exite")
    
    return boat
    
def check_random_boat(random_boat):
    for positions in random_boat:
        if positions[0] < 0 or positions[1] < 0:
            print("No se puede insertar el barco en el tablero, hay posiciones negativas que no admitimos.")
            ok = 0
            break
        else:
            ok = 1
    return ok

def boat_positions(board, *args):
    for boat in args:  # recorro los barcos
        for boat_pos in boat: # recorro las tuplas de las posiciones de los barcos
            try:
                if board[boat_pos[0]][boat_pos[1]] == " ":
                    board[boat_pos[0]][boat_pos[1]] = "O" # coloco el barco donde toca
                elif board[boat_pos[0]][boat_pos[1]] == "O":
                    print("Este barco no se puede posicionar aquí, entra en conflicto con otro barco")
            except Exception as e:
                print("Creo que nos hemos salido del tablero", e)
    return board

# board: tablero
# boat: tupla de la info del barco (2,3),4,N
# card_point: dirección que va a tener el barco
def boat_constructor(tablero, pos_i_boat): # pos_i_boat = (2,3),4,N
    barco = []
    pos = pos_i_boat[0]
    card_point = pos_i_boat[2].lower()
    print(f"Construyendo el barco desde {pos_i_boat[0]} con longitud {pos_i_boat[1]} y orientación '{pos_i_boat[2]}'")

    if card_point == "n":
        for i in range(1,pos_i_boat[1]+1): # itero tantas veces como posiciones haya
            if check_coord(tablero, pos):
                #tablero[pos] = "O"
                barco.append(pos)
                pos = (pos[0] - 1, pos[1]) # restamos un dígito a la fila para orientar el barco en dirección N
            else:
                print("No se puede colocar aquí el barco, prueba otra posición")
                return(tablero, False)

    elif card_point == "s":
        for i in range(1,pos_i_boat[1]+1): # itero tantas veces como posiciones haya
            if check_coord(tablero, pos):
                #tablero[pos] = "O"
                barco.append(pos)
                pos = (pos[0] + 1, pos[1]) # aumentamos un dígito a la fila para orientar el barco en dirección S
            else:
                print("No se puede colocar aquí el barco, prueba otra posición")
                return(tablero, False)

    elif card_point == "e":
        for i in range(1,pos_i_boat[1]+1): # itero tantas veces como posiciones haya
            if check_coord(tablero, pos):
                #tablero[pos] = "O"
                barco.append(pos)
                pos = (pos[0], pos[1] + 1) # restamos un dígito a la fila para orientar el barco en dirección E
            else:
                print("No se puede colocar aquí el barco, prueba otra posición")
                return(tablero, False)

    elif card_point == "o":
         for i in range(1,pos_i_boat[1]+1): # itero tantas veces como posiciones hay
            if check_coord(tablero, pos):
                #tablero[pos] = "O"
                barco.append(pos)
                pos = (pos[0], pos[1] - 1) # restamos un dígito a la fila para orientar el barco en dirección O

            else:
                print("No se puede colocar aquí el barco, prueba otra posición")
                return(tablero, False)

    else:
            print("Ese punto cardinal no exite")
            return(tablero, False)
    
    return (tablero, check_coord(tablero, pos), barco)


# tablero = np.array
# pos = (2,3)
def disparar(tablero, pos):
    tocado = False
    if tablero[pos] == "O":
        tablero[pos] = "X"
        tocado = True
        print("¡¡¡BOOM!!! Barco tocado")
    elif tablero[pos] == "X":
        print("Agonía deja de perder el tiempo, aqui ya has disparado antes...")
    else:
        tablero[pos] = '-'
    return tocado


def imprimir_tablero(jugador):
    caracter = '='
    n = 45
    tablero_2 = jugador + "_disp"
    print(vars.dic_tableros[tablero_2])
    print(caracter * n)
    print(vars.dic_tableros[jugador])

def reiniciar_partida():
    tam = 10
    vars.tam_barcos = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    vars.dic_vidas = {"jugador": 20,"maquina": 20}
    vars.dic_tableros = {"jugador": np.full((tam, tam), " ", dtype=object), # donde estén nuestros barcos
                "jugador_disp": np.full((tam, tam), " ", dtype=object), # donde vamos a disparar
                "maquina": np.full((tam, tam), " ", dtype=object), 
                "maquina_disp": np.full((tam, tam), " ", dtype=object),}