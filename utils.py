import random 

import numpy as np

# 1º Crear los tableros de los jugadores; 1 para cada jugador y cada uno con su espejo.

def crear_tj1():
    global tab_jug1, tab_1_shoot

    tab_jug1 =np.full( (10, 10), '_' )
    tab_1_shoot = np.full( (10, 10), '_' )
    return(tab_jug1, tab_1_shoot)

def crear_tj2():
    global tab_jug2, tab_2_shoot

    tab_jug2 =np.full( (10, 10), '_' )
    tab_2_shoot = np.full( (10, 10), '_' )
    return(tab_jug2, tab_2_shoot)


tablero1 = crear_tj1()
tablero2 = crear_tj2()

# 2º Crear barco aleatorio 

def crear_barco_aleatorioj1(eslora):
    fila = random.randint(0,9)
    columna = random.randint(0,9)
    barco_aleatorioj1 = [(fila, columna)]

    orientacion = random.choice(["Horizontal", "Vertical"])
    while len(barco_aleatorioj1) < eslora:
        if orientacion == "Horizontal":
            columna = columna + 1
            barco_aleatorioj1.append((fila, columna))
        else:
            fila = fila + 1
            barco_aleatorioj1.append((fila, columna))
    
        if barco_aleatorioj1 and all(barco_aleatorioj1[fila, columna] == '_' for fila, columna in barco_aleatorioj1):
    return barco_aleatorioj1

def crear_barco_aleatorioj2(eslora):
    fila = random.randint(0,9)
    columna = random.randint(0,9)
    barco_aleatorioj2 = [(fila, columna)]

    orientacion = random.choice(["Horizontal", "Vertical"])
    while len(barco_aleatorioj2) < eslora:
        if orientacion == "Horizontal":
            columna = columna + 1
            barco_aleatorioj2.append((fila, columna))
        else:
            fila = fila + 1
            barco_aleatorioj2.append((fila, columna))
   
        if barco_aleatorioj2 and all(barco_aleatorioj2[fila, columna] == '_' for fila, columna in barco_aleatorioj2):
    return barco_aleatorioj2
# (AQUI DEBERIA DETERMINAR LOS LIMITES DEL TABLERO PARA QUE LOS BARCOS NO SE SALGAN Y VERIFICAR QUE NO SE SUPERPONGAN) .

        
# 3º Crear la flotas de barcos

def crear_flotaj1():
    flota =[]
    eslora=[2,2,2,3,3,4]
    for n in eslora:
       flota.append(crear_barco_aleatorioj1(n))
    return flota 



def crear_flotaj2():
    flota =[]
    eslora=[2,2,2,3,3,4]
    for n in eslora:
       flota.append(crear_barco_aleatorioj2(n))
    return flota 
flotaj1 = crear_flotaj1()
flotaj2 = crear_flotaj2()

# 4º Colocar 1 Barco

def colocar_barcoj1 (barcoj1,tab_jug1):
    for casilla in barcoj1:
        tab_jug1[casilla]= "O"
    return tab_jug1

def colocar_barcoj2 (barcoj2,tab_jug2):
    for casilla in barcoj2:
        tab_jug2[casilla]= "O"
    return tab_jug2


# 5º Colocar flotas en el tablero

def colocar_flotaj1(flotaj1, tab_jug1): 
    for barcoj1 in flotaj1:
        colocar_barcoj1(barcoj1, tab_jug1)
    return tab_jug1

def colocar_flotaj2(flotaj2, tab_jug2): 
    for barcoj2 in flotaj2:
        colocar_barcoj2(barcoj2, tab_jug2)
    return tab_jug2




# Disparar en los tableros
def dispararj1():
    Fila=int(input())
    Columna=int(input())
    if tab_jug2[Fila,Columna]=="O":
        tab_1_shoot[Fila,Columna]="X"
        tab_jug2[Fila,Columna]="X"
        print(tab_1_shoot) 
        print("OH NO!! HE FALLADO, TU TURNO")
        return dispararj1()
    else:
        tab_1_shoot[Fila,Columna]="A"
        tab_jug2[Fila,Columna]="A"
        print("TE TENGO!, AQUI VOY  DE NUEVO...")
        return False
    

def dispararj2():
    Fila=randint(0,9)
    Columna=randint(0,9)
    if tab_jug1[Fila,Columna]=="O":
        tab_jug1[Fila,Columna]="X"             
        print("TE ENCONTRE, MI TURNO NUEVAMENTE")
        return dispararj2()
    elif tab_jug1[Fila,Columna]=="_":
        tab_jug1[Fila,Columna]="A"
        print("POR POCO... VENGA, TE TOCA")
        return False
    else:
        return dispararj2()      




