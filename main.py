
import utils

# BUCLE PARA INICIAR EL JUEGO

while True:
        ingreso = input("Bienvenid@s a HUNDIR LA FLOTA. Marca 1 para comenzar a jugar")
        if ingreso!="":
                u.crear_tj1()
                u.colocar_flotaj1(flotaj1, tab_jug1)
                print("Estos son tus tableros \n")
                u.crear_tj2()
                u.colocar_flotaj2(flotaj2, tab_jug2)          
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
