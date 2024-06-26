import funciones as f
import random
import variables as vars
import sys
import os

# Función para redirigir la salida estándar a /dev/null
def block_print():
    sys.stdout = open(os.devnull, 'w')

# Función para restaurar la salida estándar
def enable_print():
    sys.stdout = sys.__stdout__

def main():
     # A partir de aqui, introducimos barcos del jugador con sus comprobaciones
    #barcos_restantes_jugador = vars.tam_barcos.copy()
    #barcos_restantes_maquina = vars.tam_barcos.copy()
    
    ############### input jugador ######################################################3
    while vars.tam_barcos: #barcos_restantes_jugador
        print("Barcos restantes para colocar:", vars.tam_barcos) #barcos_restantes_jugador
        print(vars.dic_tableros["jugador"]) 
        print("Posición inicial a partir de la que se va a empezar a construir el barco.")
        barco = f.introducir_input()
        if barco[1] == 1:
            barco_construido = (vars.dic_tableros["jugador"], f.check_coord(vars.dic_tableros["jugador"], barco[0]))
            if barco_construido[1]:
                vars.dic_tableros["jugador"][barco[0]] = "O"
        else:
            barco_construido = f.boat_constructor(vars.dic_tableros["jugador"], barco) # añadimos el barco al tablero
            if len(barco_construido) == 3 and barco_construido[1]:
                for pos in barco_construido[2]:
                    vars.dic_tableros["jugador"][pos] = "O"
        if barco_construido[1]:
            print(f"El barco que se va a poner en el tablero -> {barco}")
            vars.tam_barcos.remove(int(barco[1])) #barcos_restantes_jugador  si es valido borramos el barco de la lista            
    # En este punto deberíamos de tener el tablero del jugador creado con barcos y todo
    #################################################################################################
    
    ############### input maquina ######################################################
    vars.tam_barcos = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    block_print()
    while vars.tam_barcos:
        pos_ini = (random.randint(0,9), random.randint(0,9)) # posicion a partir de la cual vamos a introducir las coordenadas
        tam_barco = int(random.choice(vars.tam_barcos)) # barco aleatorio a colocar
        orientacion = random.choice(vars.p_cardinales) # orientacion aleatoria
        barco = (pos_ini, tam_barco, orientacion)
        if barco[1] == 1:
            barco_construido = (vars.dic_tableros["maquina"],f.check_coord(vars.dic_tableros["maquina"], barco[0]))
            if barco_construido[1]:
                barco_construido[0][barco[0]] = "O"

        else:
            barco_construido = f.boat_constructor(vars.dic_tableros["maquina"], barco) # añadimos el barco al tablero
            if len(barco_construido) == 3 and barco_construido[1]:
                for pos in barco_construido[2]:
                    vars.dic_tableros["maquina"][pos] = "O"
        if barco_construido[1]:
            print(f"El barco que se va a poner en el tablero -> {barco}")
            vars.tam_barcos.remove(int(barco[1])) # si es valido borramos el barco de la lista
            print(vars.dic_tableros["maquina"]) 
            print("Barcos restantes para colocar:", vars.tam_barcos)
    enable_print()
    ###################################################################################
    # Debería de tener los barcos del jugador y la máquina colocados:
    print("Jugador ->",vars.dic_tableros["jugador"]) 
    print("\n===========================================\n")
    print("Máquina ->",vars.dic_tableros["maquina"])
    

    '''
    dic_vidas = {"jugador":20,"maquina":20}
    for barco, coordenadas in vars.barcos.items(): # itero sobre el diccionario
        for pos in coordenadas: # itero sobre la lista de posiciones
                vars.dic_tableros["maquina"][pos] = "O"
                vars.dic_tableros["jugador"][pos] = "O"
    '''

    while 0 not in vars.dic_vidas.values():
        print(f"VIDAS:\n Tú -> {vars.dic_vidas["jugador"]} vidas \n Rival -> {vars.dic_vidas["maquina"]} vidas")
        print("\nTú turno, apunta bien...")
        pos = f.obtener_tupla()
        if vars.dic_tableros["jugador_disp"][pos] == " ":
            tocado = f.disparar(vars.dic_tableros["maquina"], pos)
            if tocado:
                vars.dic_tableros["jugador_disp"][pos] = "X"
                vars.dic_vidas["maquina"] -= 1
            else:
                vars.dic_tableros["jugador_disp"][pos] = "-"
            
        else:
            print("Apunta mejor, que esa posición ya la has marcado\n")
        
        f.imprimir_tablero("jugador")

        print("¡Cuidado! Le toca a tu rival\n")
        pos = (random.randint(0,9),random.randint(0,9))
        print(f"Te han disparado en la posición {pos} y...\n")
        if vars.dic_tableros["maquina_disp"][pos] == " ":
            tocado = f.disparar(vars.dic_tableros["jugador"], pos)
            if tocado:
                vars.dic_tableros["maquina_disp"][pos] = "X"
                vars.dic_vidas["jugador"] -= 1
            else:
                vars.dic_tableros["maquina_disp"][pos] = "-"
                print("Agua :), has tenido suerte esta vez\n")
            
        else:
            print("Apunta mejor, que esa posición ya la has marcado\n")
    
        f.imprimir_tablero("jugador")

    for vidas in vars.dic_vidas.values():
        if vidas != 0:
            print("¡¡¡ENHORABUENA!!! Has ganado")
            break
        else:
            print("Ohhhhhhhhh... Has perdido")
            break

    reiniciar_partida = input("¿Jugamos otra vez?")
    if reiniciar_partida.lower() == "no":
        print ("¡¡¡Nos alegra que hayas jugado con nostros, te esperamos pronto!!!")
    else:
        print("Entendemos que te has quedado con más ganas, vamos a jugar otra vez!!")
        f.reiniciar_partida()
        main()
        

if __name__ == "__main__":
    main()
