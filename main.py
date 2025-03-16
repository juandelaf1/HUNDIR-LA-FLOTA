
import utils

tablero1 = crear_tj1()
tablero2 = crear_tj2()
barcoj1 = crear_barco_aleatorioj1()
barcoj2 = crear_barco_aleatorioj2()
flotaj1 = crear_flotaj1()
flotaj2 = crear_flotaj2()
tablero1 =colocar_barcoj1()
tablero2 = colocar_barcoj2()
tablero1 = colocar_flotaj1()
tablero2 = colocar_flotaj2()
tab_1_shoot = dispararj1()
tab_2_shoot = dispararj2()

# BUCLE PARA INICIAR EL JUEGO

while True:
        ingreso = input("Bienvenid@s a HUNDIR LA FLOTA. Marca 1 para comenzar a jugar")
        if ingreso!="":
                crear_tj1()
                colocar_flotaj1()
                print("Estos son tus tableros \n")
                crear_tj2()
                colocar_flotaj2()          
        break
# BUCLE PARA DETERMINAR DURACION DEL JUEGO
while True:
    print(tab_1_shoot)
    print()
    print(tab_jug1)
    ingresar=input("Marcar 2 para comenzar disparar=") 
    if ingresar=="2":
        if "O" in tab_jug1 and "O" in tab_jug2:
            dispararj1()
            dispararj2()
        else:
            break
