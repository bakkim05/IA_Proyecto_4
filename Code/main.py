import time
from random import randint

#Funcion de población inicial
def pobl_ini(poblacion):
    i = 0
    j = 0
    for i in range(100):
        individuo = []
        for j in range(7):
            individuo.append(randint(-100, 100))
        poblacion.append(individuo)
        j=0

#Funcion para leer el archivo de datos
def leer_csv():
    print("datos leidos")


#Funcion para evaluar los datos en las funciones 
def eval_datos():
    #y = 0
    print("datos evaluados")


#Funcion para escoger los miembros mas aptos de la poblacion (50% del total)
def selec_indi():
    print("Individuos seleccionados")


#Funcion para realizar el cruce de los individuos
def cruce():
    print("individuos cruzados")


#Funcion para

def main():
    timeout = time.time() + 60*5   # 5 minutes from now

    poblacion = []
    
    #funcion para cargar los datos del excel
    leer_csv()

    #llamar función poblacion inicial (crea arrelgo de arreglos)
    pobl_ini(poblacion)

    while True:
        test = 0
        if time.time() > timeout:
            break

        #llamar funcion para evaluar datos del excel 
        eval_datos()

        #llamar funcion para escoger 50% mejor 
        selec_indi()

        #llamar funcion para cruzar
        cruce()

        

        
main()