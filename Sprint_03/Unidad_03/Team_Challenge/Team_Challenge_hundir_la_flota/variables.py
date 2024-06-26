import numpy as np
import funciones as f

# CONSTANTES
p_cardinales =["n","s","e","o"]
tam = 10
tam_barcos = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

# VARIABLES
dic_tableros = {"jugador": np.full((tam, tam), " ", dtype=object), # donde estén nuestros barcos
                "jugador_disp": np.full((tam, tam), " ", dtype=object), # donde vamos a disparar
                "maquina": np.full((tam, tam), " ", dtype=object), 
                "maquina_disp": np.full((tam, tam), " ", dtype=object),}
dic_vidas = {"jugador": 20,"maquina": 20}
barco_a_poner = []
